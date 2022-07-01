from constants import *
import pygame

class Table(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/table.png")
        picture = pygame. transform. scale(self.image, (126, 126))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)


    def update(self, main_group):
        pass
