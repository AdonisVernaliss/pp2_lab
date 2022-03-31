import pygame

pygame.init()
size = width, hight = (400, 200)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Bad - Media - Player')
music_list = {
    'Franz Schubert - Ave Maria, D. 839.mp3',
    'Franz Schubert - Die forelle.mp3',
    'Franz Schubert - Fischerweise, D.881.mp3'
}
music = ''


def pause_song():
    pygame.mixer.music.pause()


def unpause_song():
    pygame.mixer.music.unpause()


def forward():
    pygame.mixer.music.stop()
    for mus in music_list:
        pygame.mixer.music.load(rf'music\{mus}')  # <----
        pygame.mixer.music.play()


def backward():
    for mus in music_list:
        pygame.mixer.music.load(rf'music\{mus}')  # <----
        pygame.mixer.music.play()


SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == SONG_END:
            print('The song ended.')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            forward()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            backward()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pause_song()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            unpause_song()
    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
