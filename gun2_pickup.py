from constants import *
import pygame
import random
class Gun2_pickup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.width = 32
        self.height = 32
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/gun2.png")
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
