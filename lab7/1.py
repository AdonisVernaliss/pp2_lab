import pygame
import datetime

pygame.init()

clock = pygame.time.Clock()

mick = pygame.transform.scale(pygame.image.load("123/mickeyclock.png"), (800, 600))
min = pygame.transform.scale(pygame.image.load("123/min.png"), (800, 600))
sec = pygame.transform.scale(pygame.image.load("123/sec.png"), (50, 600))


def rot_center(surf, image, angle, x, y):
    image = pygame.transform.rotate(image, angle)
    rect = image.get_rect(center=image.get_rect(center=(x, y)).center)
    surf.blit(image, rect)


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clock")

done = False

while not done:
    t = datetime.datetime.now()

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(mick, (0, 0))
    rot_center(screen, min, -t.second * (6), 400, 300)
    rot_center(screen, sec, -t.minute * (6), 400, 300)

    pygame.display.update()

pygame.quit()
