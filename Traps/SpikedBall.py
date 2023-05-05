from Var import *
import numpy as np
from Objects import Object


class SpikedBall(Object):

    def __init__(self, x, y, width, height,numChains,speed,angle):
        super().__init__(x, y, width, height, "spikedBall")
        self.spikedBall = load_sprite_sheets("Traps", "Spiked Ball", width, height)
        self.image = self.spikedBall["Spiked Ball"][0]
        self.mask = pygame.mask.from_surface(self.image)
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

        posY=0

        for i in range(self.numChain):
            spikedBall=SpikedBallChain((self.rect.x)+(self.image.get_width()/2 -8),self.rect.y-16+posY,8,8)
            self.chains.append(spikedBall)
            posY-=16




    def movement(self):

            posY=0
            posX=0

            self.d2theta = -(self.g / self.L) * np.sin(self.theta)
            self.dtheta += self.d2theta * self.dt
            self.theta += self.dtheta * self.dt
            self.x = np.sin(self.theta) * self.L 
            self.y = -np.cos(self.theta) * self.L
        
            self.rect.x= self.chains[len(self.chains)-1].rect.x -21
            self.rect.y= self.chains[len(self.chains)-1].rect.y -21
            
            for chain in self.chains:

                chain.rect.x,chain.rect.y=self.convertPos(posX,posY)
                posX+=self.x 
                posY+=self.y 
               
                
                
    

    def loop(self):
       self.movement()
    
    def convertPos(self, x, y):
        xprime = x +self.posX
        yprime = -y   +self.posY
        return xprime, yprime


            


class SpikedBallChain(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "chain")
        self.chains = load_sprite_sheets("Traps", "Spiked Ball", width, height)
        self.image = self.chains["Chain"][0]
        self.mask = pygame.mask.from_surface(self.image)


 


       