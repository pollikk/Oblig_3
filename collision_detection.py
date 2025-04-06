import pygame

class collision():
    def __init__(self, position):
        self.position = position
    
    def checkCollision(self, incommingObject):
        return incommingObject.collidepoint(self.position)