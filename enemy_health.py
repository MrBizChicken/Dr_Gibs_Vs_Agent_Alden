from constants import *
import pygame
import random as rand
from main_entity import Main_entity
import gun1
import gun2
class Enemy_health(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.speed = 3
        self.change_direction_timer = 2 #SECONDS
        self.height = height
        self.width = width
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((0, 255, 0))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (x, y)
        self.health = 10
