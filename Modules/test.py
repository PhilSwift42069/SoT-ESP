"""
@Author https://github.com/PhilSwift42069
@Source https://github.com/PhilSwift42069/SoT-ESP
"""

from pyglet.text import Label
from pyglet.shapes import Circle
from pyglet.graphics import Group
from helpers import calculate_distance, object_to_screen, main_batch, \
     TEXT_OFFSET_X, TEXT_OFFSET_Y
from mapping import ships
from Modules.display_object import DisplayObject

ICON_COLOR = (0,0,100)

class Test(DisplayObject):
    """
    Test class for developing new features
    """

    def __init__(self, memory_reader, actor_id, address, my_coords, raw_name):
        """
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
        #self.name = ships.get(self.raw_name).get("Name")
        self.coords = self._coord_builder(self.actor_root_comp_ptr,
                                          self.coord_offset)
        self.distance = calculate_distance(self.coords, self.my_coords)

        self.screen_coords = object_to_screen(self.my_coords, self.coords)

        # All of our actual display information & rendering
        self.color = ICON_COLOR
        self.group = Group()
        self.text_str = self._built_text_string()
        self.text_render = self._build_text_render()
        #self.icon = self._build_circle_render()

        # Used to track if the display object needs to be removed
        self.to_delete = False
    
    def _built_text_string(self):
        """
        Generates a string used for rendering. Separate function in the event
        you need to add more data or want to change formatting
        """
        return f"barrel - {self.address}m"
    
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
        A generic method to update all the interesting data about a test
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

        self.screen_coords = object_to_screen(self.my_coords, self.coords)

        if self.screen_coords:
            # Ships have two actors dependant on distance. This switches them
            # seamlessly at 1750m
            '''
            if "Near" in self.name and new_distance > 1750:
                self.group.visible = False
            elif "Near" not in self.name and new_distance < 1750:
                self.group.visible = False
            else:
                self.group.visible = True
            '''

            # Update the position of our circle and text
            #self.icon.x = self.screen_coords[0]
            #self.icon.y = self.screen_coords[1]
            self.text_render.x = self.screen_coords[0] + TEXT_OFFSET_X
            self.text_render.y = self.screen_coords[1] + TEXT_OFFSET_Y

            # Update our text to reflect out new distance
            self.distance = new_distance
            self.text_str = self._built_text_string()
            self.text_render.text = self.text_str

        else:
            # if it isn't on our screen, set it to invisible to save resources
            self.group.visible = False
