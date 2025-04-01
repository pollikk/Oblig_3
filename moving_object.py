import pygame
import random
import main
from pygame.math import Vector2

# All moving objects
class moving_object(pygame.sprite.Sprite):
    # Sets angle to the original sprites position and places the sprite randomly on the screen
    def __init__(self):
        angle = 0
        self.position = Vector2(random.randint(0, main.SCREEN_X), random.randint(0, main.SCREEN_Y))