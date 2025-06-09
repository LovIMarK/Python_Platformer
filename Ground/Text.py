from Utils.settings import get_text_tile
from Core.objects import Object
import pygame

class Text(Object):
    """
    Represents a text element rendered from a tile-based font system.
    """

    def __init__(self, x, y, size, location, color="black"):
        """
        Initialize a text object at a given position.

        Args:
            x (int): X-coordinate for the text.
            y (int): Y-coordinate for the text.
            size (int): Size of each character tile.
            location (tuple): Location of the character in the tile sheet.
            color (str, optional): Text color (default is "black").
        """
        super().__init__(x, y, size, size, "text")
        text_surface = get_text_tile(size, location, color)
        self.image.blit(text_surface, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
