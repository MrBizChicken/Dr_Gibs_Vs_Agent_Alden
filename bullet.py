from constants import *
import pygame
from main_entity import Main_entity

class Bullet(Main_entity):
    def __init__(self, rect, width, height, dir):
        super().__init__(rect[0], rect[1], width, height)


        self.speed = 20
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((200, 200, 200))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.center = (self.x, self.y)
        self.dir = dir

    def update(self, main_group):
        solid_objects_group = main_group.solid_objects_group
        crate_group = main_group.crate_group
        ammo_pickup_group = main_group.ammo_pickup_group
        enemy_group = main_group.enemy_group
        gun_crate_group = main_group.gun_crate_group
        gun2_pickup_group = main_group.gun2_pickup_group
        player_group = main_group.player_group
        boss1_group = main_group.boss1_group
        self.rect = self.rect.move(self.dir.x * self.speed, self.dir.y * self.speed)
        self.collide(solid_objects_group, crate_group, ammo_pickup_group, enemy_group, gun_crate_group, gun2_pickup_group, player_group, boss1_group, main_group)


    def collide(self, solid_objects_group, crate_group, ammo_pickup_group , enemy_group, gun_crate_group, gun2_pickup_group, player_group, boss1_group, main_group):

        if pygame.sprite.spritecollide(self, crate_group, True):
            self.kill()
            for c in crate_group:
                c.drop_ammo(ammo_pickup_group)

        if pygame.sprite.spritecollide(self, solid_objects_group, False):
            self.kill()

        for h in enemy_group:
            if pygame.Rect.colliderect(self.rect, h.rect):
                h.hurt(player_group, main_group)
                self.kill()

                if h.health <= 0:
                    h.kill()

        for b1 in boss1_group:
            if pygame.Rect.colliderect(self.rect, b1.rect):
                b1.hurt(player_group)
                self.kill()


                if b1.health <= 0:
                    b1.kill()


        for g in gun_crate_group:
            if pygame.Rect.colliderect(self.rect, g.rect):
                self.kill()

                g.damage(gun2_pickup_group)
                if g.health <= 0:
                    g.kill()
