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
    
    def _built_text_string(self):
        """
        Generates a string used for rendering. Separate function in the event
        you need to add more data or want to change formatting
        """
        return f"barrel - {self.distance}m"