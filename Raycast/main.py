import pygame
from settings import *
from map import Map
from player import Player
from raycaster import Raycaster

screen = pygame.display.set_mode((WINDOW_WIDTH*2, WINDOW_HEIGHT))

map = Map()
player = Player()

clock = pygame.time.Clock()
raycaster = Raycaster(player, map)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    player.update(map)
    raycaster.castAllRays()

    screen.fill((0, 0, 0))

    map.render(screen)
    player.render(screen)

    raycaster.render(screen)
    # pygame.draw.line(
    #     screen,
    #     (50, 50, 50),
    #     (WINDOW_WIDTH, 0),
    #     (WINDOW_WIDTH, WINDOW_HEIGHT)
    # )

    pygame.display.update()