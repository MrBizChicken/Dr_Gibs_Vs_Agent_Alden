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
        self.pd = 0
    def update(self, block_group):
        self.key_input(block_group)



    def key_input(self, block_group):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            block = pygame.sprite.spritecollide(self, block_group, False)
            if not block:
                if self.rect.x > 0:
                    self.rect.x += -self.speed
            else:
                self.rect.left = block[0].rect.right
            self.pd = (-1, 0)
        elif keys[pygame.K_RIGHT]:
            block = pygame.sprite.spritecollide(self, block_group, False)
            if not block:
                if self.rect.right < GAME_WIDTH:
                    self.rect.x += self.speed
            else:
                self.rect.right = block[0].rect.left

            self.pd = (1, 0)

        elif keys[pygame.K_UP]:
            block = pygame.sprite.spritecollide(self, block_group, False)
            if not block:
                if self.rect.y > 0:
                    self.rect.y += -self.speed
            else:
                self.rect.top = block[0].rect.bottom
            self.pd = (0, -1)

        elif keys[pygame.K_DOWN]:
            block = pygame.sprite.spritecollide(self, block_group, False)
            if not block:
                if self.rect.bottom < GAME_HEIGHT:
                    self.rect.y += self.speed
            else:
                self.rect.bottom = block[0].rect.top
            self.pd = (0, 1)
