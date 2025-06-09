from Utils.settings import *
from Core.objects import Object


class SpikeHead(Object):
    """
    SpikeHead trap object that moves horizontally and damages the player on collision.
    Has different animations for hits from each direction.
    """

    ANIMATION_DELAY = 7

    def __init__(self, x, y, width, height, direction=0):
        """
        Initialize the SpikeHead trap.

        Args:
            x (int): X-coordinate
            y (int): Y-coordinate
            width (int): Width of the sprite
            height (int): Height of the sprite
            direction (int): Initial direction of movement (0 = right, 1 = left)
        """
        super().__init__(x, y, width, height, "spikeHead")
        self.sprites = load_sprite_sheet_cached("Traps", "Spike Head", width, height)
        self.image = self.sprites["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)

        self.animation_count = 0
        self.animation_name = "Idle"

        self.direction = direction
        self.velocity = 5
        self.collide = False
        self.collide_count = 0

        self.exist = True  # Required for decoration cleanup logic

    def move(self):
        """
        Move the spikehead horizontally based on its current direction.
        """
        if self.direction == 0:  # Moving right
            self.rect.x += self.velocity
        elif self.direction == 1:  # Moving left
            self.rect.x -= self.velocity

    def blink(self):
        """Switch to the idle blink animation."""
        self.animation_name = "Blink (54x52)"

    def hit_bottom(self):
        """Trigger bottom collision animation."""
        self.animation_name = "Bottom Hit (54x52)"

    def hit_top(self):
        """Trigger top collision animation."""
        self.animation_name = "Top Hit (54x52)"

    def hit_right(self):
        """Trigger right collision animation."""
        self.animation_name = "Right Hit (54x52)"

    def hit_left(self):
        """Trigger left collision animation."""
        self.animation_name = "Left Hit (54x52)"

    def update(self):
        """
        Main update update: handles animation, collision effects, and movement.
        """
        sprites = self.sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        # Sync rect and mask with the current sprite
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        # Reset animation cycle
        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

        # Handle post-collision animation timing
        if self.collide:
            self.collide_count += 1
            if self.collide_count > FPS // 5:
                self.collide_count = 0
                self.collide = False
                self.blink()

        # Perform movement
        self.move()
