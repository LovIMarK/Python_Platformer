from Utils.settings import *
from Core.objects import Object
import numpy as np


class SpikedBall(Object):
    """
    A pendulum-like spiked ball trap that swings using simulated physics.
    """

    GRAVITY = 9.8
    ROD_LENGTH = 20

    def __init__(self, x, y, width, height, num_chains, speed, angle):
        super().__init__(x, y, width, height, "spikedBall")
        self.sprites = load_sprite_sheet_cached("Traps", "Spiked Ball", width, height)
        self.image = self.sprites["Spiked Ball"][0]
        self.mask = pygame.mask.from_surface(self.image)

        self.chains = []
        self.position_origin_x = self.rect.x
        self.position_origin_y = self.rect.y
        self.num_chains = num_chains
        self.chain_speed = speed
        self.chain_angle = angle

        # Pendulum physics
        self.dt = self.chain_speed / 100
        self.theta = (self.chain_angle / 10) * np.pi
        self.angular_velocity = 0.0
        self.x = np.sin(self.theta) * self.ROD_LENGTH
        self.y = -np.cos(self.theta) * self.ROD_LENGTH

    def activate(self):
        """
        Initialize and create all the chain links.
        """
        offset_y = 0
        for _ in range(self.num_chains):
            chain = SpikedBallChain(
                self.rect.x + (self.image.get_width() / 2 - 8),
                self.rect.y - 16 + offset_y,
                8,
                8
            )
            self.chains.append(chain)
            offset_y -= 16

    def update(self):
        """
        Update the physics and position of the spiked ball and its chain.
        """
        self._apply_physics_motion()

    def _apply_physics_motion(self):
        offset_x = 0
        offset_y = 0

        angular_acceleration = -(self.GRAVITY / self.ROD_LENGTH) * np.sin(self.theta)
        self.angular_velocity += angular_acceleration * self.dt
        self.theta += self.angular_velocity * self.dt

        self.x = np.sin(self.theta) * self.ROD_LENGTH
        self.y = -np.cos(self.theta) * self.ROD_LENGTH

        if self.chains:
            self.rect.x = self.chains[-1].rect.x - 21
            self.rect.y = self.chains[-1].rect.y - 21

        for chain in self.chains:
            chain.rect.x, chain.rect.y = self._calculate_chain_position(offset_x, offset_y)
            offset_x += self.x
            offset_y += self.y

    def _calculate_chain_position(self, x, y):
        return x + self.position_origin_x, -y + self.position_origin_y


class SpikedBallChain(Object):
    """
    Chain link used by the SpikedBall trap.
    """
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "chain")
        self.sprites = load_sprite_sheets("Traps", "Spiked Ball", width, height)
        self.image = self.sprites["Chain"][0]
        self.mask = pygame.mask.from_surface(self.image)
