from constants import *
import pygame
import make_level

pygame.init()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
make_level = make_level.Make_levels()

def main():
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_f:
                    make_level.load_level(1)


        make_level.draw()
        make_level.update()

def load_level(self, level):
    make_level.player_group.empty()
    make_level.bullet_group.empty()
    make_level.ammo_pickup_group.empty()
    make_level.block_group.empty()
    make_level.enemy_group.empty()
    make_level.crate_group.empty()
    make_level.gun_crate_group.empty()
    make_level.gun2_pickup_group.empty()
    make_level.solid_objects_group.empty()
    make_level.door_group.empty()
    make_level.load_level(level)


    pygame.quit()

if __name__ == "__main__":
    main()
