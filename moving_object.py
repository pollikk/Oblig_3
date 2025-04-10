import pygame
import random
from config import STARTING_ANGLE, SCREEN_X, SCREEN_Y
from pygame.math import Vector2

# All moving objects
class Moving_object(pygame.sprite.Sprite):
    # Sets angle to the original sprites position and places the sprite randomly on the screen
    def __init__(self):
        super().__init__()
        self.angle = STARTING_ANGLE
        self.position = Vector2(random.randint(0, SCREEN_X), random.randint(0, SCREEN_Y))
        self.velocity = Vector2(0, 0)

    




