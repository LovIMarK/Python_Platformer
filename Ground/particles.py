from Utils.settings import *
import pygame
import random

class Particles(pygame.sprite.Sprite):
    """
    Particle used for visual effects like wind or smoke.
    Repeats itself automatically after its lifetime ends.
    """

    def __init__(self, x: int, y: int, width: int, height: int, dy: int = -2):
        """
        Initialize a single particle.

        Args:
            x (int): Initial x position.
            y (int): Initial y position.
            width (int): Width of the particle sprite.
            height (int): Height of the particle sprite.
            dy (int, optional): Vertical movement speed per frame. Defaults to -2 (upward).
        """
        super().__init__()
        self.origin = (x, y)
        self.width = width
        self.height = height
        self.dy = dy
        self.rect = pygame.Rect(x, y, width, height)

        self.sprites = load_sprite_sheet_cached("Other", "", width, height)
        self.images = self.sprites["Dust Particle"]
        self.image = self.images[0]
        self.image.set_alpha(170)
        self.mask = pygame.mask.from_surface(self.image)

        self.animation_count = 0
        self.animation_delay = 3
        self.reset()

    def reset(self):
        """
        Reset the particle to its origin and restart its animation and lifetime.
        """
        self.rect.x, self.rect.y = self.origin
        self.lifetime = random.randint(40, 80)
        self.animation_count = 0

    def update(self):
        """
        Updates the particle's animation frame and movement. Automatically
        resets the particle once its lifetime expires.
        """
        self.rect.y += self.dy
        self.lifetime -= 1

        if self.lifetime <= 0:
            self.reset()

        sprite_index = (self.animation_count // self.animation_delay) % len(self.images)
        self.image = self.images[sprite_index]
        self.animation_count += 1

    def draw(self, win: pygame.Surface, offset_x: int, offset_y: int):
        """
        Draw the particle on the screen at its position relative to the camera.

        Args:
            win (pygame.Surface): The window surface to draw on.
            offset_x (int): Horizontal camera offset.
            offset_y (int): Vertical camera offset.
        """
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))
