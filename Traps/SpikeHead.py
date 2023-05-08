from Var import *
from Objects import Object


class SpikeHead(Object):
    ANIMATION_DELAY = 10

    def __init__(self, x, y, width, height,direction=0):
        super().__init__(x, y, width, height, "spikeHead")
        self.platforms = load_sprite_sheets("Traps", "Spike Head", width, height)
        self.image = self.platforms["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Idle"
        self.collide=False
        self.collide_count=0
        self.direction=direction
        self.velo=5

    

    def movement(self):
        if self.direction==0:
            self.rect.x+=self.velo        
        elif self.direction==1:
            self.rect.x-=self.velo  

        # if self.direction==0:
        #     self.rect.y-=1        
        # elif self.direction==1:
        #     self.rect.x+=1  
        # elif self.direction==2:
        #     self.rect.y+=1
        # elif self.direction==3:
        #     self.rect.x-=1     

    def Blink(self):
        self.animation_name = "Blink (54x52)"

    def Bottom(self):
        self.animation_name = "Bottom Hit (54x52)"
    def Top(self):
        self.animation_name = "Top Hit (54x52)"
    def Right(self):
        self.animation_name = "Right Hit (54x52)"
    def Left(self):
        self.animation_name = "Left Hit (54x52)"

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
        if self.collide:
            self.collide_count+=1
            if self.collide_count>FPS/5:
                self.collide_count=0
                self.collide=False
                self.Blink()
        self.movement()



