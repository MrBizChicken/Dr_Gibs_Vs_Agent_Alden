from constants import *
import pygame
import random as rand
from enemy_entity import Enemy_entity
import gun1
import gun2
class Boss2(Enemy_entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.speed = 3
        self.change_direction_timer = 2 #SECONDS

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((200, 0, 0))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.health = 200
        self.gun = gun1.Gun1()



        # self.direction = self.random_vector2()



    def update(self, main_group):
        solid_objects_group = main_group.solid_objects_group
        self.wait_random_direction_move(solid_objects_group, self.speed)


    def hurt(self, player_group):
        self.rect.width += 5
        self.rect.height += 5
        keys = pygame.key.get_pressed()

        for p in player_group:
            if keys[pygame.K_2] and p.can_swicth2 == True:

                self.gun = gun2.Gun2()

            if keys[pygame.K_1]:
                self.gun = gun1.Gun1()
        self.health -= self.gun.damage
