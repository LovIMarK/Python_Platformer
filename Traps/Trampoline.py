from Var import *
from Objects import Object

class Trampoline(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "trampoline")
        self.trampoline = load_sprite_sheets("Traps", "Trampoline", width, height)
        self.image = self.trampoline["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Idle"
        self.onTrampoline=False
        self.trampoline_count=0

    

    def loop(self):
        sprites = self.trampoline[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
        if  self.onTrampoline:
            self.trampoline_count+=1
            if self.trampoline_count > FPS/3:
                self.stopJumping()


    def Jump(self):
        self.animation_name = "Jump (28x28)"
        self.onTrampoline=True
       
            
    def stopJumping(self):
        self.animation_name = "Idle"
        self.trampoline_count=0
        self.onTrampoline=False