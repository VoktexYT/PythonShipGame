import pygame
import random
from sound import SoundManager


choise_x = [90, 190, 290, 390, 470]


class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('image/projectile_roche.png')
        self.rect = self.image.get_rect()
        self.rect.x = -100000
        self.rect.y = 0
        self.attack = 3
        self.velocity = 5
        self.sound = SoundManager()
        self.origin_image = self.image
        self.angle = random.randint(0, 360)

    def rotate(self):
        self.angle += 0.7
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def forward(self):
        self.rect.x -= self.velocity
        self.rotate()

    def damage(self):
        if self.game.check_colision(self, self.game.all_players):
            self.game.player.health -= self.attack

    def delete(self):
        if self.rect.x < -300:
            self.rect.x = 1000 + random.randint(200, 300)
            self.rect.y = random.choice(choise_x)
            self.velocity = random.randint(5, 7)

