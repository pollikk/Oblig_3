import pygame
from bullet import bullet 

class shoot:
    def __init__(self):
        self.bullets = pygame.sprite.Group()

    def fire(self, position, angle):
        new_bullet = bullet(position, angle)
        self.bullets.add(new_bullet)

    def update(self):
        self.bullets.update()

    def draw(self, surface):
        self.bullets.draw(surface)