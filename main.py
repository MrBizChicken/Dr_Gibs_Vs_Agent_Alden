from constants import *
import pygame
import states_manager




def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    screen_size = pygame.FULLSCREEN
    surface = pygame.display.set_mode((COLS * BLOCK_SIZE, ROWS * BLOCK_SIZE))

    states_manager_obj = states_manager.States_manager()


    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()



        states_manager_obj.draw()
        states_manager_obj.events()
        states_manager_obj.update()




    pygame.quit()

if __name__ == "__main__":
    main()
