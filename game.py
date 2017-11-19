from player import *
from connection.client import Client


HOST = '192.168.1.35'
PORT = 49055

objects = []
players = []
work = True

client = Client(HOST, PORT)

player1 = Player(client.get_self_x0(), client.get_self_y0())
player2 = Player(client.get_opp_x0(), client.get_opp_y0())
print(player1.x, "", player1.y)
print(player2.x, "", player2.y)


players.append(player1)
players.append(player2)

ball = Ball(200, 200)
objects.append(ball)

player1_score = 0
player2_score = 0

timer = pygame.time.Clock()
while work:
    timer.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            work = False
            print(player1_score, " ", player2_score)
            client.stop_connection()

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

    player1.moving(right, left, up, down)
    client.send_x(player1.x)
    client.send_y(player1.y)

    player2.get_x(client.get_opp_x())
    player2.get_y(client.get_opp_y())

    player1.draw(WINDOW)
    player2.draw(WINDOW, YELLOW)


    for obj in objects:
        obj.draw(WINDOW)

    pygame.display.update()

