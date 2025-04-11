''' Tarje Carlsen, Tristan Natvig '''

import pygame

class collision():
    '''
    The collision class works with returning a boolean for if the object that is being checked collides with another object.
    this is used in the gameloop to check when two specific objects are colliding.
    '''
    def __init__(self, rect):
        self.rect = rect
    
    def checkCollision(self, incommingObject_rect):
        return self.rect.colliderect(incommingObject_rect)