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
import ammo_pickup
pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
screen_size = pygame.FULLSCREEN
surface = pygame.display.set_mode((0, 0), screen_size)


player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
ammo_pickup_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
crate_group = pygame.sprite.Group()
solid_objects_group = pygame.sprite.Group()
level_transtion_group = pygame.sprite.Group()
make_level_group = pygame.sprite.Group()






map = []

def get_csv_file_and_put_in_array():
    filename = 'start_map.csv'

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for level in reader:
            map.append(level)



def draw_level():

    get_csv_file_and_put_in_array()
    for row in range(len(map)):
        for col in range(len(map[row])):


            if map[row][col] == "s":
                block_group.add(stone.Stone(col * BLOCK_SIZE, row * BLOCK_SIZE))


            if map[row][col] == "m":
                block_group.add(metal.Metal(col * BLOCK_SIZE, row * BLOCK_SIZE))

            if map[row][col] == "e":
                enemy_group.add(henchmen.Henchmen(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

            if map[row][col] == "p":
                player_group.add(player.Player(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

            if map[row][col] == "c":
                crate_group.add(crate.Crate(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))




            col += 1

        row += 1




draw_level()

pygame.init()




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

        draw()
        update()


    pygame.quit()



def draw():
    surface.fill((20, 20, 20))


    player_group.draw(surface)
    ammo_pickup_group.draw(surface)

    bullet_group.draw(surface)
    block_group.draw(surface)
    enemy_group.draw(surface)
    solid_objects_group.draw(surface)

    pygame.display.flip()


def update():
    solid_objects_group.add(block_group , enemy_group, crate_group)
    solid_objects_group.update(solid_objects_group, bullet_group)
    player_group.update(solid_objects_group, bullet_group, ammo_pickup_group)
    block_group.update(solid_objects_group, bullet_group)
    bullet_group.update(solid_objects_group, bullet_group, crate_group, ammo_pickup_group, enemy_group)
    enemy_group.update(solid_objects_group, bullet_group)
    level_transtion_group.update()
    ammo_pickup_group.update()




if __name__ == "__main__":
    main()
