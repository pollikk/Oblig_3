import pygame

class collision():
    def __init__(self, rect):
        self.rect = rect
    
    def checkCollision(self, incommingObject_rect):
        return self.rect.colliderect(incommingObject_rect)