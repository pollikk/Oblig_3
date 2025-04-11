import pygame
from pygame import Vector2
from rotatable import Rotatable
from moving_object import Moving_object
from config import PLAYER_SIZE, SPEED, GRAVITATION, MAX_FUEL


class Ship(Rotatable, Moving_object):
    def __init__(self, image, position):
        super().__init__()
        size = PLAYER_SIZE
        self.original_image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), size)
        self.position = position
        self.velocity = pygame.Vector2(0, 0)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.position)
        self.thrust_engaged = False
        self.gravity = Vector2(0, GRAVITATION)
        self.friction = 0.96
        self.fuel = MAX_FUEL
        self.collision_rect = pygame.Rect(0, 0, 60, 60) 
        self.collision_rect.center = self.position

    def update(self,dt):
        if self.thrust_engaged and self.fuel >= 0:
            moving_direction = Vector2(0, -1).rotate(-self.angle)
            moving_speed = SPEED
            self.velocity += moving_direction * moving_speed * dt
            self.fuel -= 20 *dt
        else:
            self.velocity *= self.friction ** dt

        self.velocity += self.gravity *dt
        self.position += self.velocity *dt
        self.rect.center = self.position
        self.collision_rect.center = self.position 

    def respawn(self,respawn):
        self.position = respawn
        self.velocity = pygame.Vector2(0, 0)
        self.rect = self.image.get_rect(center=self.position)
        self.gravity = Vector2(0, GRAVITATION)
        self.friction = 0.96
        self.fuel = MAX_FUEL
        self.collision_rect = pygame.Rect(0, 0, 60, 60) 
        self.collision_rect.center = self.position
        self.thrust_engaged = False
