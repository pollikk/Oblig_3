import pygame
import random
from config import GRAVITY, STARTING_ANGLE, SPEED, SCREEN_X, SCREEN_Y
from pygame.math import Vector2

# All moving objects
class Moving_object(pygame.sprite.Sprite):
    # Sets angle to the original sprites position and places the sprite randomly on the screen
    def __init__(self):
        super().__init__()
        self.angle = STARTING_ANGLE
        self.position = Vector2(random.randint(0, SCREEN_X), random.randint(0, SCREEN_Y))
        self.velocity = Vector2(0, 0)
        self.gravity = Vector2(0, GRAVITY)

    def update(self, dt):
        moving_direction = Vector2(0, -1).rotate(-self.angle)
        moving_speed = SPEED
        self.velocity += moving_direction * moving_speed * dt
        self.position += self.velocity * dt
        self.rect.center = self.position




