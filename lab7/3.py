import pygame

pygame.init()

size = width, height = (600, 600)

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption(r'PP2/\LAB7/\3.py')

clock = pygame.time.Clock()

color = WHITE

x = 300
y = 300
dx = 0
dy = 0
velocity = 20

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
            dy = 0
            dx = -1 * velocity
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
            dy = 0
            dx = 1 * velocity
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
            dx = 0
            dy = -1 * velocity
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
            dx = 0
            dy = 1 * velocity
        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_RIGHT:
        #     dy = 0
        #     dx = 1 * velocity
        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
        #     dy = 0
        #     dx = -1 * velocity
        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_WHEELDOWN:
        #     dx = 0
        #     dy = 1 * velocity
        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_WHEELUP:
        #     dx = 0
        #     dy = -1 * velocity
    screen.fill(WHITE)
    y += dy
    x += dx
    if x > width-50:
        x = width-50
    if x < 0:
        x = 0
    if y > height-50:
        y = height-50
    if y < 0:
        y = 0
    ellipse = pygame.draw.ellipse(screen, RED, (x, y, 50, 50))
    clock.tick(60)
    pygame.display.update()
pygame.quit()
