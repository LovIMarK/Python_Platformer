from Var import *
from Objects import Object

class Cube(Object):
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "cube")
        self.platforms = load_sprite_sheets("Traps", "Blocks", width, height)
        self.image = self.platforms["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Idle"
        self.hit=False
        self.hit_count=0
        self.invisible=False
        self.invisible_count=0


    def Invisible(self):
        self.animation_name = "Invisible (22x22)"
        self.hit=False
        self.hit_count=0

    def HitTop(self):
        self.animation_name = "HitTop (22x22)"
        self.hit=True
        self.invisible=True

    def HitSide(self):
        self.animation_name = "HitSide (22x22)"

    def Visible(self):
        self.animation_name = "Idle"
        self.invisible=False
        self.invisible_count=0
    
    def Hit1(self):
        self.animation_name = "Part 1 (22x22)"
        self.hit1=True
        self.hit=False
        self.hit_count=0
        self.rect.y+=20

    def Hit2(self):
        self.animation_name = "Part 2 (22x22)"
        self.rect.y-=20    


    def loop(self):
        sprites = self.platforms[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if  self.hit:
            self.hit_count+=1
            if self.hit_count>FPS/4:
                self.Invisible()
        if  self.invisible:
            self.invisible_count+=1
            if self.invisible_count>FPS*2:
                self.Visible()
            
        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0