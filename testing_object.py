import pygame
from pygame import Vector2
from rotatable import Rotatable
from moving_object import Moving_object
from config import PLAYER_SIZE

class Ship(Rotatable, Moving_object):
    def __init__(self, image, position):
        super().__init__()
        size = PLAYER_SIZE
        self.original_image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), size)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.position)