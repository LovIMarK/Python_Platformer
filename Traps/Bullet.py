from Utils.settings import *
from Core.Objects import Object

class Bullet(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "bullet")
        self.bullet = load_sprite_sheet_cached("Enemies", "Plant", width, height)
        self.image = self.bullet["Bullet"][0]
        self.mask = pygame.mask.from_surface(self.image)


    def loop(self):
        self.rect.x-=5
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)