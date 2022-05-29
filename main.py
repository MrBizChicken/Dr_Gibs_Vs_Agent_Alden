from constants import *
import pygame
import player
import csv
import stone
import metal
import bullet
import enemy
import level_transtion
pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))


player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
level_transtion_group = pygame.sprite.Group()

player = player.Player()


player_group.add(player)



map = []
filename = 'test_map.csv'
def get_csv_file_and_put_in_array():


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
                enemy_group.add(enemy.Enemy(col * BLOCK_SIZE, row * BLOCK_SIZE))

            if map[row][col] == "2":
                level_transtion_group.add(level_transtion.Level_transtion(col * BLOCK_SIZE, row * BLOCK_SIZE))

            # if  pygame.Rect.colliderect(player.rect, level_transtion.Level_transtion(col, row).rect):
            #     filename = "next_level.csv"
            #     print("TRUE")


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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_e:
                    bullet_group.add(bullet.Bullet(player.rect.x - 20, player.rect.y - 4, player.pd))



        draw()
        update()
        pygame.display.flip()

    pygame.quit()




def draw():
    surface.fill((200, 200, 200))


    player_group.draw(surface)
    bullet_group.draw(surface)
    block_group.draw(surface)
    enemy_group.draw(surface)
    level_transtion_group.draw(surface)






def update():
    player_group.update(block_group)
    block_group.update()
    bullet_group.update(block_group)
    enemy_group.update(block_group)
    level_transtion_group.update()


if __name__ == "__main__":
    main()
