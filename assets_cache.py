import pygame
from Ground.Sprite import load_sprite_sheets

_SPRITE_CACHE = {}
_IMAGE_CACHE = {}

def load_sprite_sheet_cached(dir1, dir2, width, height, direction=False):
    key = (dir1, dir2, width, height, direction)
    if key not in _SPRITE_CACHE:
        _SPRITE_CACHE[key] = load_sprite_sheets(dir1, dir2, width, height, direction)
    return _SPRITE_CACHE[key]

def load_image_cached(path):
    if path not in _IMAGE_CACHE:
        _IMAGE_CACHE[path] = pygame.image.load(path).convert_alpha()
    return _IMAGE_CACHE[path]
