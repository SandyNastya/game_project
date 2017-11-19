from balls import Ball
from window import *


STEP = 3
left = right = up = down = False
YELLOW = (255, 255, 0)

class Player():
#class Player(Ball):
    def __init__(self, x, y, color = RED):
        #Ball.__init__(self, x, y)
        self.x = x
        self.y = y
        self.color = color
        self.radius = 30
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
        #print(self.x, " ", self.y)

    def send_x(self):
        return self.figure.x

    def send_y(self):
        return self.figure.y

    def get_x(self, x):
        self.x = x

    def get_y(self, y):
        self.y = y

    def draw(self, window, color = RED):
        self.figure = pygame.draw.circle(window, color, (self.x, self.y), self.radius)

    def draw_opponent(self, window, color = YELLOW):
        self.figure = pygame.draw.circle(window, color, (self.x, self.y), self.radius)
