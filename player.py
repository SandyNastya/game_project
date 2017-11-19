from balls import Ball
from window import *

RADIUS = 30
STEP = 3
left = right = up = down = False

class Player():
#class Player(Ball):
    def __init__(self, x, y, color = RED):
        #Ball.__init__(self, x, y)
        self.x = x
        self.y = y
        self.color = color
        self.radius = RADIUS
        self.figure = pygame.draw.circle(WINDOW, self.color, (self.x, self.y), self.radius)

    def moving(self, right, left, up, down):
        if self.x + self.radius + STEP <= WINDOW_WIDTH:
            if right:
                self.x += STEP
        if self.x - self.radius - STEP >= 0:
            if left:
                self.x -= STEP
        if self.y - self.radius - STEP >= 0:
            if up:
                self.y -= STEP
        if self.y + self.radius + STEP <= WINDOW_HEIGHT:
            if down:
                self.y += STEP

    def send_x(self):
        return self.x

    def send_y(self):
        return self.y

    def get_x(self, x):
        self.x = x

    def get_y(self, y):
        self.y = y

    def draw(self, window, color = RED):
        self.figure = pygame.draw.circle(window, color, (self.x, self.y), self.radius)