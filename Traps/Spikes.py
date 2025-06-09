from Utils.settings import load_sprite_sheet_cached
from Core.objects import Object
import pygame

class Spikes(Object):
    """
    Represents a spike trap that can be rotated in different directions.
    """

    def __init__(self, x, y, width, height, direction="up"):
        """
        Initialize the spike object.

        Args:
            x (int): X position.
            y (int): Y position.
            width (int): Width of the spike.
            height (int): Height of the spike.
            direction (str): Direction the spikes are facing ("up", "down", "left", "right").
        """
        super().__init__(x, y, width, height, "spikes")
        self.sprites = load_sprite_sheet_cached("Traps", "Spikes", width, height)
        self.animation_name = "Idle"
        self.animation_count = 0
        self.direction = direction
        self.set_oriented_images()
        self.mask = pygame.mask.from_surface(self.image)

    def set_oriented_images(self):
        """
        Prepare the images based on the direction of the spikes.
        """
        base_images = self.sprites[self.animation_name]
        self.oriented_images = []
        for img in base_images:
            if self.direction == "right":
                oriented_img = pygame.transform.rotate(img, 270)
            elif self.direction == "left":
                oriented_img = pygame.transform.rotate(img, 90)
            elif self.direction == "down":
                oriented_img = pygame.transform.rotate(img, 180)
            else:
                oriented_img = img  # default "up"
            self.oriented_images.append(oriented_img)
        self.image = self.oriented_images[0]
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """
        Update the spike animation frame.
        """
        sprite_index = self.animation_count % len(self.oriented_images)
        self.image = self.oriented_images[sprite_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count += 1

    def draw(self, win, offset_x=0, offset_y=0):
        """
        Draw the spike on the screen.

        Args:
            win (Surface): Pygame surface to draw on.
            offset_x (int): Horizontal camera offset.
            offset_y (int): Vertical camera offset.
        """
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))
