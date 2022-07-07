import pygame
from constants import *
class End(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        self.image = pygame.image.load("images/end.png")
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (0, 0)

        pygame.mixer.music.load("end.mp3")
        pygame.mixer.music.play(0)
