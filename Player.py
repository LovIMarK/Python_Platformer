from Var import *




class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "NinjaFrog", 32, 32, True)
    ANIMATION_DELAY = 3
    LIFE=1

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.lives=self.LIFE
        self.death=0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.jump=False
        self.hit = False
        self.hit_count = 0
        self.slidePlat=False
        self.checkPointX=0
        self.checkPointY=500
        self.onfan=False
        self.onfan_count=0
        self.slide=False
        self.onChrono=True
        self.slash=False
        self.slash_count=False
        self.levels=3
        self.unlockLevel=3


    def Slide(self):
        self.slide=True
        if self.jump:
            self.jump_count = 0
            self.y_vel=2
        self.jump=False


    def StopSlide(self):
        self.slide=False

    def Slash(self):
        self.slash=True


    def Jump(self):
        self.jump=True
        if self.jump and  self.slide and self.direction=="left":
            self.x_vel = 20
        elif self.jump and  self.slide and self.direction=="right":
            self.x_vel = -20


        self.slidePlat=False
        self.onfan=False
        self.onfan_count=0
        self.y_vel = -self.GRAVITY * 8
        self.slide=False
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def onFan(self):
        self.onfan=True

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def make_hit(self):
        self.hit = True




    def make_slidePlat(self):
        self.slidePlat=True




    def move_left(self, vel):
        self.x_vel = -vel
        self.slidePlat=False
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        self.slidePlat=False
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        if  not self.onfan and not self.slide:
            self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        elif self.slide:
            self.y_vel += min(1, (self.fall_count / (fps*100)) * self.GRAVITY)
        elif self.onfan:
            self.onfan_count+=1
            if self.onfan_count<FPS:
                self.rect.y-=5

        if self.lives<=0:
            self.rect.x=self.checkPointX
            self.rect.y=self.checkPointY
            self.lives=self.LIFE



        # if self.rect.y>HEIGHT or self.rect.y<HEIGHT - 96 * 11:
        #     self.lives=0

        if self.hit:
            self.hit_count += 1
            if self.lives==1:
                self.lives-=1
                self.hit = False
                self.hit_count = 0


        if self.hit_count > fps * 2:
            if self.hit:
                self.lives-=1
            self.hit = False
            self.hit_count = 0
        if self.slash:
            self.slash_count+=1
        if self.slash_count>fps/10:
            self.slash_count=0
            self.slash=False

        if self.slidePlat:
            self.x_vel = 2

        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1
        self.update_sprite()


    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"

        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2 :
                sprite_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 2 and not self.slide:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"
        elif self.slide:
            sprite_sheet="wall_jump"
        if self.slash and not self.slide:
            sprite_sheet="slash"


        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x,offset_y):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y-offset_y))