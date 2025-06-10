from Utils.settings import load_sprite_sheet_cached, FPS
from Core.objects import Object
import pygame

class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height, loop_fire=False):
        """
        Initialize the fire trap object.

        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.
            width (int): Width of the sprite.
            height (int): Height of the sprite.
            loop_fire (bool): If True, the fire cycles on/off endlessly.
        """
        super().__init__(x, y, width, height, "fire")
        self.sprites = load_sprite_sheet_cached("Traps", "Fire", width, height)
        self.image = self.sprites["off"][0]
        self.mask = pygame.mask.from_surface(self.image)

        self.animation_count = 0
        self.animation_name = "off"

        self.is_igniting = False
        self.ignite_timer = 0

        self.is_extinguishing = False
        self.extinguish_timer = 0

        self.loop_fire = loop_fire

    def turn_on(self):
        """Activate fire animation."""
        self.animation_name = "on"
        self.is_extinguishing = True

    def turn_off(self):
        """Deactivate fire animation."""
        self.animation_name = "off"

    def hit(self):
        """Play hit animation and prepare to turn on fire."""
        self.animation_name = "hit"
        self.is_igniting = True

    def update(self):
        """
        Update the animation frame and state transitions for the fire object.
        """
        sprites = self.sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

        if self.is_igniting:
            self.ignite_timer += 1
            if self.ignite_timer > FPS / 3:
                self.turn_on()
                self.ignite_timer = 0
                self.is_igniting = False

        if self.is_extinguishing:
            self.extinguish_timer += 1
            if self.extinguish_timer > FPS * 2 and not self.loop_fire:
                self.turn_off()
                self.extinguish_timer = 0
                self.is_extinguishing = False
