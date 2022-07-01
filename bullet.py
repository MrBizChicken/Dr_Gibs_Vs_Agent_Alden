from constants import *
import pygame
from main_entity import Main_entity

class Bullet(Main_entity):
    def __init__(self, rect, width, height, dir):
        super().__init__(rect[0], rect[1], width, height)


        self.speed = 20
        self.spritesheet = pygame.image.load("images/egg_explosions.png")
        self.y_sprite_sheet_index = 0
        self.max_frame = 7
        self.frame = 0
        self.animation_speed = 0.1
        self.image = self.get_image_from_sprite_sheet(0, self.y_sprite_sheet_index)
        self.rect = self.image.get_rect()
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
        self.collide(solid_objects_group, crate_group, ammo_pickup_group, enemy_group, gun_crate_group, gun2_pickup_group, player_group, boss1_group)


    def collide(self, solid_objects_group, crate_group, ammo_pickup_group , enemy_group, gun_crate_group, gun2_pickup_group, player_group, boss1_group):

        if pygame.sprite.spritecollide(self, crate_group, True):
            self.kill()
            self.animate()
            for c in crate_group:
                c.drop_ammo(ammo_pickup_group)

        if pygame.sprite.spritecollide(self, solid_objects_group, False):
            self.kill()
            self.animate()

        for h in enemy_group:
            if pygame.Rect.colliderect(self.rect, h.rect):
                h.hurt(player_group)
                self.kill()
                self.animate()

                if h.health <= 0:
                    h.kill()

        for b1 in boss1_group:
            if pygame.Rect.colliderect(self.rect, b1.rect):
                b1.hurt(player_group)
                self.kill()
                self.animate()



                if b1.health <= 0:
                    b1.kill()


        for g in gun_crate_group:
            if pygame.Rect.colliderect(self.rect, g.rect):
                self.kill()
                self.animate()

                g.damage(gun2_pickup_group)
                if g.health <= 0:
                    g.kill()

    def get_image_from_sprite_sheet(self, row, col):
        image = pygame.Surface((16, 16))
        image.blit(self.spritesheet, (0, 0), (row, col, 16, 16))
        #image.set_colorkey()
        return image

    def animate(self):
        self.frame += self.animation_speed

        if self.frame > self.max_frame:
            self.frame = 7

        self.image = self.get_image_from_sprite_sheet(round(self.frame) * 16, self.y_sprite_sheet_index)
