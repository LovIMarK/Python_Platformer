import pygame
from Utils.settings import FPS, load_sprite_sheet_cached
from Core.objects import Object

class Cube(Object):
    """Represents an interactive cube platform with animations."""

    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height):
        """
        Initialize a Cube object.

        Args:
            x (int): X position.
            y (int): Y position.
            width (int): Width of the cube.
            height (int): Height of the cube.
        """
        super().__init__(x, y, width, height, "cube")
        self.platform_sprites = load_sprite_sheet_cached("Traps", "Blocks", width, height)
        self.image = self.platform_sprites["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)

        self.animation_frame = 0
        self.current_animation = "Idle"
        
        self.is_hit = False
        self.hit_timer = 0
        self.is_invisible = False
        self.invisible_timer = 0

    def set_invisible(self):
        """Set cube to invisible state."""
        self.current_animation = "Invisible (22x22)"
        self.is_hit = False
        self.hit_timer = 0

    def hit_top(self):
        """Handle cube top collision."""
        self.current_animation = "HitTop (22x22)"
        self.is_hit = True
        self.is_invisible = True
        self.hit_timer = 0

    def hit_side(self):
        """Handle cube side collision."""
        self.current_animation = "HitSide (22x22)"

    def set_visible(self):
        """Set cube back to visible (idle) state."""
        self.current_animation = "Idle"
        self.is_invisible = False
        self.invisible_timer = 0

    def break_part_1(self):
        """First stage of cube break animation."""
        self.current_animation = "Part 1 (22x22)"
        self.is_hit = False
        self.hit_timer = 0
        self.rect.y += 20

    def break_part_2(self):
        """Second stage of cube break animation."""
        self.current_animation = "Part 2 (22x22)"
        self.rect.y -= 20

    def update(self):
        """Update cube's animation and state every frame."""
        sprites = self.platform_sprites[self.current_animation]
        sprite_index = (self.animation_frame // self.ANIMATION_DELAY) % len(sprites)

        self.image = sprites[sprite_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

        self.animation_frame += 1

        # Handle hit state duration
        if self.is_hit:
            self.hit_timer += 1
            if self.hit_timer > FPS / 4:
                self.set_invisible()

        # Handle invisibility duration
        if self.is_invisible:
            self.invisible_timer += 1
            if self.invisible_timer > FPS * 2:
                self.set_visible()

        # Reset animation frame if cycle complete
        if self.animation_frame // self.ANIMATION_DELAY >= len(sprites):
            self.animation_frame = 0
