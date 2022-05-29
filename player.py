from constants import *
import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 64
        self.height = 64
        self.x = 90
        self.y = 90
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.pd = 0
    def update(self, block_group):
        self.key_input()
        self.collison(block_group)



    def key_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            self.rect.x = 0
            self.rect.y = 0



        if keys[pygame.K_LEFT]:
            if self.rect.x > 0:
                self.rect.x += -self.speed

            self.pd = (-1, 0)

        if keys[pygame.K_RIGHT]:
            if self.rect.right < GAME_WIDTH:
                self.rect.x += self.speed

            self.pd = (1, 0)


        if keys[pygame.K_UP]:

            if self.rect.y > 0:
                self.rect.y += -self.speed

            self.pd = (0, -1)



        if keys[pygame.K_DOWN]:
            if self.rect.bottom < GAME_HEIGHT:
                self.rect.y += self.speed

            self.pd = (0, 1)


    def collison(self, block_group):
        for block in block_group:
            collide = pygame.sprite.Rect.colliderect(self.rect, block.rect)

            if collide:
                #right collison
                if self.pd[0] > 0:
                    self.rect.right = block.rect.left

                #left collison
                if self.pd[0] < 0:
                    self.rect.left = block.rect.right

                #bottom collison
                if self.pd[1] > 0:
                    self.rect.bottom = block.rect.top

                #top collison
                if self.pd[1] < 0:
                    self.rect.top = block.rect.bottom
