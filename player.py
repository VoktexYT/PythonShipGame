# import [...]
import pygame


# class player
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 880
        self.max_health = 880
        self.velocity = 3
        self.image = pygame.image.load('image/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 500

    # la bar de vie
    def health_bar_font(self, surface):
        font_bar_color = (255, 0, 208)
        font_bar_position = [100, 50, self.health, 10]
        pygame.draw.rect(surface, font_bar_color, font_bar_position)

    def health_bar_back(self, surface):
        back_bar_color = (94, 0, 44)
        back_bar_position = [100, 50, self.max_health, 10]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)

    # direction du joueur [droite, gauche, haut, bas]
    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def dead_player(self):
        self.rect.x -= 1000
