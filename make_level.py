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

        self.level = LEVELS

        self.level_num = 0

        # self.load_level(self.level_num)







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

    def load_level(self, level, main_group):
        block_group = main_group.block_group
        enemy_group = main_group.enemy_group
        player_group = main_group.player_group
        door_group = main_group.door_group
        crate_group = main_group.crate_group
        gun_crate_group = main_group.gun_crate_group
        boss1_group = main_group.boss1_group
        bullet_group = main_group.bullet_group
        ammo_pickup_group = main_group.ammo_pickup_group
        gun2_pickup_group = main_group.gun2_pickup_group
        solid_objects_group = main_group.solid_objects_group
        player_group.empty()
        bullet_group.empty()
        ammo_pickup_group.empty()
        block_group.empty()
        enemy_group.empty()
        crate_group.empty()
        gun_crate_group.empty()
        gun2_pickup_group.empty()
        solid_objects_group.empty()
        door_group.empty()
        boss1_group.empty()


        map_tiles = self.get_list(self.level[level])
        for row in range(len(map_tiles)):
            for col in range(len(map_tiles[row])):
                item = map_tiles[row][col]


                if item == "s":
                    block_group.add(stone.Stone(col * BLOCK_SIZE, row * BLOCK_SIZE))


                if item == "m":
                    block_group.add(metal.Metal(col * BLOCK_SIZE, row * BLOCK_SIZE))

                if item == "e":
                    enemy_group.add(henchmen.Henchmen(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "p":

                    player_group.add(player.Player(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "c":
                    crate_group.add(crate.Crate(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "g":
                    gun_crate_group.add(gun_crate.Gun_crate(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "d":
                    door_group.add(door.Door(col * BLOCK_SIZE, row * BLOCK_SIZE))

                if item == "b1":
                    boss1_group.add(boss1.Boss1(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))



    def clear_level(self, main_group):
        block_group = main_group.block_group
        enemy_group = main_group.enemy_group
        player_group = main_group.player_group
        door_group = main_group.door_group
        crate_group = main_group.crate_group
        gun_crate_group = main_group.gun_crate_group
        boss1_group = main_group.boss1_group
        bullet_group = main_group.bullet_group
        ammo_pickup_group = main_group.ammo_pickup_group
        gun2_pickup_group = main_group.gun2_pickup_group
        solid_objects_group = main_group.solid_objects_group

        player_group.empty()
        bullet_group.empty()
        ammo_pickup_group.empty()
        block_group.empty()
        enemy_group.empty()
        crate_group.empty()
        gun_crate_group.empty()
        gun2_pickup_group.empty()
        solid_objects_group.empty()
        door_group.empty()
        self.load_level(self.level_num, main_group)

    def collide_door(self, main_group):
        player_group = main_group.player_group
        door_group = main_group.door_group
        if pygame.sprite.groupcollide(player_group, door_group, False, False):

            self.level_num = self.level_num + 1
            self.clear_level(main_group)
