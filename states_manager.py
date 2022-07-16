from constants import *
from pygame import mixer
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
import end
import make_level
import groups_man
class States_manager():
    def __init__(self):
        self.groups_manager = groups_man.Groups_man()
        self.states = ["intro", "start", "running", "paused", "dead", "end"]
        self.state = self.states[1]
        self.intro_group = pygame.sprite.Group()
        self.intro_group.add(intro.Intro())

        self.background_image = pygame.image.load("images/floot.png").convert()
        self.pause_image = pygame.image.load("images/pause.png").convert()
        self.start_image = pygame.image.load("images/start.png").convert()

        self.screen_size = pygame.FULLSCREEN
        self.surface = pygame.display.set_mode((0, 0), self.screen_size)


        self.filename = 'start_map.csv'

        self.map = []

        self.ml = make_level.Make_levels()
        self.ml.load_level(self.ml.level_num, self.groups_manager)

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

            if event.type == pygame.KEYUP:
                if event.key == 32:#SPACE
                    if self.state == "start":
                        self.state = "running"


    def draw(self):
        self.surface.fill((100, 100, 100))#background

        if self.state == "intro":
            self.intro_group.draw(self.surface)
        if self.state == "start":
            self.surface.blit(self.start_image, [0, 0])
        if self.state == "running":
            self.surface.blit(self.background_image, [0, 0])

            self.groups_manager.get_drawing_group().draw(self.surface)
        if self.state == "paused":
            self.surface.blit(self.pause_image, [0, 0])
        if self.state == "dead":
            pass

        pygame.display.flip()




    def update(self):
        if self.state == "intro":
            self.intro_group.update(self.state)
        if self.state == "start":
            pass
        if self.state == "running":

            self.groups_manager.update()
            self.ml.lock_door(self.groups_manager, self.state)



        if self.state == "paused":
            pass
        if self.state == "dead":
            pass
        if self.state == "end":
            pass
