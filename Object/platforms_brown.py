from Utils.settings import FPS, load_sprite_sheet_cached
from Core.objects import Object
import pygame

class PlatformsBrown(Object):
    """
    Represents a brown platform that can switch between on and off states with animations.
    """
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        """
        Initialize a brown platform.

        Args:
            x (int): X-coordinate of the platform.
            y (int): Y-coordinate of the platform.
            width (int): Width of the platform.
            height (int): Height of the platform.
        """
        super().__init__(x, y, width, height, "platformsBrown")
        self.platform_sprites = load_sprite_sheet_cached("Traps", "Platforms", width, height)
        self.animation_name = "Brown Off"
        self.image = self.platform_sprites[self.animation_name][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0

    def activate(self):
        """Switch platform animation to 'on' state."""
        self.animation_name = "Brown On (32x8)"

    def deactivate(self):
        """Switch platform animation to 'off' state."""
        self.animation_name = "Brown Off"

    def update(self):
        """Update platform animation each frame."""
        sprites = self.platform_sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

        self.animation_count += 1
        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0
