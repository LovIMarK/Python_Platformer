from settings import *
from Objects import Object
from Ground.Particules import Particules

class Fan(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fan")
        self.fan = load_sprite_sheet_cached("Traps", "Fan", width, height)
        self.image = self.fan["Off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Off"
        self.fan_count = 0
        self.particuleExist = False
        self.particule = [Particules(self.rect.x, self.rect.y - 16 - 40 * i, 16, 16) for i in range(4)]

    def onFan(self):
        self.fan_count += 1

    def on(self):
        self.animation_name = "On (24x8)"

    def off(self):
        self.animation_name = "Off"

    def loop(self):
        self.animation_name = "On (24x8)"

        sprites = self.fan[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        for obj in self.particule:
            obj.loop()
            obj.rect.y -= 4
            if obj.rect.y < self.rect.y - 300:
                obj.rect.y = self.rect.y - 16

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
