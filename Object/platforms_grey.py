from Utils.settings import FPS, load_sprite_sheet_cached
from Core.objects import Object
import pygame

class PlatformsGrey(Object):
    """
    Represents a grey moving platform with directional animation (left or right).
    """
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height, direction):
        """
        Initialize a grey platform.

        Args:
            x (int): X-coordinate of the platform.
            y (int): Y-coordinate of the platform.
            width (int): Width of the platform.
            height (int): Height of the platform.
            direction (str): Direction of movement ('left' or 'right').
        """
        super().__init__(x, y, width, height, "platformsGrey")
        self.platform_sprites = load_sprite_sheet_cached("Traps", "Platforms", width, height)
        self.direction = direction
        self.animation_name = "Grey On (32x8)"
        self.image = self.platform_sprites["Grey Off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0

    def activate(self):
        """Switch platform animation to 'on' state."""
        self.animation_name = "Grey On (32x8)"

    def deactivate(self):
        """Switch platform animation to 'off' state."""
        self.animation_name = "Grey Off"

    def update(self):
        """Update platform animation and orientation each frame."""
        sprites = self.platform_sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        if self.direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0
