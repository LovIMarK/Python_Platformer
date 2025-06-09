from Utils.settings import *
from Core.import_helper import *

def create_level_1(block_size):
    """
    Construct level 1 with all game objects and decorations.

    Args:
        block_size (int): The size of each tile/block in pixels.

    Returns:
        tuple[list, list]: A tuple containing:
            - A list of all interactive game objects
            - A list of all decorative/static elements (like start, end, checkpoint)
    """
    # Core decorative elements
    checkpoint = Checkpoint(block_size * 19, HEIGHT - block_size * 2 - 32, 64, 64)
    start = Start(-24, HEIGHT - block_size * 3 - 32, 64, 64)
    end = End(block_size * 34, HEIGHT - block_size * 2 - 32, 64, 64)

    FIRE_SPACING = 32           

    # Enemies
    plants = [
        Plant(block_size * 24, HEIGHT - block_size * 6 + 20, 44, 42, 400),
    ]

    # Trampolines
    trampolines = [
        Trampoline(block_size * 8 - (block_size // 2) - 2, HEIGHT - block_size * 5, 28, 28)
    ]

    # Fans
    fans = [
        Fan(150, HEIGHT - block_size - 12, 24, 20)
    ]

    # Spikes
    spikes = [
        # First platform
        Spikes(block_size * 10, HEIGHT - block_size * 5 - 32, 16, 20, "up"),
        Spikes(block_size * 10 - 32, HEIGHT - block_size * 5 + 32, 16, 20, "left"),
        Spikes(block_size * 10 - 32, HEIGHT - block_size * 5, 16, 20, "left"),
        Spikes(block_size * 10 + 16, HEIGHT - block_size * 5 - 32, 16, 20, "up"),

        # Wall jump section 1
        *[Spikes(block_size * 26 + dx, HEIGHT - block_size, 16, 20, "up") for dx in (0, 32, 64)],
        *[Spikes(block_size * 26 - 32, HEIGHT - block_size + dy, 16, 20, "left") for dy in (0, 32, 64)],
        *[Spikes(block_size * 27 - 8, HEIGHT - block_size + dy, 16, 20, "right") for dy in (0, 32, 64)],

        # Wall jump section 2
        *[Spikes(block_size * 28 + dx, HEIGHT - block_size * 5 - 32, 16, 20, "up") for dx in (0, 32, 64)],
        *[Spikes(block_size * 28 - 32, HEIGHT - block_size * 5 + dy, 16, 20, "left") for dy in (0, 32)]
    ]

    # Falling platforms
    falling = [
        FallingPlatform(block_size * 6 + i * 64, HEIGHT - block_size, 32, 10)
        for i in range(18)
        if i % 2 == 0
    ]

    # Spike heads
    spike_heads = [
        SpikeHead(block_size * 5, HEIGHT - block_size * 3, 54, 52),
        SpikeHead(block_size * 11, HEIGHT - block_size * 3, 54, 52),
    ]

    # Moving platforms
    platforms_grey = [
        PlatformsGrey(block_size * 12, HEIGHT - block_size * 5, 32, 8, "right"),
        PlatformsGrey(block_size * 17, HEIGHT - block_size * 5, 32, 8, "left")
    ]

    # Fire traps
    fires = [
        Fire(block_size * 13 + i * FIRE_SPACING, HEIGHT - block_size * 5, 16, 32)
        for i in range(11)
        if i < 2 or i > 8
    ]

    # Ground floor blocks
    floor = [
        Block(i * block_size, HEIGHT - block_size, block_size, block_size, BIG_DIRT)
        for i in range(35)
        if i < 5 or 17 < i < 23 or i > 29
    ]

    # Walls
    wall_down = [
        Block(block_size * (24 + a * 4), HEIGHT - block_size * i, block_size, block_size, BIG_DIRT)
        for a in range(2)
        for i in range(6)
    ]

    wall_up = [
        Block(block_size * 26, HEIGHT - block_size * i, block_size, block_size, BIG_DIRT)
        for i in range(12)
        if i < 2 or i > 3
    ]

    # Other solid blocks
    trampoline = trampolines[0]
    other_blocks = [
        Block(0, HEIGHT - block_size * 2, block_size, block_size, BIG_DIRT),
        Block(block_size * 8 - trampoline.image.get_width(), HEIGHT - block_size * 5 + trampoline.image.get_height(), block_size - 32, block_size, ROCK_STEIN),
        Block(block_size * 4, HEIGHT - block_size * 4, block_size, block_size, BIG_DIRT),
        Block(block_size * 3, HEIGHT - block_size * 4, block_size, block_size, BIG_DIRT),
        Block(block_size * 4, HEIGHT - block_size * 5, block_size, block_size, BIG_DIRT),
        Block(block_size * 3, HEIGHT - block_size * 3, block_size, block_size, BIG_DIRT),
        Block(block_size * 4, HEIGHT - block_size * 3, block_size, block_size, BIG_DIRT),
        Block(block_size * 10, HEIGHT - block_size * 5, block_size, block_size, BIG_DIRT),
        Block(block_size * 18, HEIGHT - block_size * 3, block_size, block_size, BIG_DIRT),
        Block(block_size * 10, HEIGHT - block_size * 3, block_size, block_size, BIG_DIRT),
        Block(block_size * 10, HEIGHT - block_size * 4, block_size, block_size, BIG_DIRT),
    ]

    # Wall at far left of screen
    first_wall = [
        Block(-WIDTH // 2, HEIGHT - block_size * i, block_size, block_size, BIG_DIRT)
        for i in range(1, 12)
    ]

    # Activate start checkpoint
    start.on()

    # Group all objects and decorations
    objects = [
        *floor, *other_blocks, *platforms_grey, *spike_heads, *fires,
        *fans, *falling, *trampolines, *spikes, *plants, *wall_down, *wall_up, *first_wall
    ]
    decorations = [start, checkpoint, end]

    return objects, decorations