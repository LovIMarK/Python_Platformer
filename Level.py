
from Var import *
from Import import *


class Level():

    def __init__(self,level,block_size):
        self.level=level
        self.block_size=block_size
        self.background="yellow.png"
        
    
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
            Plant(block_size * 24,HEIGHT - block_size *6+20,44,42,400),
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


        
        

        


       
        
        

        fallingPlatform=FallingPlatform(0, 0, 32, 10)
        falling = [
                FallingPlatform(block_size * 6+i * fallingPlatform.image.get_width(), HEIGHT - block_size, 32, 10)
                for i in range(18)
                if i % 2 == 0
            ]
        

        # saws=[
        #         Saw(block_size *1, HEIGHT - block_size*6, 38, 38,7,30,90)
        # ]



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
                Block(i * block_size, HEIGHT - block_size, block_size,block_size,BIGDIRT)
                for i in range(35)
                if i < 5 or i > 17 and i < 23 or i > 29
                ]
        

        wallDown =  [
                Block(  block_size*(24+(a*4)),   HEIGHT - block_size*i,block_size,block_size,BIGDIRT)
                for i in range(6)
                for a in range(2)
                ]
        
    

        wallUp =  [
        Block(  block_size*26,  HEIGHT -  block_size*i,block_size,block_size,BIGDIRT)
        for i in range(12)
        if i < 2 or i > 3
        ]

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            Block(block_size *8-trampoline.image.get_width() , HEIGHT - block_size  * 5 + trampoline.image.get_height() , block_size-32,block_size,ROCKSTEIN),
            
            Block(block_size * 4, HEIGHT - block_size * 4, block_size,block_size,BIGDIRT),
            Block(block_size * 3, HEIGHT - block_size * 4, block_size,block_size,BIGDIRT),
            Block(block_size * 4, HEIGHT - block_size * 5, block_size,block_size,BIGDIRT),
            Block(block_size * 3, HEIGHT - block_size * 3, block_size,block_size,BIGDIRT),
            Block(block_size * 4, HEIGHT - block_size * 3, block_size,block_size,BIGDIRT),



            Block(block_size * 10, HEIGHT - block_size * 5, block_size,block_size,BIGDIRT),
            Block(block_size * 18, HEIGHT - block_size * 3, block_size,block_size,BIGDIRT),
            Block(block_size * 10, HEIGHT - block_size * 3, block_size,block_size,BIGDIRT),
            Block(block_size * 10, HEIGHT - block_size * 4, block_size,block_size,BIGDIRT),
            



        ]
        FirstWall = [
        Block(  0-(WIDTH/2),  HEIGHT -  block_size*i,block_size,block_size,BIGDIRT)
        for i in range(1,12)
        ]
    


        for obj in FirstWall:
            blocks.append(obj)



        for obj in wallDown:
            blocks.append(obj)
        for obj in wallUp:
            blocks.append(obj)
        for obj in floor:
            blocks.append(obj)


        start.on()
        objects = [
            *floor,
                *blocks,
                *platformsGreys,
                *spikeHeads,
                *fires,
                *fans,
                *falling,
                *trampolines,
                *spikes,
                *plants,

                ]
        decoration=[
            start,
            checkPoint,
            end,

        ]
        return objects,decoration
    

    def Level2(self,block_size):


        checkPoint=Checkpoint(block_size * 19, HEIGHT - block_size *2-32,64,64)
        start=Start(0-24,HEIGHT - block_size *3-32,64,64)
        end = End(block_size * 38,HEIGHT - block_size*2-32,64,64)

        block=Block(0,0, block_size-32,block_size,(208,16))
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
            Block(block_size * 4, HEIGHT - block_size * 4, block_size,block_size,BIGDIRT),
            Block(block_size * 4, HEIGHT - block_size * 5, block_size,block_size,BIGDIRT),

            Block(block_size * 3, HEIGHT - block_size * 2.5, 96,18,WOODPLAT,"woodPlat"),
            Block(block_size * 3, HEIGHT - block_size * 4, 96,18,WOODPLAT,"woodPlat"),
            Block(block_size * 3, HEIGHT - block_size * 5.5, 96,18,WOODPLAT,"woodPlat"),
            Block(block_size * 3, HEIGHT - block_size * 7, 96,18,WOODPLAT,"woodPlat"),


            Block(block_size * 12, HEIGHT - block_size * 7, block_size-32,block_size,(208,16)),
            Block(block_size * 12, HEIGHT - block_size * 5, block_size-32,block_size,(208,16)),
            Block(block_size * 12, HEIGHT - block_size * 3, block_size-32,block_size,(208,16)),



            Block(block_size * 12+block.image.get_width(), HEIGHT - block_size * 3, block_size-32,block_size,(208,16)),
            Block(block_size * 13+32, HEIGHT - block_size * 3, block_size-32,block_size,(208,16)),
            Block(block_size * 14, HEIGHT - block_size * 3, block_size-32,block_size,(208,16)),
            Block(block_size * 14+block.image.get_width(), HEIGHT - block_size * 3, block_size-32,block_size,(208,16)),
            Block(block_size * 15+32, HEIGHT - block_size * 3, block_size-32,block_size,(208,16)),
            Block(block_size * 16, HEIGHT - block_size * 3, block_size-32,block_size,(208,16)),
            Block(block_size * 16+block.image.get_width(), HEIGHT - block_size * 3, block_size-32,block_size,(208,16)),
            Block(block_size * 17+32, HEIGHT - block_size * 3, block_size-32,block_size,(208,16)),


            Block(block_size * 23+11, HEIGHT - block_size * 2, 32,32,LITTLECHAIN),
            Block(block_size * 24+11, HEIGHT - block_size * 3, 32,32,LITTLECHAIN),
            Block(block_size * 25+11, HEIGHT - block_size * 4, 32,32,LITTLECHAIN),
            Block(block_size * 26+11, HEIGHT - block_size * 5, 32,32,LITTLECHAIN),
            


        ]
       
        ##FirstWall
        for i in range(1,12):
           blocks.append( Block(  0-(WIDTH/2),  HEIGHT -  block_size*i,block_size,block_size,BIGDIRT))
        
        ##SecondWall
        for i in range(1,8):
            blocks.append( Block(  block_size * 4,  HEIGHT -  block_size*i,block_size,block_size,BIGDIRT))
        

      

        platformsGrey= PlatformsGrey(0,0,32,8,"left")
        platformsGreys=[]
        for i in range(21):
            if i<9:
                platformsGreys.append(PlatformsGrey(block_size * 5+i*platformsGrey.image.get_width(), HEIGHT - block_size * 7,32,8,"right"))
            if i<3 and i<9:
                platformsGreys.append(PlatformsGrey(block_size * 5+i*platformsGrey.image.get_width(), HEIGHT - block_size * 5,32,8,"left"))
                platformsGreys.append(PlatformsGrey(block_size * 5+i*platformsGrey.image.get_width(), HEIGHT - block_size * 3,32,8,"left"))
            elif i>3 and i<9:
                platformsGreys.append(PlatformsGrey(block_size * 5+i*platformsGrey.image.get_width(), HEIGHT - block_size * 5,32,8,"right"))
                platformsGreys.append(PlatformsGrey(block_size * 5+i*platformsGrey.image.get_width(), HEIGHT - block_size * 3,32,8,"right"))
            platformsGreys.append(PlatformsGrey(block_size * 5+i*platformsGrey.image.get_width(), HEIGHT - block_size * 1,32,8,"right"))
        
        
        
        
        for i in range (9):
            if i<5:
                platformsGreys.append(PlatformsGrey(block_size * 6+i*platformsGrey.image.get_width(), HEIGHT - block_size * 6,32,8,"left"))
                platformsGreys.append(PlatformsGrey(block_size * 6+i*platformsGrey.image.get_width(), HEIGHT - block_size * 4,32,8,"left"))
            elif i>4:
                platformsGreys.append(PlatformsGrey(block_size * 6+i*platformsGrey.image.get_width(), HEIGHT - block_size * 6,32,8,"right"))
                platformsGreys.append(PlatformsGrey(block_size * 6+i*platformsGrey.image.get_width(), HEIGHT - block_size * 4,32,8,"right"))

        plants=[
            Plant(block_size * 12-12, HEIGHT - block_size * 8+12,44,42,800),
            Plant(block_size * 12-12, HEIGHT - block_size * 6+12,44,42,800),
            Plant(block_size * 12-12, HEIGHT - block_size * 4+12,44,42,800),
        ]
        spikes=[

            ###Wall <plants
            Spikes(block_size * 12-32, HEIGHT - block_size* 7+32, 16, 20,"left"),
            Spikes(block_size * 12-32, HEIGHT - block_size* 7, 16, 20,"left"),
            Spikes(block_size * 12-32, HEIGHT - block_size* 5+32, 16, 20,"left"),
            Spikes(block_size * 12-32, HEIGHT - block_size* 5, 16, 20,"left"),
            Spikes(block_size * 12-32, HEIGHT - block_size* 3+32, 16, 20,"left"),
            Spikes(block_size * 12-32, HEIGHT - block_size* 3, 16, 20,"left"),


            ###Wall left
            Spikes(block_size * 5-8, HEIGHT - block_size* 7+32, 16, 20,"right"),
            Spikes(block_size * 5-8, HEIGHT - block_size* 7+64, 16, 20,"right"),

            Spikes(block_size * 5-8, HEIGHT - block_size* 6, 16, 20,"right"),
            Spikes(block_size * 5-8, HEIGHT - block_size* 6+32, 16, 20,"right"),

            Spikes(block_size * 5-8, HEIGHT - block_size* 5+32, 16, 20,"right"),
            Spikes(block_size * 5-8, HEIGHT - block_size* 5+64, 16, 20,"right"),

            Spikes(block_size * 5-8, HEIGHT - block_size* 4, 16, 20,"right"),
            Spikes(block_size * 5-8, HEIGHT - block_size* 4+32, 16, 20,"right"),


            ###wall no jump

            Spikes(block_size * 13, HEIGHT - block_size* 3-32, 16, 20,"up"),
            Spikes(block_size * 13+32, HEIGHT - block_size* 3-32, 16, 20,"up"),
            Spikes(block_size * 13+64, HEIGHT - block_size* 3-32, 16, 20,"up"),

            Spikes(block_size * 14, HEIGHT - block_size* 3-32, 16, 20,"up"),
            Spikes(block_size * 14+32, HEIGHT - block_size* 3-32, 16, 20,"up"),
            Spikes(block_size * 14+64, HEIGHT - block_size* 3-32, 16, 20,"up"),

            Spikes(block_size * 15, HEIGHT - block_size* 3-32, 16, 20,"up"),
            Spikes(block_size * 15+32, HEIGHT - block_size* 3-32, 16, 20,"up"),
            Spikes(block_size * 15+64, HEIGHT - block_size* 3-32, 16, 20,"up"),

            Spikes(block_size * 16, HEIGHT - block_size* 3-32, 16, 20,"up"),
            Spikes(block_size * 16+32, HEIGHT - block_size* 3-32, 16, 20,"up"),
            Spikes(block_size * 16+64, HEIGHT - block_size* 3-32, 16, 20,"up"),


            Spikes(block_size * 17, HEIGHT - block_size* 3-32, 16, 20,"up"),
            Spikes(block_size * 17+32, HEIGHT - block_size* 3-32, 16, 20,"up"),
            Spikes(block_size * 17+64, HEIGHT - block_size* 3-32, 16, 20,"up"),


        ]

        trampolines=[
            Trampoline(block_size *22 , HEIGHT - block_size  * 1-56, 28, 28),
            Trampoline(block_size *23 , HEIGHT - block_size  * 2-56, 28, 28),
            Trampoline(block_size *24 , HEIGHT - block_size  * 3-56, 28, 28),
            Trampoline(block_size *25 , HEIGHT - block_size  * 4-56, 28, 28),
            Trampoline(block_size *26 , HEIGHT - block_size  * 5-56, 28, 28),
        ]

        floor = [
                
                ]
        
        for i in range(39):
            if i < 5 or i > 18 and i < 23 or i > 29:
                floor.append(Block(i * block_size, HEIGHT - block_size, block_size,block_size,BIGDIRT))

       

        bees=[
            Bee(block_size *22+36 , HEIGHT - block_size  * 6, 36, 34,HEIGHT),
            Bee(block_size *23+40 , HEIGHT - block_size  * 7, 36, 34,HEIGHT),
            Bee(block_size *24+44 , HEIGHT - block_size  * 8, 36, 34,HEIGHT),
            Bee(block_size *28+44 , HEIGHT - block_size  * 8, 36, 34,HEIGHT),

            Bee(block_size *30 , HEIGHT - block_size  * 6, 36, 34,HEIGHT),
            Bee(block_size *31 , HEIGHT - block_size  * 8, 36, 34,HEIGHT),
            Bee(block_size *32 , HEIGHT - block_size  * 6, 36, 34,HEIGHT),
            Bee(block_size *33 , HEIGHT - block_size  * 6, 36, 34,HEIGHT),
            Bee(block_size *34 , HEIGHT - block_size  * 8, 36, 34,HEIGHT),
            Bee(block_size *35 , HEIGHT - block_size  * 6, 36, 34,HEIGHT),
            Bee(block_size *36 , HEIGHT - block_size  * 7, 36, 34,HEIGHT),
            Bee(block_size *37 , HEIGHT - block_size  * 6, 36, 34,HEIGHT),

        ]
        cubes=[
            Cube(block_size *30 , HEIGHT - block_size  * 4, 22, 22),
            Cube(block_size *31 , HEIGHT - block_size  * 5, 22, 22),
            Cube(block_size *32 , HEIGHT - block_size  * 4, 22, 22),
            Cube(block_size *33 , HEIGHT - block_size  * 4.5, 22, 22),
            Cube(block_size *34 , HEIGHT - block_size  * 4, 22, 22),
            Cube(block_size *35 , HEIGHT - block_size  * 5, 22, 22),
            Cube(block_size *36 , HEIGHT - block_size  * 4, 22, 22),




            Cube(block_size *30 , HEIGHT - block_size  * 3, 22, 22),
            Cube(block_size *32 , HEIGHT - block_size  * 3, 22, 22),
            Cube(block_size *34 , HEIGHT - block_size  * 3, 22, 22),
            Cube(block_size *36 , HEIGHT - block_size  * 3, 22, 22),
        ]

        start.on()
        objects = [
                *floor,
                *blocks,
                *cubes,
                *platformsGreys,
                *trampolines,
                *spikes,
                *plants,
                *bees
                ]
        
        decoration=[
            start,
            checkPoint,
            end,

        ]

        return objects,decoration
    
    def Level3(self,block_size):

        checkPoint=Checkpoint(block_size * 20, HEIGHT - block_size * 5-32,64,64)
        start=Start(0-24,HEIGHT - block_size *2+32,64,64)
        end = End(block_size * 40,HEIGHT - block_size*5-32,64,64)

        
        
        fire =Fire(0,0, 16, 32)
        fires=[
            
            Fire(0-(WIDTH/2)+i*fire.image.get_width(), HEIGHT - block_size * 1+32, 16, 32)
            for i in range(88)
            if i<61 or i>75
        ]


        fireFirstRun=[
            Fire(block_size * 7+i*fire.image.get_width(), HEIGHT - block_size * 4+63, 16, 32)
            for i in range(21)

        ]
        Second=[
            Fire(block_size * 28+i*fire.image.get_width(), HEIGHT - block_size * 6+63+32, 16, 32)
            for i in range(19)
            if i<19 


        ]
       
        for i in range(19):
            if i%3==0:
                fire=Fire(block_size * 28+i*fire.image.get_width(), HEIGHT - block_size * 6+63, 16, 32,True)
                fire.on()
                fires.append(fire)




        for obj in fireFirstRun:
            fires.append(obj)
        for obj in Second:
            fires.append(obj)


        blocks=[
               
                ##first trap
                Block( block_size * 6, HEIGHT - block_size * 3, block_size,block_size,BIGROCK),
                Block( block_size * 13, HEIGHT - block_size * 1, block_size,block_size,BIGROCK),
                Block( block_size * 13, HEIGHT - block_size * 2, block_size,block_size,BIGROCK),
                Block( block_size * 13, HEIGHT - block_size * 3, block_size,block_size,BIGROCK),



                ##checkPoint
                Block( block_size * 20, HEIGHT - block_size * 4, block_size,block_size,BIGROCK),
                Block( block_size * 21, HEIGHT - block_size * 4, block_size,block_size,BIGROCK),



                Block( block_size * 24, HEIGHT - block_size * 6, block_size,block_size,BIGROCK),


                 Block( block_size * 35,HEIGHT - block_size*4, block_size,block_size,BIGROCK),

                ## spikedwall
                Block( block_size * 29, HEIGHT - block_size * 8, block_size,block_size,BIGROCK),
                Block( block_size * 30, HEIGHT - block_size * 8, block_size,block_size,BIGROCK),
                Block( block_size * 31, HEIGHT - block_size * 8, block_size,block_size,BIGROCK),
                Block( block_size * 32, HEIGHT - block_size * 8, block_size,block_size,BIGROCK),
                Block( block_size * 33, HEIGHT - block_size * 8, block_size,block_size,BIGROCK),
                Block( block_size * 34, HEIGHT - block_size * 8, block_size,block_size,BIGROCK),
                Block( block_size * 35, HEIGHT - block_size * 8, block_size,block_size,BIGROCK),
                Block( block_size * 35, HEIGHT - block_size * 7, block_size,block_size,BIGROCK),
                Block( block_size * 35, HEIGHT - block_size * 6, block_size,block_size,BIGROCK),
                Block( block_size * 35, HEIGHT - block_size * 5, block_size,block_size,BIGROCK),


                Block( block_size * 34,HEIGHT - block_size*2, block_size,block_size,BIGROCK),
                Block( block_size * 35,HEIGHT - block_size*2, block_size,block_size,BIGROCK),
                Block( block_size * 36,HEIGHT - block_size*2, block_size,block_size,BIGROCK),

                Block( block_size * 37,HEIGHT - block_size*2, block_size,block_size,BIGROCK),
                Block( block_size * 37,HEIGHT - block_size*3, block_size,block_size,BIGROCK),

                Block( block_size * 38,HEIGHT - block_size*2, block_size,block_size,BIGROCK),
                Block( block_size * 38,HEIGHT - block_size*3, block_size,block_size,BIGROCK),
                Block( block_size * 38,HEIGHT - block_size*4, block_size,block_size,BIGROCK),

                Block( block_size * 39,HEIGHT - block_size*2, block_size,block_size,BIGROCK),
                Block( block_size * 39,HEIGHT - block_size*3, block_size,block_size,BIGROCK),
                Block( block_size * 39,HEIGHT - block_size*4, block_size,block_size,BIGROCK),
                Block( block_size * 40,HEIGHT - block_size*2, block_size,block_size,BIGROCK),
                Block( block_size * 40,HEIGHT - block_size*3, block_size,block_size,BIGROCK),
                Block( block_size * 40,HEIGHT - block_size*4, block_size,block_size,BIGROCK),


        ]
        wall=[
            
                Block(0-(WIDTH/2), HEIGHT - block_size * i, block_size,block_size,BIGROCK)
                for i in range(11)
        ]

        for obj in wall:
            blocks.append(obj)

        spike =Spikes(0,0, 16, 20,"up")
        spikes=[
            Spikes(block_size * 29-32, HEIGHT - block_size* 7-32, 16, 20,"left"),
            Spikes(block_size * 29-32, HEIGHT - block_size* 7-64, 16, 20,"left"),
            Spikes(block_size * 29-32, HEIGHT - block_size* 7-96, 16, 20,"left"),
            Spikes(block_size * 29, HEIGHT - block_size* 8-32, 16, 20,"up"),

            Spikes(block_size * 37-32, HEIGHT - block_size* 2-96, 16, 20,"left"),
            Spikes(block_size * 38-32, HEIGHT - block_size* 3-96, 16, 20,"left"),



        ]
        posy=3
        for a in range(5) :
            for i in range(3):
                spikes.append(Spikes(block_size * 36-8, HEIGHT - block_size* posy-((spike.width*2)*(i+1)), 16, 20,"right"))
            posy+=1
       

        spikeHeads=[
            SpikeHead(block_size * -4, HEIGHT - block_size * 1,54,52),
            SpikeHead(block_size * -3, HEIGHT - block_size * 2,54,52),
            SpikeHead(block_size * 10, HEIGHT - block_size * 4,54,52,1),
            SpikeHead(block_size * 17, HEIGHT - block_size * 2,54,52,1),
            SpikeHead(block_size * 22, HEIGHT - block_size * 4,54,52)
            
        ]

        fruits=[Fruit( block_size * 12,HEIGHT - block_size*2,32,32,"Apple")]


        start.on()
        objects = [
                *blocks,
                *spikeHeads,
                *fires,
                *spikes,
                ]

        decoration=[
            start,
            checkPoint,
            end,
            *fruits

        ]

        return objects,decoration
    
    def Level4(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]
        end = End(block_size * 3, HEIGHT - block_size * 2-32,64,64)
        objects = [
                *blocks,
                end
                ]

        decoration=[
            start,
            checkPoint,
            end,

        ]

        return objects,decoration
    
    def Level5(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        decoration=[
            start,
            checkPoint,
            end,

        ]

        return objects,decoration

    def Level6(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        decoration=[
            start,
            checkPoint,
            end,

        ]

        return objects,decoration
    
    def Level7(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        decoration=[
            start,
            checkPoint,
            end,

        ]
        return objects,decoration
    
    def Level8(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        decoration=[
            start,
            checkPoint,
            end,

        ]
        return objects,decoration
    def Level9(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        decoration=[
            start,
            checkPoint,
            end,

        ]
        return objects,decoration
        

    def Level10(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        decoration=[
            start,
            checkPoint,
            end,

        ]
        return objects,decoration
    
    def Level11(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level12(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level13(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level14(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level15(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level16(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level17(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level18(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level19(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level20(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level21(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level22(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level23(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level24(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level25(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level26(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level27(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects
    
    def Level28(self,block_size):

        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
            
        ]

        objects = [
                *blocks
                ]

        return objects

    
    def Level29(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects

    def Level30(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects

    def Level31(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    
    def Level32(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level33(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level34(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level35(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level36(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level37(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level38(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level39(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level40(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level41(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level42(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
        
    def Level43(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level44(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level45(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level46(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level47(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level48(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level49(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
    def Level50(self,block_size):
        blocks=[
            Block(0, HEIGHT - block_size * 2, block_size,block_size,BIGDIRT),
        ]
        objects = [*blocks]
        return objects
