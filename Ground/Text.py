from Utils.settings import *
from Core.Objects import Object

class Text(Object):

    def __init__(self, x, y, size,location,color="black"):
        super().__init__(x, y, size, size,"text")
        text = get_text(size,location,color)
        self.image.blit(text, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
