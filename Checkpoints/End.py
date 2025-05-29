from Utils.settings import *
from Core.Objects import Object


class End(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "end")
        self.end = load_sprite_sheet_cached("Items", os.path.join("Checkpoints", "End"), width, height)
        self.image = self.end["End (Idle)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "End (Idle)"


    def OnEnd(self):
        self.animation_name = "End (Pressed) (64x64)"
            
    
        

    def loop(self):
        sprites = self.end[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0