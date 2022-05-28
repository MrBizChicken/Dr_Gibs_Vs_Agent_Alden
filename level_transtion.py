from constants import *
import pygame
import random
class Level_transtion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.width = 64
        self.height = 64
        self.x = x
        self.y = y
        self.speed = 2
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((200, 200, 200))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.direction = -1


    def update(self):
        pass
