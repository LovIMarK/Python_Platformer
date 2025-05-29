from settings import *
from levels.Level import *
from Ground.Button import Button
from Ground.Text import Text
from Player import Player
import pygame
import time

from utils.game_logic import (
    handle_move,
    handle_Decoration,
    Handle_plant,
    Handle_fan,
    Handle_Bee,
    handleCollisionSpikeHead,
    draw
)

def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []
    for i in range(-1, WIDTH // width + 1):
        for j in range(-1, HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    return tiles, image

block_size = 96
player = Player(0, HEIGHT - block_size - 50, 50, 50)
ActualLevel = None
objects = []
decoration = []
particules = []
background = None
bg_image = None
offset_x = 0
offset_y = 0
scroll = 0
paused = False
onMenu = False
levels = 1

def reset_level():
    global ActualLevel, objects, decoration, particules, background, bg_image, offset_x, offset_y, scroll, paused, onMenu, levels
    ActualLevel = Level(player.levels, block_size)
    objects, decoration = ActualLevel.showLevel()
    background, bg_image = get_background(ActualLevel.background)
    particules.clear()
    player.rect.x = 0
    player.rect.y = HEIGHT - block_size - 50
    player.checkPointX = 0
    player.checkPointY = 500
    player.lives = 3
    player.jump_count = 0
    player.x_vel = 0
    player.y_vel = 0
    player.onfan = False
    player.onfan_count = 0
    player.onChrono = True
    offset_x = player.rect.x - (WIDTH / 2)
    offset_y = 0
    scroll = 0
    paused = False
    onMenu = False
    levels = player.levels

def main(window):
    global ActualLevel, objects, decoration, particules, background, bg_image, offset_x, offset_y, scroll, paused, onMenu, levels

    clock = pygame.time.Clock()
    start_time = time.time()
    PausedTime = 0
    PausedDuration = 0
    times = 0
    scroll_area_height = 300
    scroll_area_width = WIDTH / 2

    buttonLevels = Button(player.rect.x + (WIDTH / 2) - 60, 0, 21, 22, "Levels")
    buttonRetry = Button(buttonLevels.rect.x - buttonLevels.image.get_width(), 0, 21, 22, "Restart")
    buttonNext = Button(buttonRetry.rect.x - buttonRetry.image.get_width(), 0, 21, 22, "Next")
    buttonLevels.buttonLevel(player.unlockLevel)

    reset_level()

    run = True
    while run:
        textes = [buttonLevels]
        if not player.onChrono or player.levels < player.unlockLevel:
            textes.append(buttonNext)
        textes.append(buttonRetry)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode((WIDTH, HEIGHT))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player.jump_count < 2 and not paused:
                    player.Jump()
                #elif event.key == pygame.K_SPACE and not player.slash and not paused:
                 #   player.Slash()
            elif event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                posMouse = pygame.mouse.get_pos()
                posMouseOffset = posMouse[0] + offset_x, posMouse[1]
                buttonLevels.OnButton(posMouseOffset)
                buttonNext.OnButton(posMouseOffset)
                buttonRetry.OnButton(posMouseOffset)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttonRetry.Clicked(posMouseOffset):
                        reset_level()
                    elif buttonNext.Clicked(posMouseOffset) and player.levels < player.unlockLevel:
                        player.levels += 1
                        reset_level()
                    for obj in buttonLevels.BUTTONS:
                        if obj.rect.collidepoint(event.pos):
                            if buttonLevels.BUTTONS.index(obj) + 1 <= player.unlockLevel:
                                player.levels = buttonLevels.BUTTONS.index(obj) + 1
                                reset_level()
                    if buttonLevels.Clicked(posMouseOffset) and (not paused or not player.onChrono and not onMenu):
                        if levels != player.levels:
                            buttonLevels.ChangeButton(player.levels)
                        onMenu = True
                        buttonLevels.DrawMenu(window)
                        paused = True
                    elif buttonLevels.Clicked(posMouseOffset) and player.onChrono:
                        paused = False
                        onMenu = False
                    elif buttonLevels.Clicked(posMouseOffset) and not player.onChrono:
                        onMenu = False

        if paused:
            if not PausedTime:
                PausedTime = time.time()
            if not player.onChrono and not onMenu:
                player.loop(FPS)
                handle_move(player, objects)
                for obj in decoration:
                    if obj.name == "end":
                        obj.loop()
                draw(window, background, bg_image, player, objects, offset_x, offset_y, scroll, particules, textes, decoration)
        elif not paused:
            Fps = []
            ChronoList = []
            posFps = 64
            posChrono = 0
            if PausedTime:
                PausedDuration += time.time() - PausedTime
                PausedTime = 0
            if player.onChrono:
                times = time.time() - start_time - PausedDuration
            chrono = time.strftime("%M%S", time.localtime(times))
            ChronoList.append(chrono)
            fps = int(clock.get_fps())
            Fps.append(fps)
            textes.append(Text(0 + offset_x, 0, 18, (F)))
            textes.append(Text(16 + offset_x, 0, 18, (P)))
            textes.append(Text(32 + offset_x, 0, 18, (S)))
            textes.append(Text(48 + offset_x, 0, 18, (16, 40)))
            digitsFps = [int(a) for a in str(Fps[0])]
            digitsChrono = [int(a) for a in str(ChronoList[0])]
            textes.append(Text(32 + offset_x, 20, 18, (16, 40)))
            for i in range(len(digitsChrono)):
                fpsnum = num_dictFps[digitsChrono[i]]
                textes.append(Text(offset_x + posChrono, 20, 18, fpsnum))
                posChrono += 16
                if i == 1:
                    posChrono += 16
            for i in range(len(digitsFps)):
                fpsnum = num_dictFps[digitsFps[i]]
                textes.append(Text(offset_x + posFps, 0, 18, fpsnum))
                posFps += 16
            scroll -= 1
            if abs(scroll) > bg_image.get_width():
                scroll = 0
            for obj in objects:
                if obj.name == "fallingPlatforms":
                    if not obj.particuleExist:
                        for particule in obj.particule:
                            particules.append(particule)
                        obj.particuleExist = True
                    obj.loop()
                elif obj.name == "spikedBall":
                    if not obj.chainExist:
                        for chain in obj.chains:
                            particules.append(chain)
                        obj.chainExist = True
                    obj.loop()
                elif obj.name == "saw":
                    if not obj.chainExist:
                        for chain in obj.chains:
                            particules.append(chain)
                        obj.chainExist = True
                    obj.loop()
                elif obj.name == "fire":
                    obj.loop()
                elif obj.name == "platformsGrey":
                    obj.loop()
                elif obj.name == "fan":
                    if not obj.particuleExist:
                        for particule in obj.particule:
                            particules.append(particule)
                        obj.particuleExist = True
                    obj.loop()
                    Handle_fan(player, obj)
                elif obj.name == "trampoline":
                    obj.loop()
                elif obj.name == "cube":
                    obj.loop()
                elif obj.name == "spikeHead":
                    obj.loop()
                    handleCollisionSpikeHead(obj, objects)
                elif obj.name == "plant":
                    Handle_plant(player, obj, objects)
                    obj.loop()
                    if obj.bulletExist:
                        obj.bullet.loop()
                elif obj.name == "bee":
                    Handle_Bee(player, obj, objects)
                    obj.loop()
                    if obj.darExist:
                        obj.dar.loop()
            for obj in decoration:
                if obj.name == "checkPoint":
                    obj.loop()
                elif obj.name == "start":
                    obj.loop()
                elif obj.name == "end":
                    obj.loop()
                elif obj.name == "fruit":
                    obj.loop()
            player.loop(FPS)
            handle_move(player, objects)
            handle_Decoration(player, decoration)
            for particule in particules[:]:
                particule.loop()
                if particule.lifetime <= 0:
                    particules.remove(particule)
                else:
                    particule.draw(window, offset_x, offset_y)
            draw(window, background, bg_image, player, objects, offset_x, offset_y, scroll, particules, textes, decoration)
            if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or ((player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0 and player.rect.x > 0):
                offset_x += player.x_vel
                buttonLevels.rect.x += player.x_vel
                buttonRetry.rect.x += player.x_vel
                buttonNext.rect.x += player.x_vel
            if player.lives == 0 and player.checkPointX == 0:
                offset_x = 0 - scroll_area_width
                buttonLevels.rect.x = WIDTH - 60 - scroll_area_width
                buttonRetry.rect.x = WIDTH - 60 - scroll_area_width - buttonLevels.image.get_width()
                buttonNext.rect.x = WIDTH - 60 - scroll_area_width - buttonLevels.image.get_width() - buttonRetry.image.get_width()
            elif player.lives == 0:
                offset_x = player.checkPointX - scroll_area_width
                buttonLevels.rect.x = player.checkPointX + WIDTH - 60 - scroll_area_width
                buttonRetry.rect.x = player.checkPointX + WIDTH - 60 - scroll_area_width - buttonLevels.image.get_width()
                buttonNext.rect.x = player.checkPointX + WIDTH - 60 - scroll_area_width - buttonLevels.image.get_width() - buttonRetry.image.get_width()
            if not player.onChrono:
                paused = True
        clock.tick(FPS)
    pygame.quit()
    quit()

def launch():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    main(window)
