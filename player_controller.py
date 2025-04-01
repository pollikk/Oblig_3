import pygame
import rotatable

class controller():
    def update(event):
        keys = pygame.key.get_pressed()
        if (event.type == pygame.KEYUP):
            if event.key==K_DOWN:
                print("down key is not pressed")
            elif event.type == pygame.KEYDOWN:
                if event.key==K_DOWN:
                    print('down key is not pressed now')
