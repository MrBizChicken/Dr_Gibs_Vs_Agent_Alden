from constants import *
import pygame
import random as rand
from main_entity import Main_entity

class Enemy_entity(Main_entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)


        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((48, 0, 0))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.direction  = pygame.math.Vector2(1, 1)

        self.can_move_timer = 2 #SECONDS
        self.timer_start_time = 0
        self.can_move_timer_ticks = 0
        self.can_move = True


    def random_direction_move(self, solid_objects_group, speed):
    # diagonal speed is to fast withoust this
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        if self.collison(solid_objects_group, "h"):
            self.direction  = self.random_vector2()

        self.rect.y += self.direction.y * speed
        if self.collison(solid_objects_group, "v"):
            self.direction  = self.random_vector2()


    def reverse_direction_move(self, solid_objects_group, speed):
        if pygame.time.get_ticks() > self.timer_start_time + self.can_move_timer * 1000:
            self.can_move = True
    # diagonal speed is to fast withoust this
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()



        # move
        if self.can_move:
            self.rect.x += self.direction.x * speed
        # check for collision
            if self.collison(solid_objects_group, "h"):
                self.can_move = False
                self.timer_start_time = pygame.time.get_ticks()
                # self.can_move_timer_ticks
                self.direction.x  = -self.direction.x

            self.rect.y += self.direction.y * speed

            if self.collison(solid_objects_group, "v"):

                self.can_move = False
                self.timer_start_time = pygame.time.get_ticks()
                # self.can_move_timer_ticks
                self.direction.y  = -self.direction.y




        # self.rect.y += self.direction.y * speed
        # if self.collison(solid_objects_group, "v"):
        #     if self.can_move:
        #         self.direction.y  = -self.direction.y
        #         self.can_move = False
        #         self.timer_ticks = 0



        # self.rect.x += self.direction.x * speed
        # if self.collison(solid_objects_group, "h"):
        #     if self.can_move:
        #         self.direction.x  = -self.direction.x
        #         self.can_move = False
        #         self.timer_ticks = 0
        #
        # self.rect.y += self.direction.y * speed
        # if self.collison(solid_objects_group, "v"):
        #     if self.can_move:
        #         self.direction.y  = -self.direction.y
        #         self.can_move = False
        #         self.timer_ticks = 0



    def random_vector2(self):
        new_vector = pygame.math.Vector2(0, 0)
        while new_vector == [0, 0]:
            new_vector = pygame.math.Vector2(rand.randint(-1, 1), rand.randint(-1, 1))
        return new_vector



    def can_move_timer(self):
        # print(self, self.timer_ticks)
        if self.timer_ticks >= self.change_direction_timer * 60:
            self.can_move = True
            self.timer_ticks = 0
        self.timer_ticks += 1
