from settings import *
from Objects import Object

class PlatformsGrey(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height,direction):
        super().__init__(x, y, width, height, "platformsGrey")
        self.platforms = load_sprite_sheet_cached("Traps", "Platforms", width, height)
        self.image = self.platforms["Grey Off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.direction=direction
        self.animation_count = 0
        self.animation_name = "Grey On (32x8)"
        self.direction=direction

    def on(self):
        self.animation_name = "Grey On (32x8)"


    def off(self):
        self.animation_name = "Grey Off"

    def loop(self):
        sprites = self.platforms[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        if self.direction=="left":
            self.image = pygame.transform.flip(self.image,True,False)
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0