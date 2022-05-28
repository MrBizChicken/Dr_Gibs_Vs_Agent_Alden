from constants import *
import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dir):
        super().__init__()

        self.width = 20
        self.height = 20
        self.x = x
        self.y = y
        self.speed = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((251, 242, 54))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.dir = dir

        print(self.dir)

    def update(self, block_group):
        self.rect = self.rect.move(self.dir[0] * self.speed, self.dir[1] * self.speed)
        self.collison(block_group)




    def collison(self, block_group):
        block = pygame.sprite.spritecollide(self, block_group, True)
