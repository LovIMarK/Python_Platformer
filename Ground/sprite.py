"""
Utility functions for loading and manipulating sprites and tiles.

Includes functions for:
- Flipping sprites
- Loading sprite sheets into frame sequences
- Extracting specific terrain blocks or text glyphs from sprite sheets
"""

import os
import pygame
from Utils.settings import *


def flip_sprites(sprites):
    """
    Flip a list of sprites horizontally.

    Parameters:
        sprites (list[Surface]): List of Pygame surfaces.

    Returns:
        list[Surface]: Flipped surfaces.
    """
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(folder_1, folder_2, frame_width, frame_height, with_direction=False):
    """
    Load sprite sheets from a directory and slice them into frames.

    Parameters:
        folder_1 (str): Folder inside 'assets'.
        folder_2 (str): Subfolder under folder_1.
        frame_width (int): Width of one frame in the sheet.
        frame_height (int): Height of one frame in the sheet.
        with_direction (bool): If True, generate right/left versions.

    Returns:
        dict[str, list[Surface]]: A dictionary of sprite frame lists, optionally by direction.
    """
    path = os.path.join("assets", folder_1, folder_2)
    image_files = [
        f for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    ]

    sprites_dict = {}

    for image_file in image_files:
        sprite_sheet = pygame.image.load(os.path.join(path, image_file)).convert_alpha()

        frames = []
        for i in range(sprite_sheet.get_width() // frame_width):
            frame_surface = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA, 32)
            frame_rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame_surface.blit(sprite_sheet, (0, 0), frame_rect)
            frames.append(pygame.transform.scale2x(frame_surface))

        sprite_name = image_file.replace(".png", "")
        if with_direction:
            sprites_dict[f"{sprite_name}_right"] = frames
            sprites_dict[f"{sprite_name}_left"] = flip_sprites(frames)
        else:
            sprites_dict[sprite_name] = frames

    return sprites_dict


def get_terrain_block(width, height, sprite_coords):
    """
    Extract and scale a block from the terrain sheet.

    Parameters:
        width (int): Width of the block to extract.
        height (int): Height of the block to extract.
        sprite_coords (tuple[int, int]): Position (x, y) in the terrain sprite sheet.

    Returns:
        Surface: The extracted terrain block.
    """
    path = os.path.join("assets", "Terrain", "Terrain.png")
    sheet = pygame.image.load(path).convert_alpha()
    block = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    block.blit(sheet, (0, 0), pygame.Rect(*sprite_coords, width, height))
    return pygame.transform.scale2x(block)


def get_text_tile(size, sprite_coords, color):
    """
    Extract a text glyph from a pixel font sprite sheet.

    Parameters:
        size (int): Width and height of the tile.
        sprite_coords (tuple[int, int]): Top-left position of the tile in the image.
        color (str): 'white' or 'black'.

    Returns:
        Surface: The text tile surface.

    Raises:
        ValueError: If color is not 'white' or 'black'.
    """
    if color == "white":
        path = os.path.join("assets", "Menu", "Text", "Text (White) (8x10).png")
    elif color == "black":
        path = os.path.join("assets", "Menu", "Text", "Text (Black) (8x10).png")
    else:
        raise ValueError(f"Color not recognized: {color}")

    font_sheet = pygame.image.load(path).convert_alpha()
    tile = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    tile.blit(font_sheet, (0, 0), pygame.Rect(*sprite_coords, size, size))
    return pygame.transform.scale2x(tile)


def flip_surface(surface):
    """
    Return a vertically flipped surface.

    Parameters:
        surface (Surface): A Pygame surface.

    Returns:
        Surface: The same surface flipped vertically.
    """
    return pygame.transform.flip(surface, False, False)
