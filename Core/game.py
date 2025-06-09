"""
Game module for running the platformer using Pygame.
Handles game state, level transitions, player control, UI buttons, and rendering.
"""

import pygame
import time
from os.path import join

from Utils.settings import *
from Levels.level_handler import Level
from Ground.button import Button
from Ground.text import Text
from player import Player
from Utils.game_logic import (
    handle_player_movement,
    handle_decorations,
    handle_plant,
    handle_fan,
    handle_bee,
    handle_spikehead_collision,
    draw
)

# Global game state variables
block_size = 96
start_time = 0
paused_duration = 0
player = Player(0, HEIGHT - block_size - 50, 50, 50)
current_level = None
objects = []
decorations = []
particles = []
background_tiles = None
background_image = None
offset_x = 0
offset_y = 0
scroll = 0
paused = False
on_menu = False
max_level = 1

def get_background(name):
    """
    Load and tile the background image.

    Parameters:
        name (str): Filename of the background image.

    Returns:
        tuple: List of tile positions, loaded background image
    """
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = [
        (i * width, j * height)
        for i in range(-1, WIDTH // width + 1)
        for j in range(-1, HEIGHT // height + 1)
    ]
    return tiles, image

def reset_level():
    """
    Resets the current level and player state to the beginning.
    """
    global current_level, objects, decorations, particles
    global background_tiles, background_image, offset_x, offset_y
    global scroll, paused, on_menu, max_level

    current_level = Level(player.levels, block_size)
    objects, decorations = current_level.show_level()
    background_tiles, background_image = get_background(current_level.background)
    particles.clear()

    player.rect.x = 0
    player.rect.y = HEIGHT - block_size - 50
    player.checkPointX = 0
    player.checkPointY = 500
    player.lives = player.LIFE
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
    on_menu = False
    max_level = player.levels

def reset_chrono():
    """
    Reset the global timer and pause trackers.
    """
    global start_time, paused_duration, paused_time
    start_time = time.time()
    paused_duration = 0
    paused_time = 0

def main(window):
    """
    Main game update. Handles events, logic updates, rendering, and user input.

    Parameters:
        window (Surface): Pygame window surface to render the game on.
    """
    global current_level, objects, decorations, particles
    global background_tiles, background_image, offset_x, offset_y
    global scroll, paused, on_menu, max_level
    global start_time, paused_duration


    clock = pygame.time.Clock()
    paused_time = 0
    paused_duration = 0
    total_time = 0

    scroll_area_width = WIDTH / 2

    # UI buttons
    button_levels = Button(player.rect.x + (WIDTH / 2) - 60, 0, 21, 22, "Levels")
    button_retry = Button(button_levels.rect.x - button_levels.image.get_width(), 0, 21, 22, "Restart")
    button_next = Button(button_retry.rect.x - button_retry.image.get_width(), 0, 21, 22, "Next")
    button_levels.buttonLevel(player.unlockLevel)

    reset_level()
    reset_chrono()

    run = True
    while run:
        # --- Handle Events ---
        texts = [button_levels]
        if not player.onChrono and player.levels < player.unlockLevel:
            texts.append(button_next)
        texts.append(button_retry)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode((WIDTH, HEIGHT))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player.jump_count < 2 and not paused:
                    player.Jump()
            elif event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
                mouse_pos = pygame.mouse.get_pos()
                mouse_offset = (mouse_pos[0] + offset_x, mouse_pos[1])
                button_levels.OnButton(mouse_offset)
                button_next.OnButton(mouse_offset)
                button_retry.OnButton(mouse_offset)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_retry.Clicked(mouse_offset):
                        paused_time = 0
                        reset_level()
                        reset_chrono()

                        start_time = time.time()
                        paused_duration = 0
                    elif button_next.Clicked(mouse_offset) and not player.onChrono and player.levels < player.unlockLevel:
                        player.levels += 1
                        paused_time = 0
                        reset_level()
                        reset_chrono()

                        start_time = time.time()
                        paused_duration = 0
                    for obj in button_levels.BUTTONS:
                        if obj.rect.collidepoint(event.pos):
                            if button_levels.BUTTONS.index(obj) + 1 <= player.unlockLevel:
                                player.levels = button_levels.BUTTONS.index(obj) + 1
                                paused_time = 0
                                reset_level()
                                reset_chrono()

                                start_time = time.time()
                                paused_duration = 0
                    if button_levels.Clicked(mouse_offset):
                        if not paused or (not player.onChrono and not on_menu):
                            if max_level != player.levels:
                                button_levels.ChangeButton(player.levels)
                            on_menu = True
                            button_levels.DrawMenu(window)
                            paused = True
                        elif player.onChrono:
                            paused = False
                            on_menu = False
                        else:
                            on_menu = False

        # --- Game Logic ---
        if paused:
            if not paused_time:
                paused_time = time.time()
            if not player.onChrono and not on_menu:
                player.update(FPS)
                handle_player_movement(player, objects)
                for deco in decorations:
                    deco.update()
                    if deco.name == "end" and deco.rect.colliderect(player.rect):
                        player.onChrono = False
                draw(window, background_tiles, background_image, player, objects, offset_x, offset_y, scroll, particles, texts, decorations)

        else:
            # Chrono and FPS logic
            if paused_time:
                paused_duration += time.time() - paused_time
                paused_time = 0
            if player.onChrono:
                total_time = time.time() - start_time - paused_duration
            # Format chrono (MM:SS)
            chrono = time.strftime("%M:%S", time.gmtime(total_time))
            fps = int(clock.get_fps())

            # --- Display FPS ---
            for i, char in enumerate("FPS"):
                texts.append(Text(offset_x + i * 16, 0, 18, num_dictFps[char]))
            for i, digit in enumerate(str(fps)):
                texts.append(Text(offset_x + 64 + i * 16, 0, 18, num_dictFps[int(digit)]))

            # --- Display chrono ---
            chrono_x = offset_x + 0  # position tout à gauche
            for i, char in enumerate(chrono):
                if char == ":":
                    coords = num_dictFps[":"]
                else:
                    coords = num_dictFps[int(char)]
                texts.append(Text(chrono_x + i * 18, 20, 18, coords))

            """
            # --- Display score ---
            score_str = str(player.score).zfill(4)  
            score_x = offset_x + 0 
            score_y = 50  

            for i, char in enumerate(score_str):
                coords = num_dictFps[int(char)]
                texts.append(Text(score_x + i * 18, score_y, 18, coords))
            """

            """ # --- Display lives ---
            lives_text = "x" + str(player.lives)
            lives_x = offset_x + 0  
            lives_y = 80           

            for i, char in enumerate(lives_text):
                coords = num_dictFps[int(char)] if char.isdigit() else num_dictFps[char]
                texts.append(Text(lives_x + i * 18, lives_y, 18, coords))
            """   


            # Background scrolling
            scroll -= 1
            if abs(scroll) > background_image.get_width():
                scroll = 0

            # Update objects
            for obj in objects:
                obj.update()
                
                if obj.name in ("saw", "spikedBall") and not obj.chainExist:
                    particles.extend(obj.chains)
                    obj.chainExist = True
                if obj.name == "fan":
                    handle_fan(player, obj)
                    obj.update_particles_visibility(True)
                elif obj.name == "spikeHead":
                    handle_spikehead_collision(obj, objects)
                elif obj.name == "plant":
                    handle_plant(player, obj, objects)
                    if obj.bullet_exists:
                        obj.bullet.update()
                elif obj.name == "bee":
                    handle_bee(player, obj, objects)
                    if obj.dart_exists:
                        obj.dart.update()

            for deco in decorations:
                deco.update()

            player.update(FPS)
            handle_player_movement(player, objects)
            handle_decorations(player, decorations)

            # update & draw custom particles
            for obj in objects:
                if hasattr(obj, "particles") and getattr(obj, "particles_visible", True):
                    for p in obj.particles:
                        p.update()
                        p.draw(window, offset_x, offset_y)

            draw(window, background_tiles, background_image, player, objects, offset_x, offset_y, scroll, particles, texts, decorations)

            # Scrolling adjustment
            if ((player.rect.right - offset_x >= WIDTH - scroll_area_width and player.x_vel > 0) or
                (player.rect.left - offset_x <= scroll_area_width and player.x_vel < 0 and player.rect.x > 0)):
                offset_x += player.x_vel
                for btn in (button_levels, button_retry, button_next):
                    btn.rect.x += player.x_vel

            # Reset camera on death
            if player.lives == 0:
                if player.checkPointX == 0:
                    offset_x = -scroll_area_width
                else:
                    offset_x = player.checkPointX - scroll_area_width
                button_levels.rect.x = offset_x + WIDTH - 60
                button_retry.rect.x = button_levels.rect.x - button_levels.image.get_width()
                button_next.rect.x = button_retry.rect.x - button_retry.image.get_width()

            if not player.onChrono:
                paused = True

        clock.tick(FPS)

    pygame.quit()
    quit()

def launch():
    """
    Initialize Pygame and start the game.
    """
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    main(window)
