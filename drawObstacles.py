import pygame
from collision_detection import collision

class obstacles (pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, red, green, blue):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((red, green, blue))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.col = collision(self.rect)