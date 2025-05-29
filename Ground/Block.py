from settings import *
from Objects import Object



class Block(Object):
    
    def __init__(self, x, y, sizeX,sizeY,location,name="block"):
        super().__init__(x, y, sizeX, sizeY,name)
        block = get_block(sizeX,sizeY,location)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
