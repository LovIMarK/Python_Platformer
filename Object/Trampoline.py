import pygame
from Utils.settings import FPS, load_sprite_sheet_cached
from Core.objects import Object

class Trampoline(Object):
    """Represents an animated trampoline object."""

    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        """
        Initialize a trampoline object.

        Args:
            x (int): X coordinate of trampoline.
            y (int): Y coordinate of trampoline.
            width (int): Width of the trampoline.
            height (int): Height of the trampoline.
        """
        super().__init__(x, y, width, height, "trampoline")
        self.sprites = load_sprite_sheet_cached("Traps", "Trampoline", width, height)
        self.image = self.sprites["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)

        self.animation_frame = 0
        self.current_animation = "Idle"
        self.is_jumping = False
        self.jump_timer = 0

    def update(self):
        """
        Update the trampoline animation each frame.
        """
        current_sprites = self.sprites[self.current_animation]
        sprite_index = (self.animation_frame // self.ANIMATION_DELAY) % len(current_sprites)
        self.image = current_sprites[sprite_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

        self.animation_frame += 1

        # Reset the animation cycle if complete
        if self.animation_frame // self.ANIMATION_DELAY >= len(current_sprites):
            self.animation_frame = 0

        # Handle trampoline jump timing
        if self.is_jumping:
            self.jump_timer += 1
            if self.jump_timer > FPS / 3:
                self.stop_jumping()

    def start_jumping(self):
        """
        Trigger the trampoline's jumping animation.
        """
        self.current_animation = "Jump (28x28)"
        self.is_jumping = True
        self.jump_timer = 0

    def stop_jumping(self):
        """
        Reset trampoline to idle state after jump animation.
        """
        self.current_animation = "Idle"
        self.is_jumping = False
        self.jump_timer = 0
