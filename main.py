from constants import *
import pygame
import player
import csv
import stone
import dirt
pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))


player_group = pygame.sprite.Group()
stone_group = pygame.sprite.Group()
dirt_group = pygame.sprite.Group()



player = player.Player()




player_group.add(player)



map = []
def get_csv_file_and_put_in_array():
    filename = 'test_map.csv'

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for level in reader:
            map.append(level)



def draw_level():
    get_csv_file_and_put_in_array()
    for row in range(len(map)):
        for col in range(len(map[row])):


            if map[row][col] == "s":
                stone_group.add(stone.Stone(col * BLOCK_SIZE, row * BLOCK_SIZE))


            if map[row][col] == "d":
                dirt_group.add(dirt.Dirt(col * BLOCK_SIZE, row * BLOCK_SIZE))
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
        pygame.display.flip()

    pygame.quit()




def draw():
    surface.fill((200, 200, 200))


    player_group.draw(surface)
    stone_group.draw(surface)
    dirt_group.draw(surface)






def update():
    player_group.update(dirt_group, stone_group)
    stone_group.update()
    dirt_group.update()



if __name__ == "__main__":
    main()
