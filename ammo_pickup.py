from constants import *
import pygame
import random
class Ammo_pickup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.width = 64
        self.height = 64
        self.x = x
        self.y = y
        self.speed = 5
        self.image = pygame.image.load("ammo.png")
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)

    def update(self):
        pass
