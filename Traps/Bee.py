from Utils.settings import *
from Core.Objects import Object
from Dar import Dar

class Bee(Object,pygame.sprite.Sprite):
    ANIMATION_DELAY = 4


    def __init__(self, x, y, width, height,dist):
        super().__init__(x, y, width, height, "bee")
        self.bee = load_sprite_sheet_cached("Enemies", "Bee", width, height)
        self.image = self.bee["Idle (36x34)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        #self.direction = "left"
        self.dar=Dar(self.rect.x+20,self.rect.y+34,16,16)
        self.animation_count = 0
        self.animation_name = "Idle (36x34)"
        self.fire=False
        self.fire_count=0
        self.darExist=False
        self.exist=True
        self.hit=False
        self.hit_count=0
        self.dist=dist
        #self.direction=direction


    def Stop(self):
        self.exist=False





    def Attack(self):
       
        if self.exist:
            self.fire=True
            self.Fire()
        else:
            self.fire=False
            self.darExist=False

    def StopAttack(self):
        if not self.hit:
            self.animation_name = "Idle (36x34)"
        self.fire=False

    def Hit(self):
        self.animation_name = "Hit (36x34)"
        self.hit =True

    def Fire(self):
        if not self.hit:
            self.animation_name = "Attack (36x34)"


    def loop(self):
        sprites = self.bee[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
        if self.fire:
            self.fire_count+=1
        if self.hit:
            self.hit_count+=1
        if self.hit_count>FPS/2:
            self.Stop()
        if  self.fire_count>FPS/2:
            self.fire_count=0
            self.StopAttack()