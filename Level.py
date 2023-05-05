
from Var import *
from Import import *


class Level():

    def __init__(self,level,block_size):
        self.level=level
        self.block_size=block_size
        
    
    def showLevel(self):
        match self.level:
            case 1:
                return self.Level1(self.block_size)
            case 2:
                return self.Level2(self.block_size)
            case 3:
                return self.Level3(self.block_size)
            case 4:
                return self.Level4(self.block_size)
            case 5:
                return self.Level5(self.block_size)
            case 6:
                return self.Level6(self.block_size)
            case 7:
                return self.Level7(self.block_size)
            case 8:
                return self.Level8(self.block_size)
            case 9:
                return self.Level9(self.block_size)
            case 10:
                return self.Level10(self.block_size)
            case 11:
                return self.Level11(self.block_size)
            case 12:
                return self.Level12(self.block_size)
            case 13:
                return self.Level13(self.block_size)
            case 14:
                return self.Level14(self.block_size)
            case 15:
                return self.Level15(self.block_size)
            case 16:
                return self.Level16(self.block_size)
            case 17:
                return self.Level17(self.block_size)
            case 18:
                return self.Level18(self.block_size)
            case 19:
                return self.Level19(self.block_size)
            case 20:
                return self.Level20(self.block_size)
            case 21:
                return self.Level21(self.block_size)
            case 22:
                return self.Level22(self.block_size)
            case 23:
                return self.Level23(self.block_size)
            case 24:
                return self.Level24(self.block_size)
            case 25:
                return self.Level25(self.block_size)
            case 26:
                return self.Level26(self.block_size)
            case 27:
                return self.Level27(self.block_size)
            case 28:
                return self.Level28(self.block_size)
            case 29:
                return self.Level29(self.block_size)
            case 30:
                return self.Level30(self.block_size)
            case 31:
                return self.Level31(self.block_size)
            case 32:
                return self.Level32(self.block_size)
            case 33:
                return self.Level33(self.block_size)
            case 34:
                return self.Level34(self.block_size)
            case 35:
                return self.Level35(self.block_size)
            case 36:
                return self.Level36(self.block_size)
            case 37:
                return self.Level37(self.block_size)
            case 38:
                return self.Level38(self.block_size)
            case 39:
                return self.Level39(self.block_size)
            case 40:
                return self.Level40(self.block_size)
            case 41:
                return self.Level41(self.block_size)
            case 42:
                return self.Level42(self.block_size)
            case 43:
                return self.Level43(self.block_size)
            case 44:
                return self.Level44(self.block_size)
            case 45:
                return self.Level45(self.block_size)
            case 46:
                return self.Level46(self.block_size)
            case 47:
                return self.Level47(self.block_size)
            case 48:
                return self.Level48(self.block_size)
            case 49:
                return self.Level49(self.block_size)
            case 50:
                return self.Level50(self.block_size)


    def Level1(self,block_size):


        checkPoint=Checkpoint(block_size * 19, HEIGHT - block_size *2-32,64,64)
        start=Start(0-24,HEIGHT - block_size *3-32,64,64)
        end = End(block_size * 34,HEIGHT - block_size*2-32,64,64)
        #end = End(block_size * 3,HEIGHT - block_size*2-32,64,64)

        
        
        plants=[
            Plant(block_size * 24,HEIGHT - block_size *6+20,44,42),
           # Plant(block_size * 26,HEIGHT - block_size *2+20,44,42)
        ]

        trampoline=Trampoline(0,0, 28, 28)
        trampolines=[
            Trampoline(block_size *8-(block_size/2)-2 , HEIGHT - block_size  * 5, 28, 28)
        ]

        fans=[
                Fan(150, HEIGHT - block_size-12, 24, 20)
            ]
        


        spikes=[
            Spikes(block_size * 10, HEIGHT - block_size* 5-32, 16, 20,"up"),
            Spikes(block_size * 10-32, HEIGHT - block_size* 5+32, 16, 20,"left"),
            Spikes(block_size * 10-32, HEIGHT - block_size* 5, 16, 20,"left"),
            Spikes(block_size * 10+16, HEIGHT - block_size* 5-32, 16, 20,"up"),
            #spike 2 wall jump
            Spikes(block_size*26, HEIGHT - block_size * 1-32, 16, 20,"up"),
            Spikes(block_size*26+32, HEIGHT - block_size * 1-32, 16, 20,"up"),
            Spikes(block_size*26+64, HEIGHT - block_size *1-32, 16, 20,"up"),
            Spikes(block_size*26-32, HEIGHT - block_size * 1, 16, 20,"left"),
            Spikes(block_size*26-32, HEIGHT - block_size * 1+32, 16, 20,"left"),
            Spikes(block_size*26-32, HEIGHT - block_size *1+64, 16, 20,"left"),
            Spikes(block_size*27-8, HEIGHT - block_size * 1, 16, 20,"right"),
            Spikes(block_size*27-8, HEIGHT - block_size * 1+32, 16, 20,"right"),
            Spikes(block_size*27-8, HEIGHT - block_size *1+64, 16, 20,"right"),
            #spike 3 wall jump
            Spikes(block_size*28, HEIGHT - block_size * 5-32, 16, 20,"up"),
            Spikes(block_size*28+32, HEIGHT - block_size * 5-32, 16, 20,"up"),
            Spikes(block_size*28+64, HEIGHT - block_size * 5-32, 16, 20,"up"),
            Spikes(block_size * 28-32, HEIGHT - block_size* 5, 16, 20,"left"),
            Spikes(block_size * 28-32, HEIGHT - block_size* 5+32, 16, 20,"left")
            

        ]


        
        

        saws=[
                Saw(block_size *1, HEIGHT - block_size*6, 38, 38,7,30,90)
        ]


        spikedBalls= [

            SpikedBall(block_size *2, HEIGHT - block_size*6, 28, 28,7,5,45),
            SpikedBall(block_size *33, HEIGHT - block_size*3, 28, 28,7,5,45)
        
            ]
        
        

        fallingPlatform=FallingPlatform(0, 0, 32, 10)
        falling = [
                FallingPlatform(block_size * 6+i * fallingPlatform.image.get_width(), HEIGHT - block_size, 32, 10)
                for i in range(18)
                if i % 2 == 0
            ]
        

        spikeHeads=[
            SpikeHead(block_size * 5, HEIGHT - block_size * 3,54,52),
            SpikeHead(block_size * 11, HEIGHT - block_size * 3,54,52),
            
        ]


        platformsGreys=[
            PlatformsGrey(block_size * 12, HEIGHT - block_size * 5,32,8,"right"),
            PlatformsGrey(block_size * 17, HEIGHT - block_size * 5,32,8,"left")
        ]
        

        fire =Fire(0,0, 16, 32)
        fires=[
            Fire(block_size * 13+i*fire.image.get_width(), HEIGHT - block_size * 5, 16, 32)
            for i in range(11)
            if i < 2 or i > 8
        ]
    

        
        

        floor = [
                Block(i * block_size, HEIGHT - block_size, block_size,BIGDIRT)
                for i in range(35)
                if i < 5 or i > 17 and i < 23 or i > 29
                ]
        

        wallDown =  [
                Block(  block_size*(24+(a*4)),   HEIGHT - block_size*i,block_size,BIGDIRT)
                for i in range(6)
                for a in range(2)
                ]
        
    

        wallUp =  [
        Block(  block_size*26,  HEIGHT -  block_size*i,block_size,BIGDIRT)
        for i in range(12)
        if i < 2 or i > 3
        ]

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            Block(block_size *8-trampoline.image.get_width() , HEIGHT - block_size  * 5 + trampoline.image.get_height() , block_size-32,ROCKSTEIN),
            
            Block(block_size * 2-6, HEIGHT - block_size * 6-10, 29,LITTLECHAIN),
            Block(block_size * 4, HEIGHT - block_size * 4, block_size,BIGDIRT),
            Block(block_size * 3, HEIGHT - block_size * 4, block_size,BIGDIRT),
            Block(block_size * 4, HEIGHT - block_size * 5, block_size,BIGDIRT),



            Block(block_size * 10, HEIGHT - block_size * 5, block_size,BIGDIRT),
            Block(block_size * 18, HEIGHT - block_size * 3, block_size,BIGDIRT),
            Block(block_size * 10, HEIGHT - block_size * 3, block_size,BIGDIRT),
            Block(block_size * 10, HEIGHT - block_size * 4, block_size,BIGDIRT),



            Block(block_size * -2, HEIGHT - block_size * 1, block_size,BIGROCK),
            Block(block_size * -2, HEIGHT - block_size * 2, block_size,BIGROCK),
            Block(block_size * -2, HEIGHT - block_size * 3, block_size,BIGROCK),
            Block(block_size * -2, HEIGHT - block_size * 4, block_size,BIGROCK),
            Block(block_size * -2, HEIGHT - block_size * 5, block_size,BIGROCK),
            Block(block_size * -2, HEIGHT - block_size * 6, block_size,BIGROCK),

        ]
        for obj in wallDown:
            blocks.append(obj)
        for obj in wallUp:
            blocks.append(obj)
        for obj in floor:
            blocks.append(obj)


        start.on()
        end.OnEnd()
        objects = [
            *floor,
                *blocks,
                start,
                checkPoint,
                end,
                *platformsGreys,
                *spikeHeads,
                *fires,
                *fans,
                *falling,
                *trampolines,
                *spikes,
                *plants,
                *spikedBalls,
                *saws
                ]
                
        return objects
    

    def Level2(self,block_size):


        end = End(block_size * 4, HEIGHT - block_size * 6-32,64,64)

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
            Block(block_size * 2-6, HEIGHT - block_size * 6-10, 29,LITTLECHAIN),
            Block(block_size * 4, HEIGHT - block_size * 4, block_size,BIGDIRT),
            Block(block_size * 3, HEIGHT - block_size * 4, block_size,BIGDIRT),
            Block(block_size * 4, HEIGHT - block_size * 5, block_size,BIGDIRT),

        ]
        

        objects = [
                *blocks,
                end
                ]

        return objects
    
    def Level3(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]
        end = End(block_size * 3, HEIGHT - block_size * 2-32,64,64)


        objects = [
                *blocks,
                end
                ]

        return objects
    
    def Level4(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]
        end = End(block_size * 3, HEIGHT - block_size * 2-32,64,64)
        objects = [
                *blocks,
                end
                ]

        return objects
    
    def Level5(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects

    def Level6(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level7(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level8(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    def Level9(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
        

    def Level10(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level11(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level12(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level13(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level14(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level15(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level16(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level17(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level18(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level19(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level20(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level21(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level22(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level23(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level24(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level25(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level26(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level27(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level28(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects

    
    def Level29(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects

    def Level30(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects

    def Level31(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    
    def Level32(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level33(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level34(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level35(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level36(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level37(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level38(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level39(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level40(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level41(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level42(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
        
    def Level43(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level44(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level45(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level46(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level47(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level48(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level49(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level50(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
