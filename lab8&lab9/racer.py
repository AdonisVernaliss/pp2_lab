# Imports
import pygame as pg
import random

pg.init()
# Settings
width, height = 400, 600
FPS = 30
SPEED = 5
SCORE = 0
LEVEL = 0
running = True
dead = False
Oy = 0
counter = SCORE

# Music
pg.mixer.music.load("background.wav")
pg.mixer.music.play(-1)

# Font
font = pg.font.SysFont("Verdana", 60)
font_of_score = pg.font.SysFont('Aarial', 22, bold=True)
font_of_level = pg.font.SysFont('Aarial', 22, bold=True)

# Display
clock = pg.time.Clock()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Race")
bg1 = pg.image.load("AnimatedStreet.png")
bg2 = pg.image.load("AnimatedStreet.png")

font_of_end = pg.font.SysFont('Aarial', 70, bold=True)
render_end = font_of_end.render('GAME OVER', True, pg.Color('yellow'))


# Player

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        k = pg.key.get_pressed()
        if k[pg.K_a]:
            if self.rect.left > 44:
                self.rect.move_ip(-7, 0)
        if k[pg.K_d]:
            if self.rect.right < 356:
                self.rect.move_ip(7, 0)
        if k[pg.K_w]:
            if self.rect.top > 0:
                self.rect.move_ip(0, -7)
        if k[pg.K_s]:
            if self.rect.bottom < 560:
                self.rect.move_ip(0, 7)


# Enemy
class Enemy(pg.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.y0 = y
        self.image = pg.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), self.y0)

    def move(self):
        self.rect.move_ip(0, SPEED + 2)
        if self.rect.top > 600:
            self.rect.center = (random.randint(40, 360), self.y0)


# Coins
class Coins(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), -50)

    def change(self):
        self.image = pg.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), -50)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.change()


# Objects

player = Player()
enemy1 = Enemy(-90)
enemy2 = Enemy(-180)
coin = Coins()

# Groups
enemies = pg.sprite.Group()
enemies.add(enemy1)
enemies.add(enemy2)
all_sprites = pg.sprite.Group()
all_sprites.add(enemy1)
all_sprites.add(enemy2)
all_sprites.add(player)
all_sprites.add(coin)
coins = pg.sprite.Group()
coins.add(coin)

INC_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_SPEED, 2000)

# MAIN
while running:

    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == INC_SPEED:
            SPEED += 1
    if not dead:
        # Scores
        render_score = font_of_score.render(f'SCORE: {SCORE}', True, pg.Color('black'))
        render_level = font_of_level.render(f'Level: {LEVEL}', True, pg.Color('black'))

        # Game
        Oy += SPEED
        if Oy >= 600:
            Oy = 0
        screen.blit(bg1, (0, Oy))
        screen.blit(bg2, (0, Oy - 600))

        if counter >= 10:
            counter = 0
            SPEED += 1

        if counter % 3:
            counter = 0
            LEVEL += 1

        for entity in all_sprites:
            entity.move()
            screen.blit(entity.image, entity.rect)

        screen.blit(render_score, (10, 10))
        screen.blit(render_level, (10, 30))

        if pg.sprite.spritecollideany(player, coins):
            pg.mixer.Sound("coin.mp3").play()
            SCORE += 2
            counter += 2
            coin.change()

        if pg.sprite.spritecollideany(player, enemies):
            pg.mixer.music.pause()
            SCORE = -1
            dead = True

    else:
        if SCORE == -1:
            pg.mixer.Sound('crash.wav').play()
            SCORE = 0

        screen.blit(render_end, (30, 250))

        for entity in all_sprites:
            entity.kill()

    pg.display.update()

pg.quit()
