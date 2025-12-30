import pygame


class SoundManager:
    def __init__(self):
        self.sounds = {
            'meteorite': pygame.mixer.Sound('sound/meteorite.ogg'),
            'click': pygame.mixer.Sound('sound/click.ogg')
        }

    def play(self, name):
        self.sounds[name].play()
