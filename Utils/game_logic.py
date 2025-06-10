"""
Game Logic Module

Handles movement, collisions, interactions with traps and decorations,
and rendering for all game elements.
"""

import pygame
from settings import *
from Traps.bullet import Bullet
from Traps.dart import Dart

def draw(window, background_tiles, background_image, player, objects, offset_x, offset_y, scroll, particles, texts, decorations):
    """
    Draw all game elements on the screen.
    """
    for tile in background_tiles:
        window.blit(background_image, (tile[0] - scroll, tile[1]))

    for particle in particles:
        particle.draw(window, offset_x, offset_y)

    for obj in objects:
        obj.draw(window, offset_x, offset_y)

    for text in texts:
        text.draw(window, offset_x, offset_y)

    for deco in decorations:
        deco.draw(window, offset_x, offset_y)

    player.draw(window, offset_x, offset_y)
    pygame.display.update()


def handle_player_movement(player, objects):
    """
    Handle player keyboard input and update movement.
    """
    keys = pygame.key.get_pressed()
    if not player.slidePlatRight and not player.slidePlatLeft:
        player.x_vel = 0

    collide_left = detect_collision(player, objects, -PLAYER_VEL * 2)
    collide_right = detect_collision(player, objects, PLAYER_VEL * 2)
    vertical_collisions = handle_vertical_collisions(player, objects, player.y_vel)
    all_collisions = [collide_left, collide_right, *vertical_collisions]

    if player.onChrono:
        if keys[pygame.K_LEFT] and not collide_left:
            player.move_left(PLAYER_VEL)
            player.StopSlide()
        elif keys[pygame.K_RIGHT] and not collide_right:
            player.move_right(PLAYER_VEL)
            player.StopSlide()
        elif keys[pygame.K_LEFT] and collide_left and not vertical_collisions:
            player.Slide()
        elif keys[pygame.K_RIGHT] and collide_right and not vertical_collisions:
            player.Slide()
        elif not collide_left and not collide_right:
            player.StopSlide()

    for obj in all_collisions:
        if obj is None:
            continue
        if obj.name == "fire" and obj.animation_name == "on":
            player.make_hit()
        elif obj.name in ("spikes", "spikeHead", "spikedBall", "saw", "plant", "bee"):
            player.make_hit()
        elif obj.name == "fire" and obj.animation_name == "off":
            obj.hit()
        elif obj.name == "trampoline":
            player.Jump(jump_strength=7)
            player.jump_count += 1
            obj.start_jumping()
        elif obj.name in ("platformsGrey", "platformsBrown"):
            if obj.direction == "right":
                player.make_slidePlat_right()
            else:
                player.make_slidePlat_left()
        elif obj.name == "fallingPlatforms":
            obj.onFalling()
        elif obj.name == "cube" and not obj.is_invisible:
            obj.hit_top()
        elif obj.name not in ("platformsGrey", "platformsBrown"):
            player.make_slidePlat_stop()


def handle_vertical_collisions(player, objects, dy):
    """
    Handle vertical (Y-axis) collisions and return all collided objects.
    """
    collided = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0 and obj.name != "woodPlat":
                player.rect.top = obj.rect.bottom
                player.hit_head()
            collided.append(obj)
    return collided


def detect_collision(player, objects, dx):
    """
    Detect horizontal (X-axis) collisions for the player.
    """
    player.move(dx, 0)
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if obj.name == "block":
                collided_object = obj
            break
    player.move(-dx, 0)
    return collided_object


def handle_decorations(player, decorations):
    """
    Handle player interactions with decorative elements such as collectibles,
    checkpoints, start point, and end-level triggers.

    This function updates the player's score, checkpoint positions, and level state.
    Decorations that no longer exist (e.g. collected items) are removed.
    """

    for decoration in decorations[:]:
        # Skip if either player or decoration is missing a collision mask
        if not hasattr(player, "mask") or not hasattr(decoration, "mask"):
            continue
        if player.mask is None or decoration.mask is None:
            continue

        # Handle collision between player and decoration
        if pygame.sprite.collide_mask(player, decoration):
            # Collectible (e.g. coins, orbs)
            if decoration.name not in ("checkPoint", "end", "start"):
                if decoration.name == "fruit":
                    decoration.collect()
                    player.score += 10

            # Checkpoint activation
            elif decoration.name == "checkPoint" and getattr(decoration, "CheckPoint_count", 0) == 0:
                if hasattr(decoration, "Check") and callable(decoration.Check):
                    decoration.Check()
                    player.checkPointX = decoration.rect.x + decoration.rect.width
                    player.checkPointY = decoration.rect.y

            # End-level trigger
            elif decoration.name == "end":
                if hasattr(decoration, "OnEnd") and callable(decoration.OnEnd):
                    decoration.OnEnd()
                if player.onChrono:
                    player.levels += 1
                    if player.levels > player.unlockLevel:
                        player.unlockLevel += 1
                player.onChrono = False

        # Remove collectibles after being collected (if marked as non-existent)
        elif decoration.name not in ("checkPoint", "end", "start"):
            if getattr(decoration, "exist", True) is False:
                decorations.remove(decoration)


def handle_plant(player, plant, objects):
    """
    Manage plant attacks and bullet collisions.
    """
    if plant.bullet_exists:
        if pygame.sprite.collide_rect(player, plant.bullet):
            player.make_hit()
            plant.bullet.destroyed = True

        for obj in objects:
            if pygame.sprite.collide_mask(obj, plant.bullet):
                if obj.name not in ("bullet", "plant"):
                    plant.bullet.destroyed = True

        if (
            plant.bullet.rect.x < plant.rect.x - plant.attack_range or
            plant.bullet.rect.x > plant.rect.x + plant.attack_range
        ):
            plant.bullet.destroyed = True

    if plant.bullet.destroyed:
        if plant.bullet in objects:
            objects.remove(plant.bullet)
        plant.bullet_exists = False
        plant.bullet = Bullet(plant.rect.x - 10, plant.rect.y + 16, 16, 16)

    if abs(player.rect.x - plant.rect.x) <= plant.attack_range:
        if not plant.bullet_exists:
            plant.attack()
            plant.bullet_exists = True
            objects.append(plant.bullet)
    else:
        plant.stop_attack()


def handle_fan(player, fan):
    """
    Handle fan interactions and push effect on player.
    """
    if player.rect.y + 100 >= fan.rect.y and fan.rect.x - fan.image.get_width() / 2 < player.rect.x < fan.rect.x + fan.image.get_width() / 2:
        player.onfan_count = 0
        player.onFan()
    elif not fan.rect.x - fan.image.get_width() / 2 < player.rect.x < fan.rect.x + fan.image.get_width() / 2:
        player.onfan = False
        player.onfan_count = 0


def handle_bee(player, bee, objects):
    """
    Handle bee projectile attacks and collisions.
    """
    for obj in objects[:]:
        if pygame.sprite.collide_rect(player, bee.dart):
            if bee.dart_exists:
                player.make_hit()
                objects.remove(bee.dart)
                bee.dart_exists = False
                bee.dart = Dart(bee.rect.x + 20, bee.rect.y + 34, 16, 16)
        elif pygame.sprite.collide_mask(obj, bee.dart):
            if obj.name == "cube" and not obj.invisible:
                obj.HitTop()
            if obj.name not in ("bee", "dart") and bee.dart_exists:
                objects.remove(bee.dart)
                bee.dart_exists = False
                bee.dart = Dart(bee.rect.x + 20, bee.rect.y + 34, 16, 16)
        elif bee.dart.rect.y > bee.rect.y + bee.dist or bee.dart.rect.y > HEIGHT:
            if obj.name != "dart" and bee.dart_exists:
                objects.remove(bee.dart)
                bee.dart_exists = False
                bee.dart = Dart(bee.rect.x + 20, bee.rect.y + 34, 16, 16)

    if abs(player.rect.x - bee.rect.x) <= 800:
        if not bee.dart_exists:
            bee.attack()
            bee.dart_exists = True
            objects.append(bee.dart)
    else:
        bee.stop_attack()


def handle_spikehead_collision(spikehead, objects):
    """
    Handle spikehead bounce logic when colliding with other objects.
    """
    for obj in objects:
        if pygame.sprite.collide_mask(spikehead, obj):
            if obj.name not in ("spikeHead", "start", "fire"):
                spikehead.collide = True
                if spikehead.direction == 0:
                    spikehead.hit_left()
                    spikehead.direction = 1
                elif spikehead.direction == 1:
                    spikehead.hit_right()
                    spikehead.direction = 0
