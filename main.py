from constants import *
import pygame
import make_level
pygame.init()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
make_level = make_level.Make_levels()

def main():
    level = 0
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()



        make_level.draw()
        make_level.events()
        make_level.update()




    pygame.quit()

if __name__ == "__main__":
    main()
