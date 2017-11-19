from window import *


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = GREEN
        self.ball = pygame.draw.circle(WINDOW, GREEN, (self.x, self.y), self.radius)

    def draw(self, window):
        self.ball = pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

