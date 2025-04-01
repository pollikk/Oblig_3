import pygame
import moving_object

class spaceship(moving_object, pygame.sprite.Sprite):
    def __init__(self, image):
        moving_object.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.radius = self.width / 2
        


