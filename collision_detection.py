import pygame

class collision():
    def __init__(self, position, object):
        self.position = position
        collide = object.collidepoint(position)
        return collide