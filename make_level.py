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

class Make_levels(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
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

        self.filename = "LEVEL1.csv"
        self.screen_size = pygame.FULLSCREEN
        self.surface = pygame.display.set_mode((0, 0), self.screen_size)
        self.map = []
        self.level = ["LEVEL1.csv", "LEVEL2.csv", "LEVEL3.csv"]
        self.level_num = 1

        self.load_level(0)

    # def change_level(self):
    #     if self.level == 2:
    #         self.filename = "LEVEL2.csv"





    def get_list(self, level):
        map_list = ""
        # reads the file and splits every new line into a list
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



    #
    #
    #
    #
    #
    #
    #
    # def draw_level(self):
    #
    #
    #     with open(self.filename, 'r') as csvfile:
    #         reader = csv.reader(csvfile)
    #         for level in reader:
    #             self.map.append(level)
    #
    #     for row in range(len(self.map)):
    #         for col in range(len(self.map[row])):
    #
    #
    #             if self.map[row][col] == "s":
    #                 self.block_group.add(stone.Stone(col * BLOCK_SIZE, row * BLOCK_SIZE))
    #
    #
    #             if self.map[row][col] == "m":
    #                 self.block_group.add(metal.Metal(col * BLOCK_SIZE, row * BLOCK_SIZE))
    #
    #             if self.map[row][col] == "e":
    #                 self.enemy_group.add(henchmen.Henchmen(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    #
    #             if self.map[row][col] == "p":
    #                 self.player_group.add(player.Player(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    #
    #             if self.map[row][col] == "c":
    #                 self.crate_group.add(crate.Crate(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    #
    #             if self.map[row][col] == "g":
    #                 self.gun_crate_group.add(gun_crate.Gun_crate(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    #
    #             if self.map[row][col] == "d":
    #                 self.door_group.add(door.Door(col * BLOCK_SIZE, row * BLOCK_SIZE))
    #
    #
    #
    #             col += 1
    #
    #         row += 1
    #




    def draw(self):
        self.surface.fill((20, 20, 20))

        self.player_group.draw(self.surface)

        self.ammo_pickup_group.draw(self.surface)

        self.gun2_pickup_group.draw(self.surface)

        self.bullet_group.draw(self.surface)

        self.block_group.draw(self.surface)

        self.enemy_group.draw(self.surface)

        self.solid_objects_group.draw(self.surface)

        self.door_group.draw(self.surface)

        pygame.display.flip()




    def update(self):
        self.solid_objects_group.add(self.block_group , self.enemy_group, self.crate_group, self.gun_crate_group)

        self.solid_objects_group.update(self.solid_objects_group, self.bullet_group, self.player_group)

        self.crate_group.update(self.solid_objects_group, self.bullet_group, self.player_group)

        self.gun_crate_group.update(self.solid_objects_group, self.player_group, self.bullet_group)

        self.player_group.update(self.solid_objects_group, self.bullet_group, self.ammo_pickup_group, self.gun2_pickup_group, self.player_group)

        self.block_group.update(self.solid_objects_group, self.bullet_group, self.player_group)

        self.bullet_group.update(self.solid_objects_group, self.bullet_group, self.crate_group, self.ammo_pickup_group, self.enemy_group, self.gun_crate_group, self.gun2_pickup_group, self.player_group)

        self.enemy_group.update(self.solid_objects_group, self.bullet_group, self.player_group)

        self.ammo_pickup_group.update()

        self.gun2_pickup_group.update()
