import pygame
from pygame import Vector2

BULLET_IMG = "images/Triangle.png"
BULLET_SIZE = 10, 10
BULLET_SPEED = 10


class bullet(pygame.sprite.Sprite):
    bullet_image = None

    def __init__(self, position, angle):
        super().__init__()
        if bullet.bullet_image is None:
            self.original_image = pygame.transform.scale(pygame.image.load(BULLET_IMG).convert_alpha(), BULLET_SIZE)
            bullet.bullet_image = pygame.transform.rotate(self.original_image, angle)
        self.image = bullet.bullet_image
        self.position = Vector2(position)
        self.rect = self.image.get_rect(center=self.position)
        self.angle = angle

        direction = Vector2(0, -1).rotate(-angle)
        self.velocity = direction * BULLET_SPEED

    def update(self):
        self.position += self.velocity
        self.rect.center = self.position

        if not (0 <= self.rect.x <= 1024 and 0 <= self.rect.y <= 768):
            self.kill()