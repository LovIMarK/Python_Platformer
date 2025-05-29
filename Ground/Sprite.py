import os
from Utils.settings import *

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = os.path.join("assets", dir1, dir2)
    images = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(os.path.join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites

def get_block(sizeX, sizeY, location):
    path = os.path.join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((sizeX, sizeY), pygame.SRCALPHA, 32)
    rect = pygame.Rect(location[0], location[1], sizeX, sizeY)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_text(size, location, color):
    if color == "white":
        path = os.path.join("assets", "Menu", "Text", "Text (White) (8x10).png")
    elif color == "black":
        path = os.path.join("assets", "Menu", "Text", "Text (Black) (8x10).png")
    else:
        raise ValueError(f"Color not recognized: {color}")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(location[0], location[1], size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def Flip(obj):
    pygame.transform.flip(obj, False, False)
