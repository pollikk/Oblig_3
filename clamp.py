import pygame
from config import SCREEN_X, SCREEN_Y

class clampPlayers():
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
