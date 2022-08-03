import pygame
from constants import *
class Intro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        self.spritesheet = pygame.image.load("images/intro.png").convert()
        self.y_sprite_sheet_index = 0

        self.image = pygame.Surface((256, 256))
        self.image = self.get_image_from_sprite_sheet(0, self.y_sprite_sheet_index)
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (0, 0)

        self.frame = 0
        self.max_frame = 4
        self.next_frame_timer = pygame.time.get_ticks()
        self.frame_timer_limit = 1000
        self.fin = False

    def update(self):
        if pygame.time.get_ticks() >= self.next_frame_timer + self.frame_timer_limit:
            self.next_frame_timer = pygame.time.get_ticks()
            self.frame += 1
            self.image = self.get_image_from_sprite_sheet(0, self.frame * 1000)
            if self.frame == self.max_frame:
                self.is_intro_fin
    def is_intro_fin(self):
        return True






    def get_image_from_sprite_sheet(self, row, col):
        image = pygame.Surface((1300, 1000))
        image.blit(self.spritesheet, (0, 0), (row, col, 1300, 1000))
        #image.set_colorkey()
        return image
