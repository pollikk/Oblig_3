
import pygame
import time
from testing_object import ship
from player_controller import controller
from pygame import Vector2

# Justering av hastighet og fps, skal flyttes til config #
SPEED = 10
TARGET_FPS = 60
clock = pygame.time.Clock()
prev_frame = time.time()


#--------------------------------------------------------#


SCREEN_X = 1024
SCREEN_Y = 768

PLAYER_SPAWN = 350, 200
PLAYER_SIZE = (45, 45)

PLAYER_TWO_IMG = "images/Triangle.png"
PLAYER_ONE_IMG = "images/Triangle_red.png"
BACKGROUND_IMG = "images/green_background.png"

STARTING_ANGLE = 0 

pygame.init()
game_running = True
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
myBackground = pygame.image.load(BACKGROUND_IMG)

if(__name__ == "__main__"):
    playerOne = ship(PLAYER_ONE_IMG, PLAYER_SPAWN, PLAYER_SIZE, STARTING_ANGLE)
    players = pygame.sprite.Group()
    players.add(playerOne)
# -------------------------- GAME LOOP -------------------------- #    
    while game_running:
        # Limit the framerate
        clock.tick(TARGET_FPS)
        
        screen.blit(myBackground, (0, 1))
        players.draw(screen)
        pygame.display.update()

        keys = pygame.key.get_pressed()
        rotation_delta = controller.update(keys) 
        playerOne.angle += rotation_delta        
        playerOne.rotate(rotation_delta)   

        # Calculate delta time
        this_frame = time.time()
        dt = this_frame - prev_frame
        prev_frame = this_frame

        




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

pygame.quit()
