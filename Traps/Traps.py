from Var import *
from Objects import Object

class Spikes(Object):
    

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "spikes")
        self.spikes = load_sprite_sheets("Traps", "Spikes", width, height)
        self.image = self.spikes["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.mask = pygame.mask.from_surface(self.image)