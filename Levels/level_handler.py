"""
Core Level Loader

This module dispatches level creation functions based on the selected level number.
Each level is implemented in its own file for modularity and clarity.
"""

from Levels.level_01 import create_level_1
from Levels.level_02 import create_level_2
from Levels.level_03 import create_level_3


class Level:
    def __init__(self, level_number: int, block_size: int):
        """
        Initialize a Level instance.

        Args:
            level_number (int): The level number to load.
            block_size (int): The size of blocks used in the level (in pixels).
        """
        self.level_number = level_number
        self.block_size = block_size
        self.background = "yellow.png"

    def show_level(self):
        """
        Returns the game objects and decorations for the specified level.

        Returns:
            tuple[list, list]: A tuple containing the game objects and decorative elements.
        """
        level_creators = {
            1: create_level_1,
            2: create_level_2,
            3: create_level_3
        }

        create_level = level_creators.get(self.level_number)
        if create_level:
            return create_level(self.block_size)
        return [], []
