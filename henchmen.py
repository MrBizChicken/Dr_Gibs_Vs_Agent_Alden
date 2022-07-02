from constants import *
import pygame
import random as rand
from enemy_entity import Enemy_entity
import gun1
import gun2
class Henchmen(Enemy_entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.speed = 2
        self.change_direction_timer = 2 #SECONDS

        self.image = pygame.image.load("images/enemy.png")
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.health = 5
        self.gun = gun1.Gun1()
        self.random_move = rand.randint(0, 1)



        # self.direction = self.random_vector2()



    def update(self, main_group):
        solid_objects_group = main_group.solid_objects_group

        self.wait_random_direction_move(solid_objects_group, self.speed)

    def hurt(self, player_group):
        keys = pygame.key.get_pressed()

        for p in player_group:
            if keys[pygame.K_2] and p.can_swicth2 == True:

                self.gun = gun2.Gun2()

            if keys[pygame.K_1]:
                self.gun = gun1.Gun1()

        self.health -= self.gun.damage
