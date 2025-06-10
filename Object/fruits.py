from Utils.settings import FPS, load_sprite_sheet_cached
from Core.objects import Object
import pygame

class Fruit(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height, kind):
        """
        Initialize a collectible fruit object.

        Args:
            x (int): X-coordinate of the fruit.
            y (int): Y-coordinate of the fruit.
            width (int): Width of the fruit sprite.
            height (int): Height of the fruit sprite.
            kind (str): Type of fruit (e.g., 'Apple', 'Bananas').
        """
        super().__init__(x, y, width, height, "fruit")
        self.fruit_sprites = load_sprite_sheet_cached("Items", "Fruits", width, height)
        self.animation_name = kind
        self.image = self.fruit_sprites[self.animation_name][0]
        self.mask = pygame.mask.from_surface(self.image)

        self.animation_count = 0
        self.collected = False
        self.collected_count = 0
        self.exist = True

    def collect(self):
        """Trigger the fruit collection animation."""
        self.animation_name = "Collected"
        self.collected = True

    def update(self):
        """Update fruit animation state each frame."""
        sprites = self.fruit_sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

        self.animation_count += 1

        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0

        if self.collected:
            self.collected_count += 1

        if self.collected_count > FPS / 3.2:
            self.exist = False
