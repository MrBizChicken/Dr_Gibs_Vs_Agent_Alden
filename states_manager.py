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
        self.states = ["intro", "start", "running", "paused", "dead", "game_over"]
        self.state = self.states[2]
        self.intro_group = pygame.sprite.Group()
        self.intro_group.add(intro.Intro())
        self.surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))


        self.filename = 'start_map.csv'

        self.map = []

        self.ml = make_level.Make_levels()
        self.ml.load_level(self.ml.level_num, self.groups_manager)
        self.pause_image = pygame.image.load("images/pause.png")
        self.start_image = pygame.image.load("images/start.png")
        self.game_over_image = pygame.image.load("images/game_over.png")
        self.background_image = pygame.image.load("images/floot.png")



    def events(self):


        events = pygame.event.get()
        # self.is_intro_fin()
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

            if event.type == pygame.KEYUP:
                if event.key == 32:#SPACE
                    if self.state == "dead":
                        self.state = "start"




    def draw(self):
        self.surface.fill((100, 100, 100))#background
        font = pygame.font.Font('freesansbold.ttf', 32)
        for p in self.groups_manager.player_group:
            text = font.render(f"HEALTH: {p.health}|AMMO: {p.ammo}", True, BLACK, WHITE)

        textRect = text.get_rect()


        textRect.center = (GAME_WIDTH - 200 , 15)


        if not self.groups_manager.player_group:
            self.state = "dead"


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
            self.surface.blit(self.game_over_image, [0, 0])

        if self.state == "end":
            self.surface.blit(self.end_image, [0, 0])
        self.surface.blit(text, textRect)



        pygame.display.flip()




    def update(self):


        if self.state == "intro":
            self.intro_group.update()


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

    # def is_intro_fin(self):
    #     print(intro.Intro().is_intro_fin)
    #
    #     if intro.Intro().frame == intro.Intro().max_frame:
    #
    #         self.state = "start"
    #         print("hello")
