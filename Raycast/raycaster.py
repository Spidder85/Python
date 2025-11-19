import pygame
from settings import *
from ray import Ray

class Raycaster:
    def __init__(self, player, map):
        self.rays: Ray = []
        self.player = player
        self.map = map

    def castAllRays(self):
        self.rays = []
        rayAngle = self.player.rotationAngle - FOV / 2
        for i in range(NUM_RAYS):
            ray = Ray(rayAngle, self.player, self.map)
            ray.cast()
            self.rays.append(ray)

            rayAngle += FOV / NUM_RAYS


    def render(self, screen):

        
        step = WINDOW_HEIGHT / 2 / 128
        for i in range(int(WINDOW_HEIGHT / 2), 0, -RES):
            color = int(i * step)
            pygame.draw.rect(
                    screen,
                    (color, color, color),
                    (WINDOW_WIDTH, WINDOW_HEIGHT/2-i, WINDOW_WIDTH, 2*i))

        i = 0
        for ray in self.rays:
            ray.render(screen)

            line_height = (32 / ray.distance) * 415

            draw_begin = int(WINDOW_HEIGHT / 2 - line_height / 2)
            draw_end = line_height

            x = WINDOW_WIDTH + i * RES
            pygame.draw.rect(
                screen,
                (ray.color, ray.color, ray.color),
                (x, draw_begin, RES, draw_end))

            i += 1