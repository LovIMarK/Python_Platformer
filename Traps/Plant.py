from Utils.settings import *
from Core.Objects import Object
from Bullet import Bullet

class Plant(Object,pygame.sprite.Sprite):
    ANIMATION_DELAY = 4


    def __init__(self, x, y, width, height,dist):
        super().__init__(x, y, width, height, "plant")
        self.plant = load_sprite_sheet_cached("Enemies", "Plant", width, height)
        self.image = self.plant["Idle (44x42)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = "left"
        self.bullet=Bullet(self.rect.x-10,self.rect.y+16,16,16)
        self.animation_count = 0
        self.animation_name = "Idle (44x42)"
        self.fire=False
        self.fire_count=0
        self.bulletExist=False
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
            self.bulletExist=False

    def StopAttack(self):
        if not self.hit:
            self.animation_name = "Idle (44x42)"
        self.fire=False

    def Hit(self):
        self.animation_name = "hit"
        self.hit =True

    def Fire(self):
        if not self.hit:
            self.animation_name = "Attack (44x42)"


    def loop(self):
        sprites = self.plant[self.animation_name]
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




