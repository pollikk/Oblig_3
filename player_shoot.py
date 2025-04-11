import pygame
from bullet import bullet 
import config

class shoot:
    def __init__(self):
        self.bullets = pygame.sprite.Group()
        self.fire_rate = config.FIRE_RATE
        self.last_shot_time = config.FIRE_RATE

    def fire(self, position, angle):
        if(self.last_shot_time >= self.fire_rate):
            new_bullet = bullet(position, angle)
            self.bullets.add(new_bullet)
            self.last_shot_time = 0

    def update(self):
        self.last_shot_time = self.last_shot_time + config.FIRE_RATE / 15
        self.bullets.update()

    def draw(self, surface):
        self.bullets.draw(surface)