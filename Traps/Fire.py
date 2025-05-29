from settings import *
from Objects import Object

class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height,fire=False):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheet_cached("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"
        self.onFire=False
        self.fire_count=0
        self.offFire=False
        self.fireOff_count=0
        self.infini=fire

    def on(self):
        self.animation_name = "on"
        self.offFire=True

    def off(self):
        self.animation_name = "off"
    
    def hit(self):
        self.animation_name = "hit"
        self.onFire=True

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
        if self.onFire:
             self.fire_count+=1
        if  self.fire_count>FPS/3:
            self.on()
            self.fire_count=0
            self.onFire=False
        if self.offFire:
            self.fireOff_count+=1
        if  self.fireOff_count>FPS*2 and not self.infini:
            self.off()
            self.fireOff_count=0
            self.offFire=False
        