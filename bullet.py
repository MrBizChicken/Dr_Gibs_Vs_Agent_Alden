from constants import *
import pygame
from main_entity import Main_entity

class Bullet(Main_entity):
    def __init__(self, rect, width, height, dir):
        super().__init__(rect[0], rect[1], width, height)


        self.speed = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((200, 200, 200))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.center = (self.x, self.y)
        self.dir = dir
        print(pygame.sprite.Group(self))

    def update(self, solid_objects_group, bullet_group, crate_group):
        self.rect = self.rect.move(self.dir.x * self.speed, self.dir.y * self.speed)
        self.collide(solid_objects_group, crate_group)


    def collide(self, solid_objects_group, crate_group):
        if pygame.sprite.spritecollide(self, crate_group, True):
            self.kill()
        if pygame.sprite.spritecollide(self, solid_objects_group, False):
            self.kill()
