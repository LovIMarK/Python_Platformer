from Var import *
from Objects import Object



class Block(Object):
    
    def __init__(self, x, y, size,location):
        super().__init__(x, y, size, size,"block")
        block = get_block(size,location)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
