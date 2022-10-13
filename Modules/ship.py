"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
"""

from turtle import distance
from pyglet.text import Label
from pyglet.shapes import Circle
from pyglet.graphics import Group
from helpers import OFFSETS, calculate_distance, object_to_screen, calculate_distance_precise, main_batch, \
     TEXT_OFFSET_X, TEXT_OFFSET_Y, CONFIG
from mapping import ships
from Modules.display_object import DisplayObject
import time
import win32api
from pynput.keyboard import Key, Controller
import math

SHIP_COLOR = (100, 0, 0)  # The color we want the indicator circle to be
CIRCLE_SIZE = 10  # The size of the indicator circle we want


class Ship(DisplayObject):
    """
    Class to generate information for a ship object in memory
    """

    def __init__(self, memory_reader, actor_id, address, my_coords, raw_name):
        """
        Upon initialization of this class, we immediately initialize the
        DisplayObject parent class as well (to utilize common methods)

        We then set our class variables and perform all of our info collecting
        functions, like finding the actors base address and converting the
        "raw" name to a more readable name per our Mappings. We also create
        a circle and label and add it to our batch for display to the screen.

        All of this data represents a "Ship". If you want to add more, you will
        need to add another class variable under __init__ and in the update()
        function

        :param memory_reader: The SoT MemoryHelper Object we use to read memory
        :param address: The address in which the AActor begins
        :param my_coords: a dictionary of the local players coordinates
        :param raw_name: The raw actor name used to translate w/ mapping.py
        """
        # Initialize our super-class
        super().__init__(memory_reader)

        self.actor_id = actor_id
        self.address = address
        self.actor_root_comp_ptr = self._get_root_comp_address(address)
        self.my_coords = my_coords
        self.raw_name = raw_name

        # Generate our Ship's info
        self.name = ships.get(self.raw_name).get("Name")
        self.coords = self._coord_builder(self.actor_root_comp_ptr,
                                          self.coord_offset)
        self.distance = calculate_distance(self.coords, self.my_coords)

        self.screen_coords = object_to_screen(self.my_coords, self.coords)
        self.speed = 0
        self.speed_x = 0
        self.speed_y = 0
        self.player_speed = 0
        self.player_speed_x = 0
        self.player_speed_y = 0

        self.old_coords = self.coords
        self.old_player_coords = self.my_coords
        self.old_time = time.time()
        self.old_speed = 0
        self.old_speed_x = 0
        self.old_speed_y = 0
        self.old_player_speed = 0
        self.old_player_speed_x = 0
        self.old_player_speed_y = 0
        self.old_distance = self.distance

        self.keyboard = Controller()

        # All of our actual display information & rendering
        self.color = SHIP_COLOR
        self.group = Group()
        self.text_str = self._built_text_string()
        self.text_render = self._build_text_render()
        self.icon = self._build_circle_render()

        # Used to track if the display object needs to be removed
        self.to_delete = False

    def _build_circle_render(self) -> Circle:
        """
        Creates a circle located at the screen coordinates (if they exist).
        Uses the color specified in our globals w/ a size of 10px radius.
        Assigns the object to our batch & group
        """
        if self.screen_coords:
            return Circle(self.screen_coords[0], self.screen_coords[1],
                          CIRCLE_SIZE, color=self.color, batch=main_batch,
                          group=self.group)

        return Circle(0, 0, 10, color=self.color, batch=main_batch,
                      group=self.group)

    def _built_text_string(self) -> str:
        """
        Generates a string used for rendering. Separate function in the event
        you need to add more data (Sunk %, hole count, etc)
        """
        return f"{self.name} - {self.distance}m - {self.speed}m/s"

    def _build_text_render(self) -> Label:
        """
        Function to build our actual label which is sent to Pyglet. Sets it to
        be located at the screen coordinated + our text_offsets from helpers.py

        Assigns the object to our batch & group

        :rtype: Label
        :return: What text we want displayed next to the ship
        """
        if self.screen_coords:
            return Label(self.text_str,
                         x=self.screen_coords[0] + TEXT_OFFSET_X,
                         y=self.screen_coords[1] + TEXT_OFFSET_Y,
                         batch=main_batch, group=self.group)

        return Label(self.text_str, x=0, y=0, batch=main_batch,
                     group=self.group)

    def update(self, my_coords: dict):
        """
        A generic method to update all the interesting data about a ship
        object, to be called when seeking to perform an update on the
        Actor without doing a full-scan of all actors in the game.

        1. Determine if the actor is what we expect it to be
        2. See if any data has changed
        3. Update the data if something has changed

        In theory if all data is the same, we could *not* update our Label's
        text, therefore saving resources. Not implemented, but a possibility
        """
        if self._get_actor_id(self.address) != self.actor_id:
            self.to_delete = True
            self.icon.delete()
            self.text_render.delete()
            return

        self.my_coords = my_coords
        self.coords = self._coord_builder(self.actor_root_comp_ptr,
                                          self.coord_offset)
        new_distance = calculate_distance(self.coords, self.my_coords)

        #Calculate all speeds/velocities
        if time.time() - self.old_time >= 0.5:
            timeChange = time.time() - self.old_time

            #calculate speeds
            self.speed = round(calculate_distance_precise(self.coords, self.old_coords) / timeChange, 2)
            self.speed_x = round((self.coords["x"] - self.old_coords['x']) / timeChange, 2)
            self.speed_y = round((self.coords["y"] - self.old_coords['y']) / timeChange, 2)
            self.player_speed = round(calculate_distance_precise(self.my_coords, self.old_player_coords), 2)
            self.player_speed_x = round((self.my_coords["x"] - self.old_player_coords['x']) / timeChange, 2)
            self.player_speed_y = round((self.my_coords["y"] - self.old_player_coords['y']) / timeChange, 2)
            
            #print(str(self.player_speed_x) + ', ' + str(self.player_speed_y))
            #print(str(self.my_coords['cam_x']) + ', ' + str(self.my_coords['cam_y']))

            #reset old values
            self.old_coords = self.coords
            self.old_player_coords = self.my_coords
            self.old_time = time.time()
            self.old_speed = self.speed
            self.old_speed_x = self.speed_x
            self.old_speed_y = self.speed_y
            self.old_player_speed_x = self.player_speed_x
            self.old_player_speed_y = self.player_speed_y

        self.screen_coords = object_to_screen(self.my_coords, self.coords)

        if self.screen_coords:
            # Ships have two actors dependant on distance. This switches them
            # seamlessly at 1750m
            if "Near" in self.name and new_distance > 1750:
                self.group.visible = False
            elif "Near" not in self.name and new_distance < 1750:
                self.group.visible = False
            else:
                self.group.visible = True

            # Update the position of our circle and text
            self.icon.x = self.screen_coords[0]
            self.icon.y = self.screen_coords[1]
            self.text_render.x = self.screen_coords[0] + TEXT_OFFSET_X
            self.text_render.y = self.screen_coords[1] + TEXT_OFFSET_Y

            # Update our text to reflect out new distance
            self.distance = new_distance
            self.text_str = self._built_text_string()
            self.text_render.text = self.text_str

        else:
            # if it isn't on our screen, set it to invisible to save resources
            self.group.visible = False

        #cannon aimbot
        if CONFIG.get('CANNON_AIMBOT_ENABLED'):  

            #set constants
            cannonballSpeed = 68
            gravity = 9.8
            screenSizeX = 2560
            sleepConstant = 0.001

            distanceFromCenter = -(self.icon.x - (screenSizeX / 2))
                    
            if win32api.GetKeyState(0x02) < 0 and win32api.GetKeyState(0x10) < 0 and 0 < self.distance < 471 and abs(distanceFromCenter) < 400:

                #find speed of player

                #do math
                requiredAngleStationary = 0.5 * (math.asin((gravity * (self.distance - 5)) / (cannonballSpeed ** 2)))
                flightTime = 2 * cannonballSpeed * math.sin(requiredAngleStationary) / gravity
                relativeSpeed_x = self.speed_x - self.player_speed_x #speed of target - speed of player
                relativeSpeed_y = self.speed_y - self.player_speed_y #speed of target - speed of player
                #relativeSpeed = math.sqrt((relativeSpeed_x ** 2) + (relativeSpeed_y ** 2))
                futureCoords = self.coords.copy()
                futureCoords['x'] = futureCoords['x'] + relativeSpeed_x * flightTime
                futureCoords['y'] = futureCoords['y'] + relativeSpeed_y * flightTime
                futureDistance = calculate_distance(futureCoords, self.my_coords)
                try:
                    requiredAngle = math.degrees(0.5 * (math.asin((gravity * (futureDistance - 5)) / (cannonballSpeed ** 2))))
                except:
                    requiredAngle = 0
                futureScreenCoords = object_to_screen(self.my_coords, futureCoords)
                try:
                    futureDistanceFromCenter = -(futureScreenCoords[0] - (screenSizeX / 2))
                except:
                    futureDistanceFromCenter = 0
                cameraAngle = self.my_coords["cam_x"]
                sleepTime = sleepConstant * abs(cameraAngle - requiredAngle)

                '''TODO
                - find relative horizontal speed of target
                - calculate horizontal distance traveled to calculate approxmiate lead angle
                - find speed of target away from boat
                - calculate new distance from boat after flight time
                - calculate new requiredAngle

                - if self.my_coords['cam_y'] = 0, forward movement is positive x axis
                - find relative horizontal speed by making right triangle with the rate of separation on both axis
                - IMPORTANT: find horizontal offset that results in the same horizontal speed as target
                - IMPORTANT: if relativeSpeed_x > relativeSpeed_y, ship is traveling along the x axis and horizontal speed is equal to the speed along the x axis
                '''
                print(str(futureDistanceFromCenter) + ' pixels from target | ' + str(requiredAngle) + ' required angle | ' + str(cameraAngle) + ' current angle | ' + str(self.speed) + ' speed')

                if futureDistanceFromCenter > 10:
                    self.keyboard.press('a')
                    time.sleep(0.005)
                    self.keyboard.release('a')
                elif futureDistanceFromCenter < -10:
                    self.keyboard.press('d')
                    time.sleep(0.005)
                    self.keyboard.release('d')
                if cameraAngle < requiredAngle - 0.01:
                    self.keyboard.press('w')
                    time.sleep(sleepTime)
                    self.keyboard.release('w')
                elif cameraAngle > requiredAngle + 0.01:
                    self.keyboard.press('s')
                    time.sleep(sleepTime)
                    self.keyboard.release('s')