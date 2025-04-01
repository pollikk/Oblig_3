import pygame
from pygame import Vector2
from rotatable import Rotatable

class ship(pygame.sprite.Sprite, Rotatable):
    def __init__(self, image, position, size, angle):
        super().__init__()
        self.original_image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), size)
        self.image = self.original_image
        self.position = Vector2(position)
        self.rect = self.image.get_rect(center=self.position)
        self.angle = angle

    # def rotate(self, angle):
    #     self.angle += angle
    #     self.image = pygame.transform.rotate(self.original_image, self.angle)
    #     self.rect = self.image.get_rect(center=self.rect.center)