from Utils.settings import *
from Core.import_helper import *

def create_level_3(block_size):
    """
    Construct and return all objects and decorations for Level 3.

    Args:
        block_size (int): Base size of one block in the game world.

    Returns:
        Tuple[List[GameObject], List[DecorationObject]]: Lists of objects and decorations for this level.
    """

    # --- Key Decoration Elements ---
    checkpoint = Checkpoint(block_size * 20, HEIGHT - block_size * 5 - 32, 64, 64)
    start = Start(0 - 24, HEIGHT - block_size * 2 + 32, 64, 64)
    end = End(block_size * 40, HEIGHT - block_size * 5 - 32, 64, 64)

    # --- Fire hazards ---
    fire = Fire(0, 0, 16, 32)
    fires = [
        Fire(0 - (WIDTH / 2) + i * fire.image.get_width(), HEIGHT - block_size + 32, 16, 32)
        for i in range(88)
        if i < 61 or i > 75
    ]

    fire_first_run = [
        Fire(block_size * 7 + i * fire.image.get_width(), HEIGHT - block_size * 4 + 63, 16, 32)
        for i in range(21)
    ]

    second = [
        Fire(block_size * 28 + i * fire.image.get_width(), HEIGHT - block_size * 6 + 63 + 32, 16, 32)
        for i in range(19)
    ]

    for i in range(19):
        if i % 3 == 0:
            flickering_fire = Fire(block_size * 28 + i * fire.image.get_width(), HEIGHT - block_size * 6 + 63, 16, 32, True)
            flickering_fire.turn_on()
            fires.append(flickering_fire)

    fires.extend(fire_first_run)
    fires.extend(second)

    # --- Solid Blocks ---
    blocks = [
        Block(block_size * 6, HEIGHT - block_size * 3, block_size, block_size, BIG_ROCK),
        Block(block_size * 13, HEIGHT - block_size, block_size, block_size, BIG_ROCK),
        Block(block_size * 13, HEIGHT - block_size * 2, block_size, block_size, BIG_ROCK),
        Block(block_size * 13, HEIGHT - block_size * 3, block_size, block_size, BIG_ROCK),
        Block(block_size * 20, HEIGHT - block_size * 4, block_size, block_size, BIG_ROCK),
        Block(block_size * 21, HEIGHT - block_size * 4, block_size, block_size, BIG_ROCK),
        Block(block_size * 24, HEIGHT - block_size * 6, block_size, block_size, BIG_ROCK),
        Block(block_size * 35, HEIGHT - block_size * 4, block_size, block_size, BIG_ROCK),

        # Spiked wall platform
        *[
            Block(block_size * (29 + i), HEIGHT - block_size * 8, block_size, block_size, BIG_ROCK)
            for i in range(7)
        ],
        Block(block_size * 35, HEIGHT - block_size * 7, block_size, block_size, BIG_ROCK),
        Block(block_size * 35, HEIGHT - block_size * 6, block_size, block_size, BIG_ROCK),
        Block(block_size * 35, HEIGHT - block_size * 5, block_size, block_size, BIG_ROCK),

        # Final approach to end
        *[
            Block(block_size * x, HEIGHT - block_size * y, block_size, block_size, BIG_ROCK)
            for x, y in [
                (34, 2), (35, 2), (36, 2),
                (37, 2), (37, 3),
                (38, 2), (38, 3), (38, 4),
                (39, 2), (39, 3), (39, 4),
                (40, 2), (40, 3), (40, 4)
            ]
        ]
    ]

    # --- Left wall to prevent falling ---
    wall = [
        Block(0 - (WIDTH / 2), HEIGHT - block_size * i, block_size, block_size, BIG_ROCK)
        for i in range(11)
    ]
    blocks.extend(wall)

    # --- Spike Traps ---
    spike = Spikes(0, 0, 16, 20, "up")  # template spike
    spikes = [
        Spikes(block_size * 29 - 32, HEIGHT - block_size * 7 - 32, 16, 20, "left"),
        Spikes(block_size * 29 - 32, HEIGHT - block_size * 7 - 64, 16, 20, "left"),
        Spikes(block_size * 29 - 32, HEIGHT - block_size * 7 - 96, 16, 20, "left"),
        Spikes(block_size * 29, HEIGHT - block_size * 8 - 32, 16, 20, "up"),
        Spikes(block_size * 37 - 32, HEIGHT - block_size * 2 - 96, 16, 20, "left"),
        Spikes(block_size * 38 - 32, HEIGHT - block_size * 3 - 96, 16, 20, "left"),
    ]

    for a in range(5):
        for i in range(3):
            spikes.append(Spikes(block_size * 36 - 8, HEIGHT - block_size * (3 + a) - ((spike.width * 2) * (i + 1)), 16, 20, "right"))

    # --- Enemies ---
    spike_heads = [
        SpikeHead(block_size * -4, HEIGHT - block_size, 54, 52),
        SpikeHead(block_size * -3, HEIGHT - block_size * 2, 54, 52),
        SpikeHead(block_size * 10, HEIGHT - block_size * 4, 54, 52, 1),
        SpikeHead(block_size * 17, HEIGHT - block_size * 2, 54, 52, 1),
        SpikeHead(block_size * 22, HEIGHT - block_size * 4, 54, 52)
    ]

    fruits = [Fruit(block_size * 12, HEIGHT - block_size * 2, 32, 32, "Apple")]

    # --- Activation & Assembly ---
    start.on()
    objects = [
        *blocks,
        *spike_heads,
        *fires,
        *spikes
    ]

    decorations = [
        start,
        checkpoint,
        end,
        *fruits
    ]

    return objects, decorations
