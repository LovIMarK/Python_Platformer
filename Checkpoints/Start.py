from settings import *
from Objects import Object

class Start(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "start")
        self.start = load_sprite_sheet_cached("Items", os.path.join("Checkpoints", "Start"), width, height)
        self.image = self.start["Start (Idle)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Start (Idle)"


    def on(self):
        self.animation_name = "Start (Moving) (64x64)"
            
    
        

    def loop(self):
        sprites = self.start[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0