from player import  *

SPEED = 20
objects = []
work = True

pygame.init()
pygame.display.set_caption('GAME')
player1 = Player(100, 100)
objects.append(player1)
ball = Ball(200, 200)
objects.append(ball)

timer = pygame.time.Clock()
while work:
    timer.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            work = False

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

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        right = True
    if key[pygame.K_LEFT]:
        left = True
    if key[pygame.K_UP]:
        up = True
    if key[pygame.K_DOWN]:
        down = True

    player1.draw(WINDOW, WINDOW_COLOR)
    player1.moving(right, left, up, down)
    for obj in objects:
        obj.draw(WINDOW, RED)
    pygame.display.update()

