from Utils.settings import *
from Core.Objects import Object

class Fruit(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height,kind):
        super().__init__(x, y, width, height, "fruit")
        self.fruit = load_sprite_sheet_cached("Items", "Fruits", width, height)
        self.image = self.fruit["Apple"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = kind
        self.collected=False
        self.collected_count=0
        self.exist=True


    def Collected(self):
        self.animation_name = "Collected"
        self.collected=True
            
    
        

    def loop(self):
        sprites = self.fruit[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
        if  self.collected:
            self.collected_count+=1
        if  self.collected_count>FPS/3.2:
            self.exist=False