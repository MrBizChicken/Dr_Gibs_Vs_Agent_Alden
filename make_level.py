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
pygame.init()

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
        self.boss1_group = pygame.sprite.Group()
        self.spritesheet = pygame.image.load(SPRITESHEET).convert()
        self.y_sprite_sheet_index = 0
        self.frame = 0
        self.max_frame = (self.spritesheet.get_width() // BLOCK_SIZE) - 1

        self.screen_size = pygame.FULLSCREEN
        self.surface = pygame.display.set_mode((0, 0), self.screen_size)
        self.map = []
        self.level = ["LEVEL1.csv", "LEVEL2.csv", "LEVEL3.csv", "LEVEL4.csv", "LEVEL5.csv", "LEVEL6.csv", "LEVEL7.csv", "LEVEL8.csv", "LEVEL9.csv", "LEVEL10.csv", "LEVEL11.csv", "LEVEL12.csv"]
        self.image = self.get_image_from_sprite_sheet(0, self.y_sprite_sheet_index)

        self.speed = 0.1


        self.level_num = 0
        self.states = ["story", "start", "running", "paused"]
        self.state = self.states[0]
        self.running = True
        self.load_level(self.level_num)
        self.background_image0 = pygame.image.load("0.png").convert()
        self.background_image1 = pygame.image.load("1.png").convert()
        self.background_image2 = pygame.image.load("2.png").convert()
        self.background_image3 = pygame.image.load("3.png").convert()
        self.background_image4 = pygame.image.load("2.png").convert()
        self.wait = 3000
        self.timer = pygame.time.get_ticks()









    def events(self):

        events = pygame.event.get()

        for event in events:
            # if event.type == pygame.QUIT:
            #     self.running = False

            #Keyboard
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                #used to kill outside loop
                if event.key == pygame.K_q:
                    return True




                if event.key == pygame.K_p:

                    if self.state == "paused" and event.key == pygame.K_p:
                        self.state = "running"
                    else:
                        self.state = "paused"


                if event.key == pygame.K_l:#SPACE
                    if self.state == "start":
                        self.state = "running"
                        print("start")

                if pygame.sprite.groupcollide(self.player_group, self.door_group, False, False):

                    self.level_num = self.level_num + 1
                    self.clear_level()


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






    def draw(self):
        self.surface.fill((20, 20, 20))






        if self.state == "start":


            if self.state == "story":
                self.surface.blit(self.image, [0, 0])
                # return image
                # self.frame += self.speed
                #
                # if self.frame > self.max_frame:
                #     self.frame = 0
                #
                # self.image = self.get_image_from_sprite_sheet(0, round(0) * 256)
                #






        elif self.state == "running":


            self.player_group.draw(self.surface)

            self.ammo_pickup_group.draw(self.surface)

            self.gun2_pickup_group.draw(self.surface)

            self.bullet_group.draw(self.surface)

            self.block_group.draw(self.surface)

            self.enemy_group.draw(self.surface)

            self.solid_objects_group.draw(self.surface)

            self.door_group.draw(self.surface)

            self.boss1_group.draw(self.surface)

        elif self.state == "paused":
            self.surface.fill((255, 100, 100))#background


        pygame.display.flip()


    def update(self):

        if self.state == "start":
            pass

        if self.state == "story":
            pass


        elif self.state == "running":
            self.solid_objects_group.add(self.block_group , self.enemy_group, self.crate_group, self.gun_crate_group)
            self.solid_objects_group.update(self.solid_objects_group, self.bullet_group, self.player_group)
            self.crate_group.update(self.solid_objects_group, self.bullet_group, self.player_group)
            self.gun_crate_group.update(self.solid_objects_group, self.player_group, self.bullet_group)
            self.player_group.update(self.solid_objects_group, self.bullet_group, self.ammo_pickup_group, self.gun2_pickup_group, self.player_group)
            self.block_group.update(self.solid_objects_group, self.bullet_group, self.player_group)
            self.bullet_group.update(self.solid_objects_group, self.bullet_group, self.crate_group, self.ammo_pickup_group, self.enemy_group, self.gun_crate_group, self.gun2_pickup_group, self.player_group, self.boss1_group)
            self.enemy_group.update(self.solid_objects_group, self.bullet_group, self.player_group)
            self.ammo_pickup_group.update()
            self.gun2_pickup_group.update()
            self.boss1_group.update(self.solid_objects_group, self.bullet_group, self.player_group)



        elif self.state == "paused":
            pass
