from settings import *
import pygame
from Traps.Bullet import Bullet

def draw(window, background, bg_image, player, objects, offset_x, offset_y, scroll, particules, textes, decoration):
    for tile in background:
        window.blit(bg_image, (tile[0] - scroll, tile[1]))
    for obj in particules:
        obj.draw(window, offset_x, offset_y)
    for obj in objects:
        obj.draw(window, offset_x, offset_y)
    for obj in textes:
        obj.draw(window, offset_x, offset_y)
    for obj in decoration:
        obj.draw(window, offset_x, offset_y)
    player.draw(window, offset_x, offset_y)
    pygame.display.update()

def handle_move(player, objects):
    keys = pygame.key.get_pressed()
    if not player.slidePlatRight and not player.slidePlatLeft:
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
        elif obj and (obj.name == "spikes" or obj.name == "spikeHead" or obj.name == "spikedBall" or obj.name == "saw" or obj.name == "plant" or obj.name == "bee"):
            player.make_hit()
        elif obj and obj.name == "fire" and obj.animation_name=="off":
            obj.hit() 
        elif obj and obj.name=="trampoline":
            player.Jump()
            player.jump_count+=1
            obj.Jump()
        elif obj and (obj.name =="platformsGrey" or obj.name =="platformsBrown"):
            if obj.direction=="right":
                player.make_slidePlat_right()
            else:
                player.make_slidePlat_left()
        elif obj and obj.name=="fallingPlatforms":
            obj.onFalling()
        elif obj and obj.name=="cube" and not obj.invisible:
            obj.HitTop()
        elif obj and (obj.name !="platformsGrey" or obj.name !="platformsBrown"):
            player.make_slidePlat_stop()

def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0 and obj.name!="woodPlat":
                player.rect.top = obj.rect.bottom
                player.hit_head()
            collided_objects.append(obj)
    return collided_objects

def collide(player, objects, dx):
    player.move(dx, 0)
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if obj.name=="block":
                collided_object = obj
            break
    player.move(-dx, 0)
    return collided_object

def handle_Decoration(player, decoration):
    for obj in decoration[:]:
        if pygame.sprite.collide_mask(player, obj):
            if obj.name!="checkPoint" and obj.name!="end" and obj.name!="start":
                obj.Collected()
                player.score+=10
            elif obj and obj.name=="checkPoint" and obj.CheckPoint_count==0:
                obj.Check()
                player.checkPointX=obj.rect.x+obj.rect.width
                player.checkPointY=obj.rect.y
            elif obj and obj.name=="end":
                obj.OnEnd()
                if player.onChrono:
                    player.levels+=1
                    if player.levels>player.unlockLevel:
                        player.unlockLevel+=1
                player.onChrono=False   
        elif obj.name!="checkPoint" and obj.name!="end" and obj.name!="start"and not obj.exist:
            decoration.remove(obj)

def Handle_plant(player, plant, objects):
    for obj in objects[:]:
        if pygame.sprite.collide_rect(player, plant.bullet):
            if plant.bulletExist:
                player.make_hit()
                objects.remove(plant.bullet)
                plant.bulletExist = False
                plant.bullet = Bullet(plant.rect.x, plant.rect.y+16, 16, 16)    
        elif pygame.sprite.collide_mask(obj, plant.bullet):
            if obj.name != "bullet" and plant.bulletExist:
                objects.remove(plant.bullet)
                plant.bulletExist = False
                plant.bullet = Bullet(plant.rect.x, plant.rect.y+16, 16, 16)
        elif plant.bullet.rect.x < plant.rect.x-plant.dist:
            if obj.name != "bullet" and plant.bulletExist:
                objects.remove(plant.bullet)
                plant.bulletExist = False
                plant.bullet = Bullet(plant.rect.x, plant.rect.y+16, 16, 16)
    if player.rect.x >= (plant.rect.x - 800) and player.rect.x <= plant.rect.x + 800:
        if not plant.bulletExist:
            plant.Attack()
            plant.bulletExist = True
            objects.append(plant.bullet)
    else:
        plant.StopAttack()

def Handle_fan(player, fan):
    if player.rect.y + 100 >= fan.rect.y and (player.rect.x > fan.rect.x - (fan.image.get_width() / 2) and player.rect.x < fan.rect.x + (fan.image.get_width() / 2)):
        player.onfan_count = 0
        player.onFan()
        fan.onFan()
    elif not (player.rect.x > fan.rect.x - (fan.image.get_width() / 2) and player.rect.x < fan.rect.x + (fan.image.get_width() / 2)):
        player.onfan = False
        player.onfan_count = 0

def Handle_Bee(player, bee, objects):
    for obj in objects[:]:
        if pygame.sprite.collide_rect(player, bee.dar):
            if bee.darExist:
                player.make_hit()
                objects.remove(bee.dar)
                bee.darExist = False
                bee.dar = Dar(bee.rect.x+20, bee.rect.y+34, 16, 16)    
        elif pygame.sprite.collide_mask(obj, bee.dar):
            if obj.name == "cube" and not obj.invisible:
                obj.HitTop()
            if obj.name != "bee" and obj.name != "dar" and bee.darExist:
                objects.remove(bee.dar)
                bee.darExist = False
                bee.dar = Dar(bee.rect.x+20, bee.rect.y+34, 16, 16)
        elif bee.dar.rect.y > bee.rect.y+bee.dist or bee.dar.rect.y > HEIGHT:
            if obj.name != "dar" and bee.darExist:
                objects.remove(bee.dar)
                bee.darExist = False
                bee.dar = Dar(bee.rect.x+20, bee.rect.y+34, 16, 16)
    if player.rect.x >= (bee.rect.x - 800) and player.rect.x <= bee.rect.x + 800:
        if not bee.darExist:
            bee.Attack()
            bee.darExist = True
            objects.append(bee.dar)
    else:
        bee.StopAttack()

def handleCollisionSpikeHead(spikehead, objects):
    for obj in objects:
        if pygame.sprite.collide_mask(spikehead, obj):
            if obj.name != "spikeHead" and obj.name != "start" and obj.name != "fire":
                spikehead.collide = True
                if spikehead.direction == 0:
                    spikehead.Left()
                    spikehead.direction += 1
                elif spikehead.direction == 1:
                    spikehead.Right()
                    spikehead.direction = 0
