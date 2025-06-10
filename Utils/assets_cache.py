"""
Sprite and image caching utilities for the platformer game.

Functions:
- load_sprite_sheet_cached: Load and cache sprite sheets with optional flipping.
- load_image_cached: Load and cache individual image files.
"""

import pygame
from Ground.sprite import load_sprite_sheets

# Global caches to avoid reloading the same assets multiple times
_SPRITE_CACHE = {}
_IMAGE_CACHE = {}

def load_sprite_sheet_cached(folder, sheet_name, sprite_width, sprite_height, flip=False):
    """
    Load and cache a sprite sheet.

    Args:
        folder (str): Directory inside 'assets' containing the sprite sheet.
        sheet_name (str): Name of the sprite sheet subfolder or file.
        sprite_width (int): Width of a single sprite frame.
        sprite_height (int): Height of a single sprite frame.
        flip (bool): If True, also generate horizontally flipped versions of sprites.

    Returns:
        dict: A dictionary mapping animation names to lists of Pygame surfaces (sprites).
    """
    cache_key = (folder, sheet_name, sprite_width, sprite_height, flip)
    if cache_key not in _SPRITE_CACHE:
        _SPRITE_CACHE[cache_key] = load_sprite_sheets(folder, sheet_name, sprite_width, sprite_height, flip)
    return _SPRITE_CACHE[cache_key]

def load_image_cached(filepath):
    """
    Load and cache an image file.

    Args:
        filepath (str): Relative path to the image file.

    Returns:
        Surface: The loaded Pygame surface with transparency.
    """
    if filepath not in _IMAGE_CACHE:
        _IMAGE_CACHE[filepath] = pygame.image.load(filepath).convert_alpha()
    return _IMAGE_CACHE[filepath]
