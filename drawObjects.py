import pygame
import main

class draw(pygame.sprite.Sprite):
    def __init__(self, image, size, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.size = size
        self.screen = screen

    def update(self):
        self.screen.blit(self.image)
        
        # self.original_image = pygame.image.load(image).convert_alpha()
        # self.original_image = pygame.transform.scale(self.original_image, size)

    # def draw(self, surface, position, angle):
    #     rotated_image = pygame.transform.rotate(self.original_image, angle)
    #     new_rect = rotated_image.get_rect(center=(position.x, position.y))
    #     surface.blit(rotated_image, new_rect.topleft)