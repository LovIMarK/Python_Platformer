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
    
