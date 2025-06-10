from Utils.settings import FPS, load_sprite_sheet_cached
from Core.objects import Object
from Traps.dart import Dart
import pygame

class Bee(Object, pygame.sprite.Sprite):
    """
    Represents a bee enemy that can shoot projectiles (Dar) and be destroyed.
    """
    ANIMATION_DELAY = 4

    def __init__(self, x, y, width, height, dist):
        """
        Initialize the bee enemy.

        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.
            width (int): Width of the sprite.
            height (int): Height of the sprite.
            dist (int): Maximum range for its projectile.
        """
        super().__init__(x, y, width, height, "bee")
        self.bee_sprites = load_sprite_sheet_cached("Enemies", "Bee", width, height)
        self.animation_name = "Idle (36x34)"
        self.image = self.bee_sprites[self.animation_name][0]
        self.mask = pygame.mask.from_surface(self.image)

        self.dart = Dart(self.rect.x + 20, self.rect.y + 34, 16, 16)
        self.dart_exists = False

        self.animation_count = 0
        self.fire = False
        self.fire_count = 0

        self.exist = True
        self.hit = False
        self.hit_count = 0
        self.dist = dist

    def stop(self):
        """Remove the bee from the game."""
        self.exist = False

    def attack(self):
        """Start firing projectile if bee is active."""
        if self.exist:
            self.fire = True
            self.set_fire_animation()
        else:
            self.fire = False
            self.dart_exists = False

    def stop_attack(self):
        """Stop firing and return to idle if not hit."""
        if not self.hit:
            self.animation_name = "Idle (36x34)"
        self.fire = False

    def set_fire_animation(self):
        """Set attack animation if not hit."""
        if not self.hit:
            self.animation_name = "Attack (36x34)"

    def hit_by_projectile(self):
        """Set hit animation and flag bee as hit."""
        self.animation_name = "Hit (36x34)"
        self.hit = True

    def update(self):
        """Update the bee's animation and status each frame."""
        sprites = self.bee_sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0

        if self.fire:
            self.fire_count += 1
        if self.hit:
            self.hit_count += 1

        if self.hit_count > FPS / 2:
            self.stop()

        if self.fire_count > FPS / 2:
            self.fire_count = 0
            self.stop_attack()
