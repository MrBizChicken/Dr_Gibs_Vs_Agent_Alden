from constants import *
import pygame
import random
import bullet
import gun1
import gun2
from main_entity import Main_entity

class Player(Main_entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.speed = 5
        self.spritesheet = pygame.image.load("images/player_sheet.png").convert()
        self.y_sprite_sheet_index = 0

        self.image = self.get_image_from_sprite_sheet(0, self.y_sprite_sheet_index)
        self.rect = pygame.Rect(self.image.get_rect())
        self.direction  = pygame.math.Vector2(0, 0)
        self.bullet_size = self.width // 4
        self.facing_direction = pygame.math.Vector2(0, 0)
        self.can_shoot = True
        self.can_swicth2 = False
        self.frame = 0
        self.max_frame = 4
        self.animation_speed = 0.1

        self.gun = gun1.Gun1()

    def update(self, main_group):
        self.animate()

        solid_objects_group = main_group.solid_objects_group
        bullet_group = main_group.bullet_group
        ammo_pickup_group = main_group.ammo_pickup_group
        gun2_pickup_group = main_group.gun2_pickup_group

        self.key_input(solid_objects_group, bullet_group, ammo_pickup_group)
        self.move(solid_objects_group, self.speed)

        if pygame.time.get_ticks() % self.gun.shoot_speed == 0:
            self.can_shoot = True;


        if pygame.sprite.spritecollide(self, ammo_pickup_group, True):

            self.gun.ammo += 5

        if pygame.sprite.spritecollide(self, gun2_pickup_group, True):

            self.gun = gun2.Gun2()
            self.can_swicth2 = True


    def get_image_from_sprite_sheet(self, row, col):
        image = pygame.Surface((16, 16))
        image.blit(self.spritesheet, (0, 0), (row, col, 16, 16))
        #image.set_colorkey()
        return image

    def animate(self):
        self.frame += self.animation_speed

        if self.frame > self.max_frame:
            self.frame = 0
            print("yo")

        self.image = self.get_image_from_sprite_sheet(round(self.frame) * 16, self.y_sprite_sheet_index)


    def key_input(self, solid_objects_group, bullet_group, ammo_pickup_group):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            self.rect.x = 90
            self.rect.y = 90

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            self.y_sprite_sheet_index = 16
            self.facing_direction = pygame.math.Vector2(0, -1)

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y_sprite_sheet_index = 0
            self.direction.y = 1
            self.facing_direction = pygame.math.Vector2(0, 1)

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.y_sprite_sheet_index = 48
            self.direction.x = -1
            self.facing_direction = pygame.math.Vector2(-1, 0)

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.y_sprite_sheet_index = 64
            self.facing_direction = pygame.math.Vector2(1, 0)
        else:
            self.y_sprite_sheet_index = 32
            self.direction = pygame.math.Vector2(0, 0)

        if keys[pygame.K_e]:
            self.shoot(bullet_group, ammo_pickup_group)

        if keys[pygame.K_1]:
            self.gun = gun1.Gun1()
            print("gun1")


        if keys[pygame.K_2]:
            if self.can_swicth2 == True:
                self.gun = gun2.Gun2()
                print("gun2")

    def shoot(self, bullet_group, ammo_pickup_group):

        if self.can_shoot and self.gun.ammo > 0:
            self.can_shoot = False;
            bullet_group.add(bullet.Bullet(self.rect.center, self.bullet_size, self.bullet_size, self.facing_direction))
            self.gun.ammo -= 1
