from player import *
from connection.server import Server
from balls import Ball
from window import *



HOST = '192.168.1.35'
PORT = 49055

objects = balls_generation()
players = []


server = Server(HOST, PORT)

player1 = Player(RADIUS, RADIUS)
player2 = Player(WINDOW_WIDTH - RADIUS, WINDOW_HEIGHT - RADIUS)
print(player1.x, "", player1.y)
print(player2.x, "", player2.y)


players.append(player1)
players.append(player2)

player1_score = 0
player2_score = 0

main_menu(WINDOW)

timer = pygame.time.Clock()
work = True
while work:
    timer.tick(60)
    server.check_state(work)
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            work = False
            server.check_state(work)
            print(player1_score, " ", player2_score)
            server.stop_connection()

        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            right = True
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            right = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            left = True
        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            left = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            up = True
        if e.type == pygame.KEYUP and e.key == pygame.K_UP:
            up = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
            down = True
        if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
            down = False

    for pl in players:
        for obj in objects:
            if pl.figure.contains(obj.ball):
                objects.remove(obj)
                if pl == player1:
                    player1_score += 1
                else:
                    player2_score += 1

    player1.draw(WINDOW, WINDOW_COLOR)
    player2.draw(WINDOW, WINDOW_COLOR)

    for point in objects:
        point.draw(WINDOW)

    player1.moving(right, left, up, down)
    server.send_cur_xpos(player1.x)
    server.send_cur_ypos(player1.y)

    player2.get_x(server.get_cur_opp_xpos())
    player2.get_y(server.get_cur_opp_ypos())

    player1.draw(WINDOW)
    player2.draw(WINDOW, YELLOW)

    pygame.display.update()

if player1_score > player2_score:
    winner("YOU WIN")
else:
    winner("YOU LOSE")