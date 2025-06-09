import pygame
from Utils.settings import *
from Core.import_helper import *

def create_level_2(block_size):
    """
    Create all the objects and decorations for level 2.

    Args:
        block_size (int): Size of each block in pixels.

    Returns:
        tuple[list, list]: A tuple containing game objects and decorative elements.
    """
    objects = []
    decorations = []

    # Start, checkpoint, and end
    start = Start(-24, HEIGHT - block_size * 3 - 32, 64, 64)
    checkpoint = Checkpoint(block_size * 19, HEIGHT - block_size * 2 - 32, 64, 64)
    end = End(block_size * 38, HEIGHT - block_size * 2 - 32, 64, 64)

    start.on()
    decorations.extend([start, checkpoint, end])

    # Static blocks
    blocks = [
        Block(0, HEIGHT - block_size * 2, block_size, block_size, BIG_DIRT),
        Block(block_size * 4, HEIGHT - block_size * 4, block_size, block_size, BIG_DIRT),
        Block(block_size * 4, HEIGHT - block_size * 5, block_size, block_size, BIG_DIRT),
    ]

    # Wood platforms
    y_offsets = [2.5, 4, 5.5, 7]
    for offset in y_offsets:
        blocks.append(Block(block_size * 3, HEIGHT - block_size * offset, 96, 18, WOOD_PLATFORM, "woodPlat"))

    # Top chain platforms
    chain_blocks = [
        Block(block_size * 23 + 11, HEIGHT - block_size * 2, 32, 32, LITTLE_CHAIN),
        Block(block_size * 24 + 11, HEIGHT - block_size * 3, 32, 32, LITTLE_CHAIN),
        Block(block_size * 25 + 11, HEIGHT - block_size * 4, 32, 32, LITTLE_CHAIN),
        Block(block_size * 26 + 11, HEIGHT - block_size * 5, 32, 32, LITTLE_CHAIN),
    ]
    blocks.extend(chain_blocks)

    # Left and middle wall structures
    for i in range(1, 12):
        blocks.append(Block(0 - (WIDTH // 2), HEIGHT - block_size * i, block_size, block_size, BIG_DIRT))

    for i in range(1, 8):
        blocks.append(Block(block_size * 4, HEIGHT - block_size * i, block_size, block_size, BIG_DIRT))

    # Platform greys
    platform_greys = []
    for i in range(21):
        x = block_size * 5 + i * 64
        if i < 9:
            platform_greys.append(PlatformsGrey(x, HEIGHT - block_size * 7, 32, 8, "right"))
        if i < 3:
            platform_greys.append(PlatformsGrey(x, HEIGHT - block_size * 5, 32, 8, "left"))
            platform_greys.append(PlatformsGrey(x, HEIGHT - block_size * 3, 32, 8, "left"))
        elif 3 <= i < 9:
            platform_greys.append(PlatformsGrey(x, HEIGHT - block_size * 5, 32, 8, "right"))
            platform_greys.append(PlatformsGrey(x, HEIGHT - block_size * 3, 32, 8, "right"))
        platform_greys.append(PlatformsGrey(x, HEIGHT - block_size * 1, 32, 8, "right"))

    # Platform greys
    for i in range(9):
        x = block_size * 6 + i * 64
        if i < 5:
            platform_greys.append(PlatformsGrey(x, HEIGHT - block_size * 6, 32, 8, "left"))
            platform_greys.append(PlatformsGrey(x, HEIGHT - block_size * 4, 32, 8, "left"))
        else:
            platform_greys.append(PlatformsGrey(x, HEIGHT - block_size * 6, 32, 8, "right"))
            platform_greys.append(PlatformsGrey(x, HEIGHT - block_size * 4, 32, 8, "right"))

    # Plants
    plants = [
        Plant(block_size * 12 - 12, HEIGHT - block_size * (8 - i * 2) + 12, 44, 42, 800)
        for i in range(3)
    ]

    # Spikes
    spikes = [
        # Near plants (left side)
        *[Spikes(block_size * 12 - 32, HEIGHT - block_size * y + dy, 16, 20, "left") for y in (7, 5, 3) for dy in (0, 32)],
        # Left column (right side)
        *[Spikes(block_size * 5 - 8, HEIGHT - block_size * y + dy, 16, 20, "right") for y, dy in zip((7, 6, 5, 4), (32, 0, 32, 0))],
        *[Spikes(block_size * 5 - 8, HEIGHT - block_size * y + 64, 16, 20, "right") for y in (7, 5)],
        # Top platform anti-jump (upward)
        *[Spikes(block_size * x + dx, HEIGHT - block_size * 3 - 32, 16, 20, "up")
          for x in (13, 14, 15, 16, 17) for dx in (0, 32, 64)]
    ]

    # Blocks under plants
    blocks_under_plants = []
    for plant in plants:
        block_x = plant.rect.x + 12
        block_y = plant.rect.y + plant.rect.height *2
        blocks_under_plants.append(Block(block_x, block_y, block_size, block_size, BIG_DIRT))

    blocks.extend(blocks_under_plants)

    # Trampolines
    trampolines = [
        Trampoline(block_size * (22 + i), HEIGHT - block_size * (1 + i) - 56, 28, 28)
        for i in range(5)
    ]

    # Bees
    bees = [
        Bee(block_size * (22 + i) + 36 + (i % 2) * 4, HEIGHT - block_size * (6 + i % 3), 36, 34, HEIGHT)
        for i in range(12)
    ]

    # Cubes
    cubes = [
        Cube(block_size * x, HEIGHT - block_size * y, 22, 22)
        for x, y in [(30, 4), (31, 5), (32, 4), (33, 4.5), (34, 4), (35, 5), (36, 4),
                     (30, 3), (32, 3), (34, 3), (36, 3)]
    ]

    

    # Floor blocks with gaps
    floor = [
        Block(i * block_size, HEIGHT - block_size, block_size, block_size, BIG_DIRT)
        for i in range(39) if i < 5 or 18 < i < 23 or i > 29
    ]

    # Aggregate all game objects
    objects.extend(floor + blocks + cubes + platform_greys + trampolines + spikes + plants + bees)

    return objects, decorations
