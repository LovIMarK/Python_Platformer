from Utils.settings import *
from Core.Objects import Object

class PlatformsBrown(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "platformsBrown")
        self.platforms = load_sprite_sheet_cached("Traps", "Platforms", width, height)
        self.image = self.platforms["Brown Off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Brown Off"

    def on(self):
        self.animation_name = "Brown On (32x8)"

    def off(self):
        self.animation_name = "Brown Off"

    def loop(self):
        sprites = self.platforms[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0