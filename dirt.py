from constants import *
import pygame
import random
class Dirt(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.width = 64
        self.height = 64
        self.x = x
        self.y = y
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((102, 57, 49))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)

    def update(self):
        pass
