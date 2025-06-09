"""
Core Object Base Class

Defines the base class for all interactive and visual elements in the game.
All game objects (enemies, platforms, traps, etc.) should inherit from this class.
"""

import pygame
from Utils.settings import *


class Object(pygame.sprite.Sprite):
    """
    Base class for all game objects using Pygame's Sprite system.
    """

    def __init__(self, x: int, y: int, width: int, height: int, name: str = None):
        """
        Initialize the object with position, size, and optional name.

        Args:
            x (int): X position on the screen.
            y (int): Y position on the screen.
            width (int): Width of the object in pixels.
            height (int): Height of the object in pixels.
            name (str, optional): Identifier name for the object (used for logic/grouping).
        """
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)  # Transparent surface
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win: pygame.Surface, offset_x: int, offset_y: int):
        """
        Draw the object on the window, applying camera offsets.

        Args:
            win (Surface): The Pygame window surface to draw onto.
            offset_x (int): Horizontal camera offset.
            offset_y (int): Vertical camera offset.
        """
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))
