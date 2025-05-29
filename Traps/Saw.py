from settings import *
import numpy as np
from Objects import Object


class Saw(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height,numChains,speed,angle):
        super().__init__(x, y, width, height, "saw")
        self.saw = load_sprite_sheet_cached("Traps", "Saw", width, height)
        self.image = self.saw["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"
        self.chainExist=False
        self.chains=[]
        self.is_moving = False
        self.posX=self.rect.x
        self.posY=self.rect.y
        self.numChain=numChains
        self.chainSpeed=speed
        self.chainAngle=angle


        self.t = 0  # temps (s)
        self.dt = self.chainSpeed/100  # intervalle de temps très petit (s)
        self.g = 9.8 # accélération gravitationnelle (m/s^2)
        self.theta = (self.chainAngle/10)* np.pi  # angle initial
        self.dtheta = 0.0  # vitesse angulaire ,le pend.ule est au repos
        self.L = 20  # longueur de la tige  (m)
        self.x = np.sin(self.theta) * self.L 
        self.y = -np.cos(self.theta) * self.L  

    def on(self):
        self.animation_name = "on"
        posY=0

        for i in range(self.numChain):
            saw=SawChain((self.rect.x)+(self.image.get_width()/2 -8),self.rect.y-16+posY,8,8)
            self.chains.append(saw)
            posY-=16


    

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.saw[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
        self.movement()



    def movement(self):

            posY=0
            posX=0

            self.d2theta = -(self.g / self.L) * np.sin(self.theta)
            self.dtheta += self.d2theta * self.dt
            self.theta += self.dtheta * self.dt
            self.x = np.sin(self.theta) * self.L 
            self.y = -np.cos(self.theta) * self.L
        
            self.rect.x= self.chains[len(self.chains)-1].rect.x -30
            self.rect.y= self.chains[len(self.chains)-1].rect.y -30
            
            for chain in self.chains:

                chain.rect.x,chain.rect.y=self.convertPos(posX,posY)
                posX+=self.x 
                posY+=self.y 
               
                
                
    

      
    
    def convertPos(self, x, y):
        xprime = x +self.posX
        yprime = -y   +self.posY
        return xprime, yprime


            


class SawChain(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "chain")
        self.chains = load_sprite_sheets("Traps", "Saw", width, height)
        self.image = self.chains["Chain"][0]
        self.mask = pygame.mask.from_surface(self.image)


 


       