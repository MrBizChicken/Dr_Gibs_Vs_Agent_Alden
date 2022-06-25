from constants import *
import pygame
import random
import ammo_pickup
class Crate(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/crate.png")
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.random_drop = random.randint(0, 1)


    def update(self, solid_objects_group, bullet_group ,player_group):
        pass
    def drop_ammo(self, ammo_pickup_group):
        if self.random_drop == 1:
            ammo_pickup_group.add(ammo_pickup.Ammo_pickup(self.rect.x, self.rect.y))
        else:
            pass
