import pygame
import os

class MusicPlayer:
    def __init__(self, playlist):
        pygame.mixer.init()
        self.playlist = playlist
        self.index = 0
        self.start_time = 0
        self.is_playing = False
        self.is_paused = False

    def play(self):
        pygame.mixer.music.load(self.playlist[self.index])
        pygame.mixer.music.play()
        self.start_time = pygame.time.get_ticks()
        self.is_playing = True
        self.is_paused = False

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False

    def next(self):
        self.index = (self.index + 1) % len(self.playlist)
        self.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.playlist)
        self.play()

    def pause(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            pygame.mixer.music.pause()
            self.is_paused = True

    def get_current_track_name(self):
        return os.path.basename(self.playlist[self.index])

    def get_time(self):
        if self.is_playing and not self.is_paused:
            seconds = (pygame.time.get_ticks() - self.start_time) // 1000
        else:
            seconds = 0
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"