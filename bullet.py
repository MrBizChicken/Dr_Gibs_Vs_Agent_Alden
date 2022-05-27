from constants import *
import pygame
import random
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direicton):
        super().__init__()

        self.width = 64
        self.height = 32
        self.x = x
        self.y = y
        self.speed = (5 ,5)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((251, 242, 54))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.direicton = direicton
    def update(self, block_group):
        self.rect.move(self.direicton) * self.speed
        self.collison(block_group)

    def collison(self, block_group):
        block = pygame.sprite.spritecollide(self, block_group, True)
