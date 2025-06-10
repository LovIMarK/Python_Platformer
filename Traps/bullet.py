import pygame
from Utils.settings import load_sprite_sheet_cached
from Core.objects import Object

class Bullet(Object):
    """
    Represents a projectile (bullet) shot by enemies like the Plant.
    """

    def __init__(self, x, y, width, height):
        """
        Initialize the bullet.
        """
        super().__init__(x, y, width, height, "bullet")
        self.sprites = load_sprite_sheet_cached("Enemies", "Plant", width, height)
        self.image = self.sprites["Bullet"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.destroyed = False 

    def update(self):
        """
        Move the bullet and update its hitbox and mask.
        """
        self.rect.x -= 3 
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
