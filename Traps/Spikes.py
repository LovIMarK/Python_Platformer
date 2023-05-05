from Var import *
from Objects import Object


class Spikes(Object):
    

    def __init__(self, x, y, width, height,direction):
        super().__init__(x, y, width, height, "spikes")
        self.spikes = load_sprite_sheets("Traps", "Spikes", width, height)
        self.image = self.spikes["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.direction=direction

    def on(self):
        match self.direction:
            case "right":
                self.rotateRight()
            case "left":
                self.rotateLeft()
            case "down":
                self.rotateDown()

         

    def rotateRight(self):
        self.image = pygame.transform.rotate(self.image, 270)
        self.mask = pygame.mask.from_surface(self.image)

    def rotateLeft(self):
        self.image = pygame.transform.rotate(self.image, 90)
        self.mask = pygame.mask.from_surface(self.image)
    
    def rotateDown(self):
        self.image = pygame.transform.rotate(self.image, 180)
        self.mask = pygame.mask.from_surface(self.image)