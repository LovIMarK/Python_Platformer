from settings import *
from Objects import Object
from Ground.Particules import Particules

class FallingPlatform(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fallingPlatforms")
        self.fallingPlatforms = load_sprite_sheet_cached("Traps", "Falling Platforms", width, height)
        self.image = self.fallingPlatforms["Off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "On (32x10)"
        self.touching = False
        self.touching_count = 0
        self.startY = self.rect.y
        self.startX = self.rect.x
        self.particuleExist = False
        self.particule = [Particules(self.rect.x + 16*i, self.rect.y + 16, 16, 16) for i in range(2)]

    def onFalling(self):
        self.touching = True

    def Falling(self):
        if self.touching:
            self.animation_name = "On (32x10)"
            self.touching_count += 1
            if self.touching_count > FPS / 10:
                self.rect.y += 10
            if self.touching_count > FPS * 3:
                self.touching = False
                self.rect.y = self.startY
                self.touching_count = 0
                self.animation_name = "Off"

    def on(self):
        self.animation_name = "On (32x10)"

    def off(self):
        self.animation_name = "Off"

    def loop(self):
        sprites = self.fallingPlatforms[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        for obj in self.particule:
            obj.loop()
            obj.rect.y += 4
            if obj.rect.y > self.startY + 100:
                obj.rect.y = self.startY + 16
            if self.touching:
                obj.image.set_alpha(0)
            elif obj.image.get_alpha() == 0:
                obj.image.set_alpha(170)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
        self.Falling()
