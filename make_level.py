from constants import *
import pygame
import csv
import stone
import player
import henchmen
import metal
import bullet
import make_level
import crate
import gun_crate
import ammo_pickup
import gun2_pickup
import door
import boss1


class Make_levels():
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

        self.map = []
        self.level = LEVELS

        self.level_num = 0

        self.load_level(self.level_num)

                # if pygame.sprite.groupcollide(self.player_group, self.door_group, False, False):
                #
                #     self.level_num = self.level_num + 1
                #     self.clear_level()


    def clear_level(self):
        self.player_group.empty()
        self.bullet_group.empty()
        self.ammo_pickup_group.empty()
        self.block_group.empty()
        self.enemy_group.empty()
        self.crate_group.empty()
        self.gun_crate_group.empty()
        self.gun2_pickup_group.empty()
        self.solid_objects_group.empty()
        self.door_group.empty()
        self.boss1_group.empty()
        self.load_level(self.level_num)



    def get_list(self, level):
        map_list = ""

        with open(level) as file:
            map_list = file.read().split("\n")
        # filter out all "#" and empty strings
        map_list = list(filter(self.is_comment, map_list))

        #finally split by csv
        for m in range(len(map_list)):
            map_list[m] = map_list[m].split(",")

        return map_list

    # filters out comments and blank strings
    def is_comment(self, string):
        if not string:
            return False
        if string[0] == "#":
            return False
        return True

    def load_level(self, level):
        self.player_group.empty()
        self.bullet_group.empty()
        self.ammo_pickup_group.empty()
        self.block_group.empty()
        self.enemy_group.empty()
        self.crate_group.empty()
        self.gun_crate_group.empty()
        self.gun2_pickup_group.empty()
        self.solid_objects_group.empty()
        self.door_group.empty()
        self.boss1_group.empty()

        map_tiles = self.get_list(self.level[level])
        for row in range(len(map_tiles)):
            for col in range(len(map_tiles[row])):
                item = map_tiles[row][col]


                if item == "s":
                    self.block_group.add(stone.Stone(col * BLOCK_SIZE, row * BLOCK_SIZE))


                if item == "m":
                    self.block_group.add(metal.Metal(col * BLOCK_SIZE, row * BLOCK_SIZE))

                if item == "e":
                    self.enemy_group.add(henchmen.Henchmen(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "p":
                    self.player_group.add(player.Player(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "c":
                    self.crate_group.add(crate.Crate(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "g":
                    self.gun_crate_group.add(gun_crate.Gun_crate(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "d":
                    self.door_group.add(door.Door(col * BLOCK_SIZE, row * BLOCK_SIZE))

                if item == "b1":
                    self.boss1_group.add(boss1.Boss1(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
