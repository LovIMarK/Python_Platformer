from Var import *
from Objects import Object

class Dar(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "dar")
        self.dar = load_sprite_sheets("Enemies", "Bee", width, height)
        self.image = self.dar["Bullet"][0]
        self.mask = pygame.mask.from_surface(self.image)


    def loop(self):
        self.rect.y+=5
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)