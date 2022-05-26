from constants import *
import pygame
import random
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 64
        self.height = 64
        self.x = 0
        self.y = 0
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)

    def update(self, dirt_group, stone_group):
        self.key_input()
        self.collide(dirt_group, stone_group)



    def key_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:

            if self.rect.x > 0:
                self.rect.x += -self.speed


        if keys[pygame.K_RIGHT]:
            if self.rect.right < GAME_WIDTH:
                self.rect.x += self.speed



        if keys[pygame.K_UP]:

            if self.rect.y > 0:
                self.rect.y += -self.speed

        if keys[pygame.K_DOWN]:
            if self.rect.bottom < GAME_HEIGHT:
                self.rect.y += self.speed
    def collide(self, dirt_group, stone_group):
        dirt = pygame.sprite.spritecollide(self, dirt_group, False)
        stone = pygame.sprite.spritecollide(self, stone_group, False)

        if dirt:
            if self.rect.bottom and self.rect.top and self.rect.left and self.rect.right < dirt[0].rect.bottom:
                self.rect.bottom = dirt[0].rect.top
        if stone:
            if self.rect.bottom and self.rect.top and self.rect.left and self.rect.right < stone[0].rect.bottom:
                self.rect.bottom = stone[0].rect.top
