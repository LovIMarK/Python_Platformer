from Var import *
from Objects import Object

class Particules(Object):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "particules")
        self.end = load_sprite_sheets("Other","", width, height)
        self.image = self.end["Dust Particle"][0]
        self.image.set_alpha(170)
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "End (Idle)"



            

    