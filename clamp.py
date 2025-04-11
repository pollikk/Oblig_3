''' Tarje Carlsen, Tristan Natvig '''

import pygame
from config import SCREEN_X, SCREEN_Y


class clampPlayers():
    '''
    Inspiration for the class is gotten from chatgpt, chatlog: https://chatgpt.com/share/67f907ab-9bd8-8011-9a27-2d6151e9a337
    The class clampPlayers works as follows: The hit edge is initially set as false. When a player collides with the edges of the screen
    its set to True. If the hit_edge boolean is set as true the players velocity is set to 0 and the thrust is set to false. This 
    makes the player not be able to move outside the screen'
    '''
    def __init__(self, player):
        hit_edge = False

        if player.rect.left < 0:
            player.position.x = player.rect.width / 2
            hit_edge = True
        elif player.rect.right > SCREEN_X:
            player.position.x = SCREEN_X - player.rect.width / 2
            hit_edge = True

        if player.rect.top < 0:
            player.position.y = player.rect.height / 2
            hit_edge = True
        elif player.rect.bottom > SCREEN_Y:
            player.position.y = SCREEN_Y - player.rect.height / 2
            hit_edge = True

        if hit_edge:
            player.velocity = pygame.Vector2(0, 0)
            player.thrust_engaged = False

        player.rect.center = player.position
