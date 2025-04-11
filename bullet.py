''' Tarje Carlsen, Tristan Natvig '''

import pygame
from pygame import Vector2
from config import BULLET_IMG, BULLET_SIZE, BULLET_SPEED, SCREEN_X, SCREEN_Y

class bullet(pygame.sprite.Sprite):
    '''
    class for creating a bullet object. inheritence from pygames sprite sprite so that it can be grouped and drawn using pygame.group.update
    and pygame.group.draw methods.
    The class sets the image, position and angle of the bullet. Then sets up a rectangle hit box using the bullets center position.
    The bullets velocity is set using the direction its facing and a static bullet speed from config file. In the update method the 
    bullet is deleted if it goes outside the screen.
    '''
    bullet_image = None
    def __init__(self, position, angle):
        super().__init__()
        if bullet.bullet_image is None:
            self.original_image = pygame.transform.scale(pygame.image.load(BULLET_IMG).convert_alpha(), BULLET_SIZE)
            bullet.bullet_image = pygame.transform.rotate(self.original_image, angle)
        self.image = bullet.bullet_image
        self.position = Vector2(position)
        self.rect = self.image.get_rect(center=self.position)
        self.angle = angle

        direction = Vector2(0, -1).rotate(-angle)
        self.velocity = direction * BULLET_SPEED

    def update(self):
        self.position += self.velocity
        self.rect.center = self.position

        if not (0 <= self.rect.x <= SCREEN_X and 0 <= self.rect.y <= SCREEN_Y):
            self.kill()