import pygame
from color import *
import time
from balls import Ball


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
NUM_OF_BALLS = 10
WINDOW_COLOR = BLACK


pygame.init()
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('WHO IS FASTER')

def main_menu(screen):
    done = False
    menu_time = time.time()
    while done == False:
        current_time = time.time()
        if current_time - menu_time >= 5:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(WHITE)
        game_nameFontObj = pygame.font.Font(None, 90)
        game_name = game_nameFontObj.render("WHO IS FASTER", True, BLACK)
        game_nameRectObj = game_name.get_rect()
        game_nameRectObj.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT * 0.25)
        screen.blit(game_name, game_nameRectObj)

        instructionFontObj = pygame.font.Font(None, 30)
        instruction = instructionFontObj.render("Collect green circles more than your friend".upper(), True, BLACK)
        instructionRectObj = instruction.get_rect()
        instructionRectObj.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT * 0.75)
        screen.blit(instruction, instructionRectObj)

        pygame.display.flip()

def winner(winner):
    screen = pygame.display.get_surface()
    done = False
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
        screen.fill(WHITE)
        winnerFontObj = pygame.font.Font(None, 90)
        winner_name = winnerFontObj.render(winner, True, BLACK)
        winner_nameRectObj = winner_name.get_rect()
        winner_nameRectObj.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT * 0.5)
        screen.blit(winner_name, winner_nameRectObj)

        pygame.display.flip()

def balls_generation():
    points = []
    x_vals = [200, 350, 400, 550, 700]
    y_vals = [100, 150, 300, 450, 500]
    for i in range(len(x_vals)):
        point = Ball(x_vals[i], y_vals[i])
        points.append(point)
    return points

