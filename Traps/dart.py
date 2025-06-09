from Utils.settings import load_sprite_sheet_cached
from Core.objects import Object
import pygame

class Dart(Object):
    """
    Represents a projectile (dart) shot by the Bee enemy.
    """

    def __init__(self, x, y, width, height):
        """
        Initialize the dart.

        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.
            width (int): Width of the dart sprite.
            height (int): Height of the dart sprite.
        """
        super().__init__(x, y, width, height, "dart")
        self.sprites = load_sprite_sheet_cached("Enemies", "Bee", width, height)
        self.image = self.sprites["Bullet"][0]
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """
        Move the dart downward and update its hitbox and mask.
        """
        self.rect.y += 5
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
