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
import make_level
import groups_man
class States_manager():
    def __init__(self):
        self.groups_manager = groups_man.Groups_man()
        self.states = ["intro", "start", "running", "paused", "dead", "game_over"]
        self.state = self.states[2]
        self.intro_group = pygame.sprite.Group()
        self.intro_group.add(intro.Intro())

        self.surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))


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


    def draw(self):
        self.surface.fill((100, 100, 100))#background

        if self.state == "intro":
            self.intro_group.draw(self.surface)
        if self.state == "start":
            self.surface.fill((63, 23, 76))
        if self.state == "running":
            self.groups_manager.get_drawing_group().draw(self.surface)
            make_level.Make_levels().load_level(make_level.Make_levels().level_num, self.groups_manager)
        if self.state == "paused":
            self.surface.fill((8, 98, 23))
        if self.state == "dead":
            pass
        if self.state == "game_over":
            pass

        pygame.display.flip()



    def update(self):
        if self.state == "intro":
            self.intro_group.update(self.state)
        if self.state == "start":
            pass
        if self.state == "running":
            self.groups_manager.update()


        if self.state == "paused":
            pass
        if self.state == "dead":
            pass
        if self.state == "game_over":
            pass
