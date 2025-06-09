from Utils.settings import *
from Core.objects import Object
from Ground.particles import Particles

class FallingPlatform(Object):
    """
    A platform that temporarily falls when touched by the player.
    Emits downward particles for a floating effect.
    """

    ANIMATION_DELAY = 3
    FALL_DELAY = FPS / 10        
    RESET_DELAY = FPS * 3       
    FALL_SPEED = 10

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fallingPlatforms")
        self.sprites = load_sprite_sheet_cached("Traps", "Falling Platforms", width, height)
        self.image = self.sprites["Off"][0]
        self.mask = pygame.mask.from_surface(self.image)

        self.animation_name = "On (32x10)"
        self.animation_count = 0

        # State
        self.touching = False
        self.touching_timer = 0
        self.startX = x
        self.startY = y

        self.particles_visible = True
        self.particleExist = False
        self.particle_count = 5

        self.generate_particles()

    def generate_particles(self):
        """
        Create a new set of downward particles.
        """
        spacing = self.rect.width / self.particle_count
        x_start = self.rect.x + (spacing - 16) / 2
        self.particles = [
            Particles(x_start + i * spacing, self.rect.bottom + 8, 16, 16, dy=2)
            for i in range(self.particle_count)
        ]

    def onFalling(self):
        """
        Start the falling countdown when touched by the player.
        """
        if not self.touching:
            self.touching = True
            self.touching_timer = 0
            self.animation_name = "Off"

    def update(self):
        """
        Handle animation, falling logic and particle updates.
        """
        # Animate sprite
        sprites = self.sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

        # Particle animation (only if visible and not yet falling)
        if self.particles_visible:
            for p in self.particles:
                p.update()

        # Falling logic
        if self.touching:
            self.touching_timer += 1

            if self.touching_timer > self.FALL_DELAY:
                self.rect.y += self.FALL_SPEED
                self.particles_visible = False  # stop drawing and updating particles

            if self.touching_timer > self.RESET_DELAY:
                self.touching = False
                self.touching_timer = 0
                self.rect.y = self.startY
                self.animation_name = "On (32x10)"
                self.particles_visible = True
                self.generate_particles()

        # Update position and collision mask
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, window, offset_x, offset_y):
        """
        Draw the platform and its particles if visible.

        Args:
            window (Surface): The Pygame window surface.
            offset_x (int): Horizontal camera offset.
            offset_y (int): Vertical camera offset.
        """
        window.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))
        if self.particles_visible:
            for p in self.particles:
                p.draw(window, offset_x, offset_y)
