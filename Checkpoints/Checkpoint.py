from Var import *
from Objects import Object

class Checkpoint(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "checkPoint")
        self.checkpoint = load_sprite_sheets("Items", "Checkpoints\Checkpoint", width, height)
        self.image = self.checkpoint["Checkpoint (No Flag)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Checkpoint (No Flag)"
        self.CheckPoint=False
        self.CheckPoint_count=0

    def onCheck(self):
        if  self.CheckPoint:
            self.animation_name = "Checkpoint (Flag Out) (64x64)"
            self.CheckPoint_count+=1
            if self.CheckPoint_count > FPS:
                self.CheckPoint=True
                self.isCheck()
    def Check(self):
        self.CheckPoint=True

    def isCheck(self):
        self.animation_name = "Checkpoint (Flag Idle)(64x64)"
        self.CheckPoint=False
        

    def loop(self):
        sprites = self.checkpoint[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
        self.onCheck()