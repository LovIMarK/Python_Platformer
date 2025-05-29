import os
import random
import math
from os import listdir
from os.path import isfile, join
import pygame

from assets_cache import load_sprite_sheet_cached


pygame.init()

from Ground.Sprite import *

pygame.display.set_caption("Platformer")


WIDTH, HEIGHT = 1200, 800
FPS = 60
PLAYER_VEL = 6
BIGDIRT=96,0
LITTLEDIRT=144,0
LITTLECHAIN=192,16
BIGROCK=0,0
LITTLEROCK=48,0
ROCKSTEIN=208,80
WOODPLAT=272,16


A=0,0
B=(8,0)
C=(16,0)
D=(24,0)
E=(32,0)
F=40,0
G=(48,0)
H=(56,0)
I=(64,0)
J=(72,0)
K=(0,10)
L=(8,10)
M=(16,10)
N=(24,10)
O=(32,10)
P=40,10
Q=(48,10)
R=(56,10)
S=64,10
T=(72,10)
U=(0,20)
V=(8,20)
W=(16,20)
X=(24,20)
Y=(32,20)
Z=(40,20)
ZERO=(0,30)
ONE=(8,30)
TWO=(16,30)
THREE=(24,30)
FOUR=(32,30)
FIVE=(40,30)
SIX=(48,30)
SEVEN=(56,30)
EIGHT=(64,30)
NINE=(72,30)




num_dictFps = {0: (0,30), 1: (8,30), 2: (16,30), 3: (24,30), 4: (32,30), 5: (40,30), 6: (48,30), 7: (56,30), 8: (64,30), 9:(72,30)}


window = pygame.display.set_mode((WIDTH, HEIGHT))


