from Utils.settings import *
from Core.objects import Object
from bullet import Bullet
import pygame


class Plant(Object, pygame.sprite.Sprite):
    """
    Enemy Plant that shoots a bullet at the player.

    Behaviors:
    - Idle animation
    - Attack animation (shooting)
    - Hit animation (when destroyed)
    - Fires only if within range and active
    """

    ANIMATION_DELAY = 6             
    FIRE_INTERVAL = FPS * 2        

    def __init__(self, x, y, width, height, attack_range):
        """
        Initialize the Plant enemy.

        Args:
            x (int): X position
            y (int): Y position
            width (int): Width of the plant
            height (int): Height of the plant
            attack_range (int): Horizontal firing range
        """
        super().__init__(x, y, width, height, "plant")
        self.sprites = load_sprite_sheet_cached("Enemies", "Plant", width, height)
        self.image = self.sprites["Idle (44x42)"][0]
        self.mask = pygame.mask.from_surface(self.image)

        # Firing logic
        self.bullet = Bullet(self.rect.x - 10, self.rect.y + 16, 16, 16)
        self.bullet_exists = False
        self.attack_range = attack_range
        self.is_firing = False
        self.fire_timer = 0

        # Animation state
        self.animation_name = "Idle (44x42)"
        self.animation_count = 0

        # Status
        self.exists = True
        self.is_hit = False
        self.hit_timer = 0

        # Direction of the plant
        self.direction = "left"

    def stop(self):
        """Completely disable the plant after destruction."""
        self.exists = False

    def attack(self):
        """
        Trigger the attack animation if the plant is still alive.
        """
        if self.exists and self.fire_timer == 0:
            self.is_firing = True
            self._start_attack_animation()
        else:
            self.is_firing = False
            self.bullet_exists = False

    def stop_attack(self):
        """
        Reset to idle animation if not hit.
        """
        if not self.is_hit:
            self.animation_name = "Idle (44x42)"
        self.is_firing = False

    def hit(self):
        """
        Mark the plant as hit and trigger hit animation.
        """
        self.animation_name = "hit"
        self.is_hit = True

    def _start_attack_animation(self):
        """
        Switch animation to attack only if not hit.
        """
        if not self.is_hit:
            self.animation_name = "Attack (44x42)"

    def update(self):
        """
        Update the plant's animation and state logic.

        Handles animation frames, bullet firing delay, hit destruction.
        """
        # Handle animation frame
        sprites = self.sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        # Update position and collision mask
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

        # Timers
        if self.fire_timer > 0:
            self.fire_timer += 1
            if self.fire_timer > self.FIRE_INTERVAL:
                self.fire_timer = 0
                self.stop_attack()

        if self.is_firing and self.fire_timer == 0:
            self.fire_timer = 1 

        if self.is_hit:
            self.hit_timer += 1
            if self.hit_timer > FPS / 2:
                self.stop()
