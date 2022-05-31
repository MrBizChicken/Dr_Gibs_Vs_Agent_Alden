from constants import *
import pygame
import random
class Gun2_pickup(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.image.load("gun2.png")
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
