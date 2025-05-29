from Utils.settings import *
from Core.Objects import Object

class Spikes(Object):
    def __init__(self, x, y, width, height, direction="up"):
        super().__init__(x, y, width, height, "spikes")
        self.sprites = load_sprite_sheet_cached("Traps", "Spikes", width, height)
        self.animation_name = "Idle"
        self.animation_count = 0
        self.direction = direction
        self.set_oriented_images()
        self.mask = pygame.mask.from_surface(self.image)

    def set_oriented_images(self):
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
                oriented_img = img
            self.oriented_images.append(oriented_img)
        self.image = self.oriented_images[0]
        self.mask = pygame.mask.from_surface(self.image)

    def loop(self):
        sprite_index = (self.animation_count) % len(self.oriented_images)
        self.image = self.oriented_images[sprite_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count += 1

    def draw(self, win, offset_x=0, offset_y=0):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))
