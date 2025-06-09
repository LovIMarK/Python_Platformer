"""
Central Import Module

This file gathers and centralizes imports for game objects, traps, checkpoints,
and visual elements across the platformer project. It ensures consistent access
to all modular classes used in level construction and gameplay.
"""

import sys
import time

# Extend system path to include relevant project folders for easy access
sys.path.extend([
    './Checkpoints',
    './Traps',
    './Core',
    './Ground',
    './Object',
    './Levels',
    './Utils',
])

# Core game object base
from objects import Object

# Trap elements
from Traps.bullet import Bullet
from Traps.dart import Dart
from Traps.bee import Bee
from Traps.plant import Plant
from Traps.fire import Fire
from Traps.spike_head import SpikeHead
from Traps.spikes import Spikes
from Traps.falling_platform import FallingPlatform
from Traps.spiked_ball import SpikedBall
from Traps.saw import Saw

# Player
from player import Player

# World objects
from Ground.block import Block
from Ground.particles import Particles
from Ground.button import Button
from Ground.text import Text

# Interactables
from Object.fan import Fan
from Object.platforms_brown import PlatformsBrown
from Object.platforms_grey import PlatformsGrey
from Object.trampoline import Trampoline
from Object.fruits import Fruit
from Object.cube import Cube

# Checkpoints and level progress
from Checkpoints.checkpoint import Start, Checkpoint, End



