
import pygame
import time
from config import SCREEN_X, SCREEN_Y, PLAYER_SIZE, GRAVITY, STARTING_ANGLE, SPEED, TARGET_FPS
from testing_object import Ship
from player_controller import controller
from collision_detection import collision
from player_shoot import shoot

# Justering av hastighet og fps, skal flyttes til config #
clock = pygame.time.Clock()
prev_frame = time.time()


#--------------------------------------------------------#




PLAYER_TWO_IMG = "images/Triangle.png"
PLAYER_ONE_IMG = "images/Triangle_red.png"
BACKGROUND_IMG = "images/green_background.png" 

pygame.init()
game_running = True
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
myBackground = pygame.image.load(BACKGROUND_IMG)

if(__name__ == "__main__"):
    playerOne = Ship(PLAYER_ONE_IMG, PLAYER_SIZE)
    playerTwo = Ship(PLAYER_TWO_IMG, PLAYER_SIZE)
    players = pygame.sprite.Group()
    players.add(playerOne)
    players.add(playerTwo)
    player_shooting = shoot()
# -------------------------- GAME LOOP -------------------------- #    
    while game_running:
        # Limit the framerate
        clock.tick(TARGET_FPS)
        # Calculate delta time
        this_frame = time.time()
        dt = this_frame - prev_frame
        prev_frame = this_frame

        keys = pygame.key.get_pressed()
        rotation_delta = controller.update(keys) * dt
        playerOne.angle += rotation_delta        
        playerOne.rotate(rotation_delta)

        if keys[pygame.K_SPACE]:
            player_shooting.fire(playerOne.position, playerOne.angle)

        player_shooting.update()

        screen.blit(myBackground, (0, 1))
        player_shooting.draw(screen)
        players.draw(screen)
        pygame.display.update()

        keys = pygame.key.get_pressed()
        players.update(dt)

        rotation_delta = controller.update(keys) 
        playerOne.angle += rotation_delta        
        playerOne.rotate(rotation_delta)   


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

pygame.quit()
