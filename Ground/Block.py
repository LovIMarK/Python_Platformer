from Utils.settings import *
from Core.objects import Object


class Block(Object):
    
    def __init__(self, x, y, sizeX, sizeY, location, name="block"):
        super().__init__(x, y, sizeX, sizeY, name)
        block = get_terrain_block(sizeX, sizeY, location)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """
        Placeholder update method to avoid AttributeError during game update.
        This block is static and does not require updates per frame.
        """
        pass
