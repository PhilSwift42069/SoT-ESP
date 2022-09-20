"""
@Author PhilSwift42069
"""

from pyglet.text import Label
from pyglet.shapes import Circle
from pyglet.graphics import Group
from helpers import calculate_distance, object_to_screen, main_batch, \
     TEXT_OFFSET_X, TEXT_OFFSET_Y
from mapping import ships
from Modules.display_object import DisplayObject

ICON_COLOR = (0,0,100)

class Fishing(DisplayObject):
    """
    Fishing autopilot
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

        # Used to track if the display object needs to be removed
        self.to_delete = False

    def update(self, my_coords: dict):
        """
        A generic method to update all the interesting data about the fisherman
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
            return
        
    def fisherman(self):
