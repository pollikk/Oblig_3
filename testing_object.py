import pygame

class ship(pygame.sprite.Sprite):
    def __init__(self, image, spawn, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = spawn