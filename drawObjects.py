import pygame


class draw:
    def __init__(self, image, size):
        self.original_image = pygame.image.load(image).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, size)

    def draw(self, surface, position, angle):
        rotated_image = pygame.transform.rotate(self.original_image, angle)
        new_rect = rotated_image.get_rect(center=(position.x, position.y))
        surface.blit(rotated_image, new_rect.topleft)