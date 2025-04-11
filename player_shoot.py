''' Tarje Carlsen, Tristan Natvig '''

import pygame
from bullet import bullet 
import config

class shoot:
    '''Sets up a group of bullets using the pygame.sprite.group and bullet class and sets a fire rate in the init method. In the 
    fire method if the time since it last shot is gone past the time of fire rate it will create a new bullet and reset the time since last shot.
    in the update method the time will get incremented so that its updated for the next time fire key is pressed. in the draw method the 
    bullets are drawn to the screen.'''
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