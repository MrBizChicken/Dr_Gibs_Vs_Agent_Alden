from constants import *
import pygame
import random
class Gun_crate(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.image.load("gun_crate.png")
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.health = 5
    def update(self, solid_objects_group, bullet_group):
        pass
