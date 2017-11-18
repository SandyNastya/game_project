from balls import Ball
from window import *


STEP = 3
left = right = up = down = False

class Player(Ball):
    def __init__(self, x, y, color = RED):
        Ball.__init__(self, x, y)
        self.color = color
        self.radius = 30
        self.figure = pygame.draw.circle(WINDOW, self.color, (self.x, self.y), self.radius)

    def moving(self, right, left, up, down):
        if right:
            self.x += STEP
        if left:
            self.x -= STEP
        if up:
            self.y -= STEP
        if down:
            self.y += STEP


    def draw(self, window, color = RED):
        self.figure = pygame.draw.circle(window, color, (self.x, self.y), self.radius)

