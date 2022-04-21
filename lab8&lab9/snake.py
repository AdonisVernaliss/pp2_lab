import pygame
import random

pygame.init()
size = 600
Snake_size = 25
x, y = random.randrange(0, size, Snake_size), random.randrange(0, size, Snake_size)
apple = random.randrange(0, size, Snake_size), random.randrange(0, size, Snake_size)
bomb = random.randrange(0, size, Snake_size), random.randrange(0, size, Snake_size)
BOMB = pygame.USEREVENT + 1
APPLE = pygame.USEREVENT + 1
lenght = 1
score = 0
level = 0
snake = [(x, y)]
FPS = 10
dx, dy = 0, 0
pygame.mixer.music.load('snake.mp3')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode([size, size])
clock = pygame.time.Clock()
font_of_score = pygame.font.SysFont('Aarial', 22, bold=True)
font_of_level = pygame.font.SysFont('Aarial', 22, bold=True)
font_of_end = pygame.font.SysFont('Aarial', 70, bold=True)

pygame.time.set_timer(BOMB, 3000)
pygame.time.set_timer(APPLE, 5000)

while True:
    screen.fill(pygame.Color('black'))

    [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, Snake_size - 2, Snake_size - 2))) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, Snake_size, Snake_size))
    pygame.draw.rect(screen, pygame.Color('yellow'), (*bomb, Snake_size, Snake_size))
    render_score = font_of_score.render(f'Sc0re: {score}', True, pygame.Color('yellow'))
    render_level = font_of_level.render(f'Level: {level}', True, pygame.Color('yellow'))
    screen.blit(render_score, (5, 5))
    screen.blit(render_level, (5, 20))
    x += dx * Snake_size
    y += dy * Snake_size
    snake.append((x, y))
    snake = snake[-lenght:]

    if snake[-1] == apple:
        apple = random.randrange(0, size, Snake_size), random.randrange(0, size, Snake_size)
        lenght += 1
        FPS += 0.3
        score += 1
        if score % 3 == 0:
            level += 1
            l = [i for i in range(5, 100, 2)]
            for i in l:
                if level == i:
                    FPS += 3.5

    if snake[-1] == bomb:
        while True:
            render_end = font_of_end.render('GAME OVER', 1, pygame.Color('yellow'))
            screen.blit(render_end, (size // 2 - 150, size // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    if (x < 0 or x > size - Snake_size or y < 0 or y > size - Snake_size) or (len(snake) != len(set(snake))):
        while True:
            render_end = font_of_end.render('GAME OVER', True, pygame.Color('yellow'))
            screen.blit(render_end, (size // 2 - 150, size // 3))
            pygame.display.flip()
            pygame.mixer.music.stop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    # if x < 0: x = size
    # if x > size: x = -Snake_size
    # if y < 0: y = size
    # if y > size: y = -Snake_size
    # if len(snake) != len(set(snake)):
    #     while True:
    #         render_end = font_of_end.render('GAME OVER', 1, pygame.Color('yellow'))
    #         screen.blit(render_end, (size // 2 - 150, size // 3))
    #         pygame.display.flip()
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 exit()
    pygame.display.flip()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == BOMB:
            bomb = random.randrange(0, size, Snake_size), random.randrange(0, size, Snake_size)
        if event.type == APPLE:
            apple = random.randrange(0, size, Snake_size), random.randrange(0, size, Snake_size)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and dx != -1:
                dx, dy = 1, 0
            if event.key == pygame.K_LEFT and dx != 1:
                dx, dy = -1, 0
            if event.key == pygame.K_UP and dy != 1:
                dx, dy = 0, -1
            if event.key == pygame.K_DOWN and dy != -1:
                dx, dy = 0, 1
            #
            if event.key == pygame.K_d and dx != -1:
                dx, dy = 1, 0
            if event.key == pygame.K_a and dx != 1:
                dx, dy = -1, 0
            if event.key == pygame.K_w and dy != 1:
                dx, dy = 0, -1
            if event.key == pygame.K_s and dy != -1:
                dx, dy = 0, 1
