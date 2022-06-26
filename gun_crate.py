from constants import *
import pygame
import random
import gun1
import gun2_pickup
class Gun_crate(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/gun_crate.png")
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.health = 10
        self.gun1 = gun1.Gun1()

    def update(self, main_group):
        pass

    def damage(self, gun2_pickup_group):


        self.health -= self.gun1.damage
        if self.health <= 0:
            gun2_pickup_group.add(gun2_pickup.Gun2_pickup(self.rect.x, self.rect.y))
