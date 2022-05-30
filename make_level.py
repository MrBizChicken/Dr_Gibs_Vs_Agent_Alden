# from constants import *
# import pygame
# import csv
#
# pygame.init()
#
#
# player_group = pygame.sprite.Group()
# bullet_group = pygame.sprite.Group()
# block_group = pygame.sprite.Group()
# enemy_group = pygame.sprite.Group()
# solid_objects_group = pygame.sprite.Group()
# level_transtion_group = pygame.sprite.Group()
# make_level_group = pygame.sprite.Group()
#
#
#
# make_level_group.add(make_level.Make_level())
#
#
#
# map = []
#
# def get_csv_file_and_put_in_array():
#     filename = 'start_map.csv'
#
#     with open(filename, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         for level in reader:
#             map.append(level)
#
#
#
# def draw_level():
#
#     get_csv_file_and_put_in_array()
#     for row in range(len(map)):
#         for col in range(len(map[row])):
#
#
#             if map[row][col] == "s":
#                 block_group.add(stone.Stone(col * BLOCK_SIZE, row * BLOCK_SIZE))
#
#
#             if map[row][col] == "m":
#                 block_group.add(metal.Metal(col * BLOCK_SIZE, row * BLOCK_SIZE))
#
#             if map[row][col] == "e":
#                 enemy_group.add(henchmen.Henchmen(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
#
#             if map[row][col] == "p":
#                 player_group.add(player.Player(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
#
#
#
#             col += 1
#
#         row += 1
#
#
#
#
# draw_level()
#
# pygame.init()
#
#
#
# git
# def main():
#
#
#     running = True
#
#     while running:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#
#             if event.type == pygame.QUIT:
#                 running = False
#
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_q:
#                     pygame.quit()
#
#         draw()
#         update()
#
#
#     pygame.quit()
#
#
#
# def draw():
#     surface.fill((20, 20, 20))
#
#
#     player_group.draw(surface)
#     bullet_group.draw(surface)
#     block_group.draw(surface)
#     enemy_group.draw(surface)
#     solid_objects_group.draw(surface)
#     level_transtion_group.draw(surface)
#
#     pygame.display.flip()
#
#
# def update():
#     solid_objects_group.add(block_group , enemy_group)
#     solid_objects_group.update(solid_objects_group, bullet_group)
#     player_group.update(solid_objects_group, bullet_group)
#     block_group.update(solid_objects_group, bullet_group)
#     bullet_group.update(solid_objects_group, bullet_group)
#     enemy_group.update(solid_objects_group, bullet_group)
#     level_transtion_group.update()
#     make_level_group(block_group, enemy_group, player_group, level_transtion_group)
