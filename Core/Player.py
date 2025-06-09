"""
Player Module

Defines the main player class for movement, animation, and interactions.
Uses a sprite sheet with multiple states (run, jump, fall, hit, etc.).
"""

from Utils.settings import *


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 2
    ANIMATION_DELAY = 1
    LIFE = 3

    SPRITES = load_sprite_sheet_cached("MainCharacters", "VirtualGuy", 32, 32, flip=True)

    def __init__(self, x: int, y: int, width: int, height: int):
        """
        Initialize the player.

        Args:
            x (int): X coordinate.
            y (int): Y coordinate.
            width (int): Width of the player.
            height (int): Height of the player.
        """
        super().__init__()

        self.rect = pygame.Rect(x, y, width, height)
        self.mask = None

        # Movement & State
        self.x_vel = 0
        self.y_vel = 0
        self.direction = "left"
        self.jump = False
        self.slide = False
        self.fall_count = 0
        self.jump_count = 0
        self.animation_count = 0

        # Hit / Death / Respawn
        self.hit = False
        self.hit_count = 0
        self.lives = self.LIFE
        self.death = 0
        self.checkPointX = 0
        self.checkPointY = 500

        # Fan interaction
        self.onfan = False
        self.onfan_count = 0

        # Wall Slide
        self.slidePlatRight = False
        self.slidePlatLeft = False

        # Slash attack
        self.slash = False
        self.slash_count = 0

        # Game progression
        self.levels = 1
        self.unlockLevel = 1
        self.onChrono = True
        self.score = 0

        # New: stunned state when hit
        self.stunned = False

    def make_hit(self):
        """
        Trigger the hit state:
        - Prevents input while stunned
        - Applies knockback (jump back)
        """
        if not self.hit:
            self.hit = True
            self.stunned = True
            self.hit_count = 0

            # Knockback direction: inverse to current facing direction
            knockback_strength = 10
            upward_force = -8

            if self.direction == "right":
                self.x_vel = -knockback_strength
            else:
                self.x_vel = knockback_strength

            self.y_vel = upward_force  # Slight upward bounce

    def Jump(self, jump_strength=None):
        """
        Make the player jump.

        Args:
            jump_strength (int, optional): The strength multiplier for the jump.
        """
        if self.stunned:
            return  # Block jump during hit animation

        if jump_strength is None:
            jump_strength = 5

        self.jump = True
        if self.slide:
            self.x_vel = 20 if self.direction == "left" else -20

        self.slide = False
        self.onfan = False
        self.onfan_count = 0

        self.y_vel = -self.GRAVITY * jump_strength
        self.jump_count += 1
        self.animation_count = 0

        if self.jump_count == 1:
            self.fall_count = 0

    def Slide(self):
        """Initiate wall-slide (ignored if stunned)."""
        if self.stunned:
            return
        self.slide = True
        if self.jump:
            self.jump_count = 0
            self.y_vel = 2
        self.jump = False

    def StopSlide(self):
        """Stop wall-slide state."""
        self.slide = False

    def Slash(self):
        """Trigger slash animation (ignored if stunned)."""
        if not self.stunned:
            self.slash = True

    def onFan(self):
        """Player is affected by a fan."""
        self.onfan = True

    def make_slidePlat_right(self):
        if not self.stunned:
            self.slidePlatRight = True

    def make_slidePlat_left(self):
        if not self.stunned:
            self.slidePlatLeft = True

    def make_slidePlat_stop(self):
        self.slidePlatRight = False
        self.slidePlatLeft = False

    def move_left(self, vel: int):
        if self.stunned:
            return
        self.x_vel = -vel
        self.make_slidePlat_stop()
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel: int):
        if self.stunned:
            return
        self.x_vel = vel
        self.make_slidePlat_stop()
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def move(self, dx: int, dy: int):
        """Move the player directly (used internally)."""
        self.rect.x += dx
        self.rect.y += dy

    def update(self, fps: int):
        """
        Main update function called every frame.
        Handles physics, animations, hit logic, and movements.
        """
        if not self.onfan and not self.slide:
            self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY * 2)
        elif self.slide:
            self.y_vel += min(1, (self.fall_count / (fps * 100)) * self.GRAVITY * 2)
        elif self.onfan:
            self.onfan_count += 1
            if self.onfan_count < FPS:
                self.rect.y -= 5

        if self.slidePlatRight:
            self.x_vel = PLAYER_VEL
        if self.slidePlatLeft:
            self.x_vel = -PLAYER_VEL

        # Respawn
        if self.lives <= 0:
            self.rect.x = self.checkPointX
            self.rect.y = self.checkPointY
            self.lives = self.LIFE

        # Death by falling
        if self.rect.y > HEIGHT or self.rect.y < HEIGHT - 96 * 11:
            self.lives = 0

        # Handle hit delay
        if self.hit:
            self.hit_count += 1
            if self.hit_count > fps // 3:
                self.lives -= 1
                self.hit = False
                self.hit_count = 0
                self.stunned = False  # Re-enable movement

        # Slash timer
        if self.slash:
            self.slash_count += 1
        if self.slash_count > fps / 10:
            self.slash_count = 0
            self.slash = False

        self.move(self.x_vel, self.y_vel)
        self.fall_count += 1
        self.update_sprite()

    def landed(self):
        """Reset jumping when landing."""
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        """Invert Y velocity on ceiling hit."""
        self.fall_count = 0
        self.y_vel *= -1

    def update_sprite(self):
        """Switch sprite animation according to state."""
        sprite_sheet = "idle"

        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0:
            sprite_sheet = "jump" if self.jump_count == 1 else "double_jump"
        elif self.y_vel > self.GRAVITY * 2 and not self.slide:
            sprite_sheet = "fall"
            self.make_slidePlat_stop()
        elif self.slide:
            sprite_sheet = "wall_jump"
        elif self.slash and not self.slide:
            sprite_sheet = "slash"
        elif self.x_vel != 0:
            sprite_sheet = "run"

        sprite_sheet_name = f"{sprite_sheet}_{self.direction}"
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update_sprite_hitbox()

    def update_sprite_hitbox(self):
        """Update the hitbox and mask to match current sprite."""
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win: pygame.Surface, offset_x: int, offset_y: int):
        """Draw the player on screen."""
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y - offset_y))
