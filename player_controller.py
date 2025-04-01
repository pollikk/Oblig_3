import pygame
import rotatable

class controller():
    def update(keys):
        rotation = 0
        if keys[pygame.K_LEFT]:
            rotation = -2
        elif keys[pygame.K_RIGHT]:
            rotation = 2
        if keys[pygame.K_UP]:
            print("test")
        if keys[pygame.K_DOWN]:
            print("test")

        return rotation
