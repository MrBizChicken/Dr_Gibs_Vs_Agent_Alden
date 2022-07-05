from constants import *
import sys, pygame, player


class Groups_man:
    def __init__(self):

        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.ammo_pickup_group = pygame.sprite.Group()
        self.block_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.crate_group = pygame.sprite.Group()
        self.gun_crate_group = pygame.sprite.Group()
        self.gun2_pickup_group = pygame.sprite.Group()
        self.solid_objects_group = pygame.sprite.Group()
        self.door_group = pygame.sprite.Group()
        self.boss1_group = pygame.sprite.Group()
        self.door_lock_group = pygame.sprite.Group()
        self.table_group = pygame.sprite.Group()
        self.drawable_objects = pygame.sprite.Group()
        self.main_group = self.update_main_group()
        self.tp_group = pygame.sprite.Group()
        self.enemy_health_group = pygame.sprite.Group()




    def update(self):
        self.main_group = self.update_main_group()
        self.solid_objects_group.empty()
        self.solid_objects_group.add(self.block_group , self.enemy_group, self.crate_group, self.gun_crate_group, self.boss1_group, self.door_lock_group, self.table_group, self.tp_group)
        self.solid_objects_group.update(self)
        self.crate_group.update(self)
        self.gun_crate_group.update(self)
        self.player_group.update(self)
        self.block_group.update(self)
        self.bullet_group.update(self)
        self.enemy_group.update(self)
        self.ammo_pickup_group.update()
        self.boss1_group.update(self)
        self.gun2_pickup_group.update()



    def get_drawing_group(self):
        self.drawable_objects.empty()
        self.drawable_objects.add(
            self.player_group,
            self.bullet_group,
            self.ammo_pickup_group,
            self.block_group,
            self.enemy_group,
            self.crate_group,
            self.gun_crate_group,
            self.gun2_pickup_group,
            self.solid_objects_group,
            self.door_group,
            self.boss1_group,
            self.door_lock_group,
            self.table_group,
            self.tp_group,
            self.enemy_health_group
        )
        return self.drawable_objects

    def get_group(self, search):
        return self.main_group[search]

    def get_main_group(self):
        return self.main_group

    def update_main_group(self):
        return {
            "player_group" : self.player_group,
            "bullet_group" : self.bullet_group,
            "ammo_pickup_group" : self.ammo_pickup_group,
            "block_group" : self.block_group,
            "enemy_group" : self.enemy_group,
            "crate_group" : self.crate_group,
            "gun_crate_group" : self.gun_crate_group,
            "gun2_pickup_group" : self.gun2_pickup_group,
            "solid_objects_group" : self.solid_objects_group,
            "door_group" : self.door_group,
            "door_lock_group" : self.door_lock_group,
            "boss1_group" : self.boss1_group,
            "table_group" : self.table_group,


        }
