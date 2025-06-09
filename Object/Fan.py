from Utils.settings import *
from Core.objects import Object
from Ground.particles import Particles

class Fan(Object):
    """
    Fan object that emits upward particles and pushes the player when active.
    """

    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        """
        Initialize the fan with animation frames and particle stream.

        Args:
            x (int): X position of the fan.
            y (int): Y position of the fan.
            width (int): Width of the fan.
            height (int): Height of the fan.
        """
        super().__init__(x, y, width, height, "fan")
        self.sprites = load_sprite_sheet_cached("Traps", "Fan", width, height)
        self.image = self.sprites["Off"][0]
        self.mask = pygame.mask.from_surface(self.image)

        self.animation_name = "On (24x8)"
        self.animation_count = 0

        self.particleExist = False
        self.particles_visible = True

        # Create a grid of upward particles
        self.particles = []
        cols = 3
        rows = 3
        x_spacing = self.rect.width / cols
        y_spacing = 20  # Vertical spacing between particles

        for row in range(rows):
            for col in range(cols):
                x_pos = self.rect.x + col * x_spacing + (x_spacing - 16) / 2
                y_pos = self.rect.y - row * y_spacing
                self.particles.append(
                    Particles(x_pos, y_pos, 16, 16, dy=-2)
                )

    def update_particles_visibility(self, visible: bool):
        """
        Show or hide the fan's particles visually and logically.

        Args:
            visible (bool): Whether particles should be visible and animated.
        """
        self.particles_visible = visible
        alpha = 170 if visible else 0
        for p in self.particles:
            p.image.set_alpha(alpha)

    def update(self):
        """
        Update fan animation and optionally particles if active.
        """
        self.animation_name = "On (24x8)" 

         
        # Choose animation based on state
        sprites = self.sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

        # Animate particles only if active
        for p in self.particles:
            p.update()

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
