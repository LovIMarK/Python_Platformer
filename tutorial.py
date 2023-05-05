from Var import *
from Level import *


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(-1,WIDTH // width + 1):
        for j in range(-1,HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image, player, objects, offset_x,scroll,particules,text):
  
    for tile in background:
        window.blit(bg_image, (tile[0]-scroll,tile[1]))
    
    

    
    for obj in particules:
        obj.draw(window, offset_x)    
    for obj in objects:
        obj.draw(window, offset_x)
    
    for obj in text:
        obj.draw(window, offset_x)
   

    player.draw(window, offset_x)
    pygame.display.update()





def handleCollisionSpikeHead(spikehead,objects):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(spikehead, obj):
            if obj.name!= "spikeHead"  :
                spikehead.collide=True
                if spikehead.direction==0:
                    spikehead.Left()
                    spikehead.direction+=1
                elif spikehead.direction==1:
                    spikehead.Right()
                    spikehead.direction=0


                # if spikehead.direction==0:
                #     spikehead.Top()
                #     spikehead.direction+=1
                # elif spikehead.direction==1:
                #     spikehead.Right()
                #     spikehead.direction+=1
                # elif spikehead.direction==2:
                #     spikehead.Bottom()
                #     spikehead.direction+=1
                # elif spikehead.direction==3:
                #     spikehead.Left()
                #     spikehead.direction=0
     


                collided_objects.append(obj)

    return collided_objects
    




def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                if obj.name!="start" and  obj.name!="checkPoint" and  obj.name!="end" :
                    player.rect.bottom = obj.rect.top
                    player.landed()
            elif dy < 0:
                if obj.name!="start" and  obj.name!="checkPoint" and  obj.name!="end" :
                    player.rect.top = obj.rect.bottom
                    player.hit_head()

            collided_objects.append(obj)

    return collided_objects


def collide(player, objects, dx):
    player.move(dx, 0)
  
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if obj.name=="block" :
                collided_object = obj
                
                
            break
       
           

    player.move(-dx, 0)
    
    return collided_object


def handle_move(player, objects):
    
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, PLAYER_VEL * 2)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    if player.onChrono:
        if keys[pygame.K_LEFT] and not collide_left:
            player.move_left(PLAYER_VEL)
            player.StopSlide()
        elif keys[pygame.K_RIGHT] and not collide_right:
            player.move_right(PLAYER_VEL)
            player.StopSlide()
        
        elif keys[pygame.K_LEFT] and collide_left and not vertical_collide:
            player.Slide()
        elif keys[pygame.K_RIGHT] and  collide_right and not vertical_collide:
            player.Slide()
        elif not collide_left and not collide_right:
            player.StopSlide()

    

   

    for obj in to_check:
        if obj and obj.name == "fire" and obj.animation_name=="on" :
            player.make_hit()
            
           
        elif obj and (obj.name== "spikes" or  obj.name== "spikeHead" or obj.name=="spikedBall"or obj.name=="saw"or obj.name=="plant"):
            if obj.name=="plant":
                obj.Hit()
            player.make_hit()
            
        elif obj and obj.name == "fire" and obj.animation_name=="off":
            obj.hit() 
                 
        elif obj and obj.name=="trampoline":
            player.Jump()
            player.jump_count+=1
            obj.Jump()
        elif obj and obj.name=="fan":
            pass
        elif obj and (obj.name =="platformsGrey" or obj.name =="platformsBrown"):
            player.make_slidePlat()
        elif obj and obj.name=="checkPoint" and obj.CheckPoint_count==0:
            obj.Check()
            player.checkPointX=obj.rect.x+obj.rect.width
            player.checkPointY=obj.rect.y
        elif obj and obj.name=="end":
            if player.onChrono:
                player.levels+=1
                if player.levels>player.unlockLevel:
                    player.unlockLevel+=1
            player.onChrono=False
        elif obj and (obj.name=="fallingPlatforms"):
            obj.onFalling()
        
        
  
            



        elif obj and (obj.name !="platformsGrey" or obj.name !="platformsBrown"):
            player.slidePlat=False

       
        #if obj and obj.name =="fan" and player.rect.y+20>=obj.rect.y and (player.rect.x >obj.rect.x and player.rect.x <obj.rect.x+obj.image.get_width())  :
            #print(player.rect.x)
            #print(obj.rect.x)
            #player.fan()
            #player.rect.y-=10




            
def Handle_fan(player,fan):
    
    if player.rect.y+300>=fan.rect.y and (player.rect.x >fan.rect.x-(fan.image.get_width()/2) and player.rect.x <fan.rect.x+(fan.image.get_width()/2)):
        player.onfan_count=0
        player.onFan()
        fan.onFan()
    elif not (player.rect.x>fan.rect.x-(fan.image.get_width()/2) and player.rect.x <fan.rect.x+(fan.image.get_width()/2)) :
        player.onfan=False
        player.onfan_count=0


def Handle_plant(player,plant,objects):


    for obj in objects:
        if pygame.sprite.collide_rect( player,plant.bullet):
           if plant.bulletExist:
                #player.make_hit()
                objects.remove(plant.bullet)
                plant.bulletExist=False
                plant.bullet=Bullet(plant.rect.x,plant.rect.y+16,16,16)    
        elif pygame.sprite.collide_mask( obj,plant.bullet):
            if obj.name != "bullet" and plant.bulletExist:
                objects.remove(plant.bullet)
                plant.bulletExist=False
                plant.bullet=Bullet(plant.rect.x,plant.rect.y+16,16,16)
        elif plant.bullet.rect.x < plant.rect.x-400:
            if obj.name != "bullet" and plant.bulletExist:
                objects.remove(plant.bullet)
                plant.bulletExist=False
                plant.bullet=Bullet(plant.rect.x,plant.rect.y+16,16,16)
        # elif obj.name=="plant" :
        #     if not plant.exist:
        #         try:   
        #             objects.remove(plant)
                    
        #         except:
        #             pass
        #     elif plant.hit and plant.bullet!=None:
        #         try:   
                    
        #             plant.bullet==None
        #             objects.remove(plant.bullet)
        #         except:
        #             pass
                
                
               
               
        
    
    if player.rect.x>=(plant.rect.x -800) and player.rect.x<=plant.rect.x+800:
        
        if not plant.bulletExist:
            plant.Attack()
            plant.bulletExist=True
            objects.append(plant.bullet)
    else:
        plant.StopAttack()



block_size = 96
player = Player(0, HEIGHT - block_size-50, 50, 50)
buttonLevels = Button(player.rect.x+(WIDTH/2)-60,0, 21, 22,"Levels" )
buttonRetry = Button(player.rect.x+(WIDTH/2)-60-buttonLevels.image.get_width(),0, 21, 22,"Restart" )
buttonNext = Button(player.rect.x+(WIDTH/2)-60-buttonLevels.image.get_width()-buttonRetry.image.get_width(),0, 21, 22,"Next" )
def main(window):
    paused=False
    clock = pygame.time.Clock()
    player.rect.x=0
    player.rect.y=HEIGHT - block_size-50
    background, bg_image = get_background("Yellow.png")
    offset_x = player.rect.x-(WIDTH/2)
    scroll_area_width =  WIDTH/2 #300#
    
    scroll=0
    run = True



    start_time=time.time()
    PausedTime=0
    PausedDuration=0
    times=0

    
    onMenu=False
    levels=player.levels
    buttonLevels.BUTTONS.clear()
    buttonLevels.buttonLevel(player.unlockLevel)

    

    
    
    ActualLevel=Level(player.levels,block_size)
    particules=[]


    objects = ActualLevel.showLevel()


    for obj in objects:
        if obj.name == "fan":
            obj.on()
        elif obj.name == "fallingPlatforms":
            obj.on()
        elif obj.name == "platformsGrey":
            obj.on()
        elif obj.name == "spikedBall":
            obj.on()
        elif obj.name == "saw":
            obj.on()
        elif obj.name == "spikes":
            obj.on()
        elif obj.name == "fan":
            obj.on()






    

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player.jump_count < 2 and not paused:
                    player.Jump()
                elif event.key==pygame.K_SPACE and not player.slash and not paused:
                    player.Slash()
            elif event.type == pygame.MOUSEMOTION:
                posMouse = pygame.mouse.get_pos()
                posMouseOffset=posMouse[0]+offset_x,posMouse[1]
                buttonLevels.OnButton(posMouseOffset)
                buttonNext.OnButton(posMouseOffset)
                buttonRetry.OnButton(posMouseOffset)
                        
            elif event.type == pygame.MOUSEBUTTONDOWN :
                posMouse = pygame.mouse.get_pos()
                if buttonRetry.rect.collidepoint(event.pos):
                    main(window)
                elif buttonNext.rect.collidepoint(event.pos):
                    pass
                for obj in buttonLevels.BUTTONS:
                    if obj.rect.collidepoint(event.pos):
                        if buttonLevels.BUTTONS.index(obj)+1 <=player.unlockLevel:
                            player.levels=buttonLevels.BUTTONS.index(obj)+1
                            player.onChrono=True
                            main(window)
                if buttonLevels.Clicked() and (not paused or not player.onChrono and not onMenu ):
                    
                    if levels!=player.levels:
                        buttonLevels.ChangeButton(player.levels)
                    onMenu=True

                    buttonLevels.DrawMenu(window)
                    paused=True
                    
                elif buttonLevels.Clicked() and player.onChrono:
                    paused=False
                    onMenu=False
                    
                elif buttonLevels.Clicked() and not player.onChrono:
                    onMenu=False






        if paused:
            textes=[]
            textes.append(buttonLevels)
            # if not player.onChrono:
            #     textes.append(buttonNext)
            textes.append(buttonNext)
            textes.append(buttonRetry)

            if not PausedTime:
                PausedTime=time.time()
                
            
            if not player.onChrono and not onMenu:
                
                player.loop(FPS)
                handle_move(player, objects)
                draw(window, background, bg_image, player, objects, offset_x,scroll,particules,textes)
                
                

        elif not paused:

            textes=[]
            Fps=[]
            ChronoList=[]
            posFps=64
            posChrono=0
            

            textes.append(buttonLevels)
            textes.append(buttonRetry)
            

            if PausedTime:
                PausedDuration += time.time() - PausedTime
                PausedTime=0

            if player.onChrono:
                times =time.time()-start_time-PausedDuration
            
        
            
            chrono =  time.strftime("%M%S", time.localtime(times))
            ChronoList.append(chrono)
            fps = int(clock.get_fps())
            Fps.append(fps)


            textes.append(Text(0+offset_x,0,18,(F)))
            textes.append(Text(16+offset_x,0,18,(P)))
            textes.append(Text(32+offset_x,0,18,(S)))
            textes.append(Text(48+offset_x,0,18,(16,40)))

            digitsFps = [int(a) for a in str(Fps[0])]
            digitsChrono = [int(a) for a in str(ChronoList[0])]
            textes.append(Text(32+offset_x,20,18,(16,40)))
            for i in range(len(digitsChrono)):
                fpsnum=num_dictFps[digitsChrono[i]]
                textes.append(Text(offset_x+posChrono,20,18,fpsnum))
                posChrono+=16
                if i ==1 :
                    posChrono+=16


            


            for i in range(len(digitsFps)):
                fpsnum=num_dictFps[digitsFps[i]]
                textes.append(Text(offset_x+posFps,0,18,fpsnum))
                posFps+=16


            
        
            scroll -= 1
            if abs(scroll) > bg_image.get_width():
                scroll = 0

            clock.tick(FPS)




            for obj in objects:
                if obj.name == "fallingPlatforms":
                    if not obj.particuleExist:
                        for particule in obj.particule:
                            particules.append(particule)
                        obj.particuleExist=True
                    obj.loop()
                elif obj.name == "spikedBall":
                    if not obj.chainExist:
                        for chain in obj.chains:
                            particules.append(chain)
                        obj.chainExist=True
                    obj.loop()
                elif obj.name == "saw":
                    if not obj.chainExist:
                        for chain in obj.chains:
                            particules.append(chain)
                        obj.chainExist=True
                    obj.loop()
                elif obj.name == "fire":
                    obj.loop()
                elif obj.name == "platformsGrey":
                    obj.loop()
                elif obj.name == "fan":
                    if not obj.particuleExist:
                        for particule in obj.particule:
                            particules.append(particule)
                        obj.particuleExist=True
                    obj.loop()
                    Handle_fan(player,obj)
                elif obj.name == "trampoline":
                    obj.loop()
                elif obj.name == "spikeHead":
                    obj.loop()
                    handleCollisionSpikeHead(obj,objects)
                elif obj.name == "plant":
                    Handle_plant(player,obj,objects)
                    obj.loop()
                    if obj.bulletExist:
                        obj.bullet.loop()
                elif obj.name == "checkPoint":
                    obj.loop()
                elif obj.name == "start":
                    obj.loop()
                elif obj.name == "end":
                    obj.loop()
                
            player.loop(FPS)
            handle_move(player, objects)            
            
            draw(window, background, bg_image, player, objects, offset_x,scroll,particules,textes)
            


            if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                    (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
                offset_x += player.x_vel
                buttonLevels.rect.x +=player.x_vel
            
         
            if player.lives==0 and player.checkPointX==0:
                offset_x=0-scroll_area_width
                buttonLevels.rect.x =WIDTH-60 -scroll_area_width
            elif player.lives==0:
                offset_x=player.checkPointX-scroll_area_width
                buttonLevels.rect.x =player.checkPointX +WIDTH-60-scroll_area_width

            if not player.onChrono:
                paused=True
            


    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
