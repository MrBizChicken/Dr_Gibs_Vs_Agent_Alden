from constants import *
import pygame
import random as rand
from main_entity import Main_entity
import gun1
import gun2
class Boss1(Main_entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.speed = 3
        self.change_direction_timer = 2 #SECONDS

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((200, 0, 0))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.health = 10
        self.gun = gun1.Gun1()



        # self.direction = self.random_vector2()



    def update(self, main_group):
        solid_objects_group = main_group.solid_objects_group
        self.move(solid_objects_group, self.speed)
        self.key_input(solid_objects_group)


    def hurt(self, player_group):
        self.width += 5
        self.height += 5
        keys = pygame.key.get_pressed()

        for p in player_group:
            if keys[pygame.K_2] and p.can_swicth2 == True:

                self.gun = gun2.Gun2()

            if keys[pygame.K_1]:
                self.gun = gun1.Gun1()
        self.health -= self.gun.damage




    def key_input(self, solid_objects_group):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            self.rect.x = 90
            self.rect.y = 90

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = 1
            self.facing_direction = pygame.math.Vector2(0, 1)

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = -1
            self.facing_direction = pygame.math.Vector2(0, -1)

        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = 1
            self.facing_direction = pygame.math.Vector2(1, 0)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = -1
            self.facing_direction = pygame.math.Vector2(-1, 0)
        else:
            self.direction.x = 0
