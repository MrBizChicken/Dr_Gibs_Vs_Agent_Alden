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
import intro

class States_manager():
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
        self.states = ["intro", "start", "running", "paused", "dead", "game_over"]
        self.state = self.states[0]
        self.intro_group = pygame.sprite.Group()
        self.intro_group.add(intro.Intro())


        self.filename = 'start_map.csv'

        self.map = []


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


    def draw(self, surface):
        surface.fill((100, 100, 100))#background

        if self.state == "intro":
            self.draw_intro_state(surface)
        elif self.state == "start":
            pass
        elif self.state == "running":
            self.draw_running_state(surface)
        elif self.state == "paused":
            pass
        elif self.state == "dead":
            pass
        elif self.state == "game_over":
            pass

        pygame.display.flip()



    def update(self):
        if self.state == "intro":
            self.update_intro_state()
        elif self.state == "start":
            pass
        elif self.state == "running":
            self.update_running_state()
        elif self.state == "paused":
            pass
        elif self.state == "dead":
            pass
        elif self.state == "game_over":
            pass



    def draw_intro_state(self, surface):
        self.intro_group.draw(surface)

    def update_intro_state(self):
        self.intro_group.update(self.state)




    def draw_running_state(self):
        self.player_group.draw(self.surface)
        self.ammo_pickup_group.draw(self.surface)
        self.gun2_pickup_group.draw(self.surface)
        self.bullet_group.draw(self.surface)
        self.block_group.draw(self.surface)
        self.enemy_group.draw(self.surface)
        self.solid_objects_group.draw(self.surface)
        self.door_group.draw(self.surface)

    def update_running_state(self):
        self.solid_objects_group.add(self.block_group , self.enemy_group, self.crate_group, self.gun_crate_group)
        self.solid_objects_group.update(self.solid_objects_group, self.bullet_group, self.player_group)
        self.crate_group.update(self.solid_objects_group, self.bullet_group, self.player_group)
        self.gun_crate_group.update(self.solid_objects_group, self.player_group, self.bullet_group)
        self.player_group.update(self.solid_objects_group, self.bullet_group, self.ammo_pickup_group, self.gun2_pickup_group, self.player_group)
        self.block_group.update(self.solid_objects_group, self.bullet_group, self.player_group)
        self.bullet_group.update(self.solid_objects_group, self.bullet_group, self.crate_group, self.ammo_pickup_group, self.enemy_group, self.gun_crate_group, self.gun2_pickup_group, self.player_group)
        self.enemy_group.update(self.solid_objects_group, self.bullet_group, self.player_group)
        self.level_transtion_group.update()
        self.ammo_pickup_group.update()
        self.gun2_pickup_group.update()
