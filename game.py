# import [...]
import pygame
from player import Player
from monster import Monster


class Game:
    def __init__(self):
        self.play = True
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster()
        self.monster = Monster(self)
        self.pressed = {}

    def check_colision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)