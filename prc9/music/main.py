import pygame
from player import MusicPlayer

pygame.init()
screen = pygame.display.set_mode((600, 250))
pygame.display.set_caption("Music Player")
font = pygame.font.SysFont(None, 36)

player = MusicPlayer([
    "ana.wav",
    "sary.wav"
])

running = True

while running:
    screen.fill((0, 0, 0))

    text = font.render("Track: " + player.get_current_track_name(), True, (255, 255, 255))
    screen.blit(text, (20, 50))

    time_text = font.render("Time: " + player.get_time(), True, (255, 255, 255))
    screen.blit(time_text, (20, 100))

    pygame.display.flip()

    if player.is_playing and not pygame.mixer.music.get_busy() and not player.is_paused:
        player.next()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            if event.key == pygame.K_s:
                player.stop()
            if event.key == pygame.K_n:
                player.next()
            if event.key == pygame.K_b:
                player.prev()
            if event.key == pygame.K_SPACE:
                player.pause()
            if event.key == pygame.K_q:
                running = False

pygame.quit()