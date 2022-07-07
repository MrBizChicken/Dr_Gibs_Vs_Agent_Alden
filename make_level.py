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
import door_lock
import boss1
import telepotation_device
import table
import end


class Make_levels():
    def __init__(self):

        self.level = LEVELS

        self.level_num = 0
        self.end_group = pygame.sprite.Group()
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
        door_lock_group = main_group.door_lock_group
        crate_group = main_group.crate_group
        gun_crate_group = main_group.gun_crate_group
        boss1_group = main_group.boss1_group
        bullet_group = main_group.bullet_group
        ammo_pickup_group = main_group.ammo_pickup_group
        gun2_pickup_group = main_group.gun2_pickup_group
        solid_objects_group = main_group.solid_objects_group
        table_group = main_group.table_group
        tp_group = main_group.tp_group
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
        table_group.empty()
        tp_group.empty()


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

                if item == "l":
                    door_lock_group.add(door_lock.Door_lock(col * BLOCK_SIZE, row * BLOCK_SIZE))

                if item == "b1":
                    boss1_group.add(boss1.Boss1(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


                if item == "t":
                    table_group.add(table.Table(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "tp":
                    tp_group.add(telepotation_device.Tp(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))




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
        table_group = main_group.table_group
        tp_group = main_group.tp_group


        player_group.empty()
        table_group.empty()
        tp_group.empty()

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

    def lock_door(self, main_group, state):
        player_group = main_group.player_group
        door_group = main_group.door_group
        enemy_group = main_group.enemy_group
        solid_objects_group = main_group.enemy_group
        door_lock_group = main_group.door_lock_group

        if self.level_num == 9:


            state = state[2]
        if state == "end":

            self.end_group.add(end.End())

            self.end_group.draw(self.surface)


        elif pygame.sprite.groupcollide(player_group, door_group, False, False):


            self.level_num = self.level_num + 1
            can_go_through_door = False
            self.clear_level(main_group)


        if pygame.sprite.groupcollide(player_group, enemy_group, False, False):


            for p in player_group:
                p.hurt()
        if not enemy_group:
            for l in door_lock_group:
                l.kill()
