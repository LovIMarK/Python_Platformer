"""
Checkpoints Module

Contains all logic related to progression points: Start, Checkpoint, and End.
Each uses a specific sprite sheet and animation logic.
"""

from Utils.settings import *
from Core.objects import Object


class Start(Object):
    """Represents the starting point of a level."""

    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "start")
        self.start = load_sprite_sheet_cached("Items", os.path.join("Checkpoints", "Start"), width, height)
        self.image = self.start["Start (Idle)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Start (Idle)"

    def on(self):
        """Activate the start animation."""
        self.animation_name = "Start (Moving) (64x64)"

    def update(self):
        """Update the start animation."""
        sprites = self.start[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


class Checkpoint(Object):
    """Mid-level checkpoint that can be activated to respawn from."""

    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "checkPoint")
        self.checkpoint = load_sprite_sheet_cached("Items", os.path.join("Checkpoints", "Checkpoint"), width, height)
        self.image = self.checkpoint["Checkpoint (No Flag)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Checkpoint (No Flag)"
        self.checking = False
        self.check_count = 0

    def Check(self):
        """Trigger checkpoint activation."""
        self.checking = True

    def isCheck(self):
        """Switch to idle flag once animation has played."""
        self.animation_name = "Checkpoint (Flag Idle)(64x64)"
        self.checking = False

    def onCheck(self):
        """Handle flag animation on activation."""
        if self.checking:
            self.animation_name = "Checkpoint (Flag Out) (64x64)"
            self.check_count += 1
            if self.check_count > FPS:
                self.isCheck()

    def update(self):
        """Update the checkpoint animation."""
        sprites = self.checkpoint[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
        self.onCheck()


class End(Object):
    """End point of a level that can be activated."""

    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "end")
        self.end = load_sprite_sheet_cached("Items", os.path.join("Checkpoints", "End"), width, height)
        self.image = self.end["End (Idle)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "End (Idle)"

    def OnEnd(self):
        """Switch animation to 'pressed' when player completes level."""
        self.animation_name = "End (Pressed) (64x64)"

    def update(self):
        """Update the end point animation."""
        sprites = self.end[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
