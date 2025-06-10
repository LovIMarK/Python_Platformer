"""
Global game settings and constants for the platformer.
Includes screen dimensions, FPS, player speed, sprite coordinates for terrain, and text tile positions.
"""

import os
import random
import math
from os import listdir
from os.path import isfile, join
import pygame

from Utils.assets_cache import load_sprite_sheet_cached
from Ground.sprite import *  # Used for graphical asset utilities

# Initialize pygame and window caption
pygame.init()
pygame.display.set_caption("Platformer")

# --- Screen and Gameplay Settings ---
WIDTH, HEIGHT = 1200, 800
FPS = 60
PLAYER_VEL = 6

# --- Sprite Sheet Coordinates (Terrain / Objects) ---
BIG_DIRT      = (96, 0)
LITTLE_DIRT   = (144, 0)
LITTLE_CHAIN  = (192, 16)
BIG_ROCK      = (0, 0)
LITTLE_ROCK   = (48, 0)
ROCK_STEIN    = (208, 80)
WOOD_PLATFORM = (272, 16)

# --- Pixel Font Coordinates (Letters) ---
A = (0, 0);     B = (8, 0);     C = (16, 0);   D = (24, 0)
E = (32, 0);    F = (40, 0);    G = (48, 0);   H = (56, 0)
I = (64, 0);    J = (72, 0);    K = (0, 10);   L = (8, 10)
M = (16, 10);   N = (24, 10);   O = (32, 10);  P = (40, 10)
Q = (48, 10);   R = (56, 10);   S = (64, 10);  T = (72, 10)
U = (0, 20);    V = (8, 20);    W = (16, 20);  X = (24, 20)
Y = (32, 20);   Z = (40, 20)

# --- Pixel Font Coordinates (Numbers) ---
ZERO  = (0, 30);   ONE   = (8, 30);   TWO   = (16, 30);  THREE = (24, 30)
FOUR  = (32, 30);  FIVE  = (40, 30);  SIX   = (48, 30);  SEVEN = (56, 30)
EIGHT = (64, 30);  NINE  = (72, 30)

# --- Mapping for Digits and Letters used in FPS/Chrono ---
num_dictFps = {
    0: ZERO, 1: ONE, 2: TWO, 3: THREE, 4: FOUR,
    5: FIVE, 6: SIX, 7: SEVEN, 8: EIGHT, 9: NINE,
    'F': F, 'P': P, 'S': S, 'L': L, 'I': I, 'V': V, 'E': E, 'x': X, 
    ':': (16, 40)
}

# --- Initialize Game Window ---
window = pygame.display.set_mode((WIDTH, HEIGHT))
