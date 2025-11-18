import math, pygame

def normalizeAngle(angle):
    angle %= 2 * math.pi
    if angle < 0:
        angle += 2 * math.pi
    return angle

class Ray:
    def __init__(self, angle, player):
        self.rayAngle = normalizeAngle(angle)
        self.player = player

    def cast(self):
        pass

    def render(self, screen):
        pygame.draw.line(screen, (255, 0, 0), (self.player.x, self.player.y), (self.player.x + math.cos(self.rayAngle) *
                                                                              50, self.player.y + math.sin(self.rayAngle) * 50))