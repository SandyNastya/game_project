from player import  *
from connection.client import Client


HOST = '172.20.10.2'
PORT = 49055

objects = []
players = []
work = True

#client = Client(HOST, PORT)

player1 = Player(100, 100)
player2 = Player(500, 500, YELLOW)

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
    player1.moving(right, left, up, down)
    player2.get_x(500)
    player2.get_y(500)

    player1.draw(WINDOW)
    player2.draw(WINDOW)


    for obj in objects:
        obj.draw(WINDOW)

    pygame.display.update()

