''' Tarje Carlsen, Tristan Natvig '''

import pygame
from collision_detection import collision

class obstacles (pygame.sprite.Sprite):
    '''
    obstacle class creates a simple obstacle by drawing a rectangle on the screen with the configurations given in the arguments.
    this sets the obstacles cooridnates, width, height and rgb collors. The class inherits from sprite.sprite to be grouped in the main loop'
    '''
    def __init__(self, x, y, width, height, red, green, blue):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((red, green, blue))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.col = collision(self.rect)