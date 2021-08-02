"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
For community support, please contact me on Discord: DougTheDruid#2784
"""


import struct
from memory_helper import ReadMemory
from mapping import ship_keys
from helpers import OFFSETS, CONFIG
from ship import Ship


STEAM_VERSION = False

UWORLD_PATTERN = "48 8B 05 ? ? ? ? 48 8B 88 ? ? ? ? 48 85 C9 74 06 48 8B 49 70"
GOBJECT_PATTERN = "89 0D ? ? ? ? 48 8B DF 48 89 5C 24"
GNAME_PATTERN = "48 8B 1D ? ? ? ? 48 85 DB 75 ? B9 08 04 00 00"

if STEAM_VERSION:
    UWORLDBASE = 0x6E685B
    GOBJECTBASE = 0x15D11DB
    GNAMEBASE = 0x153DF2A

else:
    UWORLDBASE = 0x6E5F5B
    GOBJECTBASE = 0x15E9D14
    GNAMEBASE = 0x14FFCF8


class SoTMemoryReader:
    """
    Wrapper class to handle reading data from the game, parsing what is
    important, and returning it to be shown by pyglet
    """

    def __init__(self):
        """
        Upon initialization of this object, we want to find the base address
        for the SoTGame.exe, then begin to load in the static addresses for the
        uWorld, gName, gObject, and uLevel objects.

        We also poll the local_player object to get a first round of coords.
        When running read_actors, we update the local players coordinates
        using the camera-manager object

        Also initialize a number of class variables which help us cache some
        basic information
        """
        self.rm = ReadMemory("SoTGame.exe")
        base_address = self.rm.base_address

        u_world_offset = self.rm.read_ulong(base_address + UWORLDBASE + 3)
        u_world = base_address + UWORLDBASE + u_world_offset + 7
        self.world_address = self.rm.read_ptr(u_world)

        g_name_offset = self.rm.read_ulong(base_address + GNAMEBASE + 3)
        self.g_name = self.rm.read_ptr(base_address + GNAMEBASE
                                       + g_name_offset + 7)

        g_objects_offset = self.rm.read_ulong(base_address + GOBJECTBASE + 2)
        g_objects = base_address + GOBJECTBASE + g_objects_offset + 22
        self.g_objects = self.rm.read_ptr(g_objects)

        self.u_level = self.rm.read_ptr(self.world_address +
                                        OFFSETS.get('UWorld.PersistentLevel'))

        self.u_local_player = self._load_local_player()
        self.player_controller = self.rm.read_ptr(
            self.u_local_player + OFFSETS.get('ULocalPlayer.PlayerController')
        )

        self.my_coords = self._coord_builder(self.u_local_player)
        self.my_coords['fov'] = 90

        self.actor_name_map = {}
        self.server_players = []
        self.display_objects = []

    def _load_local_player(self) -> int:
        """
        Returns the local player object out of uWorld.UGameInstance.
        Used to get the players coordinates before reading any actors
        :rtype: int
        :return: Memory address of the local player object
        """
        game_instance = self.rm.read_ptr(
            self.world_address + OFFSETS.get('UWorld.OwningGameInstance')
        )
        local_player = self.rm.read_ptr(
            game_instance + OFFSETS.get('UGameInstance.LocalPlayers')
        )
        return self.rm.read_ptr(local_player)

    def update_my_coords(self):
        """
        Function to update the players coordinates and camera information
        storing that new info back into the my_coords field. Necesarry as
        we dont always run a full scan and we need a way to update ourselves
        """
        manager = self.rm.read_ptr(
            self.player_controller + OFFSETS.get('APlayerController.CameraManager')
        )
        self.my_coords = self._coord_builder(
            manager, OFFSETS.get('APlayerCameraManager.CameraCache') + OFFSETS.get('FCameraCacheEntry.FMinimalViewInfo'), fov=True)

    def _coord_builder(self, actor_address: int, offset=0x78, camera=True,
                       fov=False) -> dict:
        """
        Given a specific actor, loads the coordinates for that actor given
        a number of parameters to define the output
        :param int actor_address: Actors base memory address
        :param int offset: Offset from actor address to beginning of coords
        :param bool camera: If you want the camera info as well
        :param bool fov: If you want the FoV info as well
        :rtype: dict
        :return: A dictionary contianing the coordinate information
        for a specific actor
        """
        if fov:
            actor_bytes = self.rm.read_bytes(actor_address + offset, 44)
            unpacked = struct.unpack("<ffffff16pf", actor_bytes)
        else:
            actor_bytes = self.rm.read_bytes(actor_address + offset, 24)
            unpacked = struct.unpack("<ffffff", actor_bytes)

        coordinate_dict = {"x": unpacked[0]/100, "y": unpacked[1]/100,
                           "z": unpacked[2]/100}
        if camera:
            coordinate_dict["cam_x"] = unpacked[3]
            coordinate_dict["cam_y"] = unpacked[4]
            coordinate_dict["cam_z"] = unpacked[5]
        if fov:
            coordinate_dict['fov'] = unpacked[7]

        return coordinate_dict

    def _read_name(self, actor_id: int) -> str:
        """
        Looks up an actors name in the g_name DB based on the actor ID provided
        :param int actor_id: The ID for the actor we want to find the name of
        :rtype: str
        :return: The name for the actor
        """
        name_ptr = self.rm.read_ptr(self.g_name + int(actor_id / 0x4000) * 0x8)
        name = self.rm.read_ptr(name_ptr + 0x8 * int(actor_id % 0x4000))
        return self.rm.read_string(name + 0x10, 64)

    def read_actors(self):
        """
        Represents a full scan of every actor within our render distance.
        Will create an object for each type of object we are interested in,
        and store it in a class variable (display_objects).
        Then our main game loop updates those objects
        """
        for display_ob in self.display_objects:
            try:
                display_ob.text_render.delete()
            except:
                continue
        self.display_objects = []
        self.update_my_coords()

        actor_raw = self.rm.read_bytes(self.u_level + 0xa0, 0xC)
        actor_data = struct.unpack("<Qi", actor_raw)

        self.server_players = []
        for x in range(0, actor_data[1]):
            # We start by getting the ActorID for a given actor, and comparing
            # that ID to a list of "known" id's we cache in self.actor_name_map
            raw_name = ""
            actor_address = self.rm.read_ptr(actor_data[0] + (x * 0x8))
            actor_id = self.rm.read_int(
                actor_address + OFFSETS.get('AActor.actorId')
            )
            if actor_id not in self.actor_name_map and actor_id != 0:
                try:
                    raw_name = self._read_name(actor_id)
                    self.actor_name_map[actor_id] = raw_name
                except Exception as e:
                    print(str(e))
            elif actor_id in self.actor_name_map:
                raw_name = self.actor_name_map.get(actor_id)

            # Ignore anything we cannot find a name for
            if not raw_name:
                continue

            # If we have Ship ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py ship_keys object, interpret the actor
            # as a ship
            elif CONFIG.get('SHIPS_ENABLED') and raw_name in ship_keys:
                ship = Ship(self.rm, actor_id, actor_address, self.my_coords,
                            raw_name)
                if "Near" not in ship.name and ship.distance < 1720:
                    continue
                else:
                    self.display_objects.append(ship)

            # If we have the world players enabled in helpers.py, and the name
            # of the actor is AthenaPlayerState, we interpret the actor as a
            # player on the server.
            # NOTE: This will NOT give us information on nearby players for the
            # sake of ESP
            elif CONFIG.get('WORLD_PLAYERS_ENABLED') and "AthenaPlayerState" in raw_name:
                self.read_world_players(actor_address)

    def read_world_players(self, actor_address):
        """
        Reads information about an AthenaPlayerState actor (a server-level
        player object), to obtain into on who is on the server. Append the user
        to the list of players on the server for a given run
        :param actor_address: The memory address which the actor begins at
        """
        player_name_location = self.rm.read_ptr(
            actor_address + OFFSETS.get('APlayerState.PlayerName')
        )
        player_name = self.rm.read_name_string(player_name_location)

        if player_name \
                and player_name not in self.server_players \
                and player_name.replace(" ", "-") not in self.server_players:
            self.server_players.append(player_name)