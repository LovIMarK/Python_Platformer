from Utils.settings import *
import pygame
import random

class Particules(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.sprites = load_sprite_sheet_cached("Other", "", width, height)
        self.images = self.sprites["Dust Particle"]
        self.image = self.images[0]
        self.image.set_alpha(170)
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_delay = 3
        self.dy = random.randint(-3, 0)
        self.dx = random.randint(-2, 2)
        self.lifetime = random.randint(30, 80)
        self.rect = pygame.Rect(x, y, width, height)

    def loop(self):
        self.rect.y += self.dy
        self.rect.x += self.dx
        self.lifetime -= 1
        sprite_index = (self.animation_count // self.animation_delay) % len(self.images)
        self.image = self.images[sprite_index]
        self.animation_count += 1

    def draw(self, win, offset_x, offset_y):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))
