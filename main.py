# import [...]
import pygame
from game import Game
from monster import Monster

# initialisation de pygame
pygame.init()

# carateristique de la page
screen = pygame.display.set_mode((1080, 700))
pygame.display.set_caption("Cube ~ Game")

# charge image arriere plan
font = pygame.image.load('image/background_start.png')

# cree de nouvelle varriable
game = Game()
monster = Monster(game)

# boucle du jeu
running = True
while running:

    monster.delete()
    monster.damage()

    if game.player.health <= 0 and not game.pressed.get(pygame.K_2):
        game.player.dead_player()
        running = False

    for monster in game.all_monsters:
        monster.forward()

    # affiche sur l ecran l image
    screen.blit(font, [0, 0])
    screen.blit(game.player.image, game.player.rect)

    game.all_monsters.draw(screen)

    # afficher la bar de vie et de projectile
    game.player.health_bar_back(screen)
    game.player.health_bar_font(screen)

    # fliper la page pour voir les element
    pygame.display.flip()

    # verrifier le deplacement du joueur
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    elif game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 1025:
        game.player.move_right()

    elif game.pressed.get(pygame.K_UP) and game.player.rect.y > 100:
        game.player.move_up()

    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y < 600:
        game.player.move_down()

    elif game.pressed.get(pygame.K_1) and game.player.health < 880:
        vie = game.player.max_health - game.player.health
        game.player.health += vie

    elif game.pressed.get(pygame.K_3) and game.player.health >= 1:
        game.player.rect.x = 1001

    elif game.pressed.get(pygame.K_w):
        game.player.move_up()

    elif game.pressed.get(pygame.K_d):
        game.player.move_right()

    elif game.pressed.get(pygame.K_s):
        game.player.move_down()

    elif game.pressed.get(pygame.K_a):
        game.player.move_left()

    # condition d arret
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # condition de lachement d un bouton
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False