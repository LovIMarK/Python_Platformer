from Utils.settings import *
from Core.objects import Object
import numpy as np


class Saw(Object):
    """
    A swinging saw trap that follows pendulum-like physics.
    """

    ANIMATION_DELAY = 3
    G = 9.8       # Gravity constant
    L = 20        # Pendulum length

    def __init__(self, x, y, width, height, num_chains, speed, angle):
        super().__init__(x, y, width, height, "saw")
        self.saw_sprites = load_sprite_sheet_cached("Traps", "Saw", width, height)
        self.image = self.saw_sprites["off"][0]
        self.mask = pygame.mask.from_surface(self.image)

        self.animation_name = "off"
        self.animation_count = 0

        self.chain_initialized = False
        self.chains = []

        self.pos_x = self.rect.x
        self.pos_y = self.rect.y
        self.num_chains = num_chains
        self.chain_speed = speed
        self.chain_angle = angle

        self.dt = self.chain_speed / 100
        self.theta = (self.chain_angle / 10) * np.pi
        self.dtheta = 0.0
        self.x = np.sin(self.theta) * self.L
        self.y = -np.cos(self.theta) * self.L

    def turn_on(self):
        """
        Activate the saw and generate its chain segments.
        """
        self.animation_name = "on"
        offset_y = 0
        for _ in range(self.num_chains):
            chain = SawChain(
                self.rect.x + (self.image.get_width() / 2 - 8),
                self.rect.y - 16 + offset_y,
                8, 8
            )
            self.chains.append(chain)
            offset_y -= 16

    def turn_off(self):
        """
        Deactivate the saw animation.
        """
        self.animation_name = "off"

    def update(self):
        """
        Update saw animation and simulate swinging motion.
        """
        sprites = self.saw_sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

        self._apply_physics_motion()

    def _apply_physics_motion(self):
        """
        Apply pendulum physics to determine the saw's position.
        """
        offset_x = 0
        offset_y = 0

        d2theta = -(self.G / self.L) * np.sin(self.theta)
        self.dtheta += d2theta * self.dt
        self.theta += self.dtheta * self.dt

        self.x = np.sin(self.theta) * self.L
        self.y = -np.cos(self.theta) * self.L

        if self.chains:
            self.rect.x = self.chains[-1].rect.x - 30
            self.rect.y = self.chains[-1].rect.y - 30

        for chain in self.chains:
            chain.rect.x, chain.rect.y = self._calculate_chain_position(offset_x, offset_y)
            offset_x += self.x
            offset_y += self.y

    def _calculate_chain_position(self, x, y):
        """
        Convert relative position to screen coordinates.
        """
        return x + self.pos_x, -y + self.pos_y


class SawChain(Object):
    """
    Visual chain element attached to a swinging saw.
    """
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "chain")
        self.chain_sprites = load_sprite_sheets("Traps", "Saw", width, height)
        self.image = self.chain_sprites["Chain"][0]
        self.mask = pygame.mask.from_surface(self.image)
