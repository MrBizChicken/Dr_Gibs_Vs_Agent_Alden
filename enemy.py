from constants import *
import pygame
import random
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.width = 64
        self.height = 64
        self.x = x
        self.y = y
        self.speed = 2
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((48, 0, 0))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.direction = -1


    def update(self, block_group):
        block = pygame.sprite.spritecollide(self, block_group, False)

        self.rect.x += self.direction

        if self.rect.left == 0:
            self.rect.x += self.direction
            self.direction = 1



        elif self.rect.right == GAME_WIDTH:
            self.rect.x += self.direction
            self.direction = -1

        elif block:
            self.rect.x += self.direction
            self.direction = 1
        elif block:
            self.rect.x += self.direction
            self.direction = -1
