
import pygame
import time
from testing_object import ship
from player_controller import controller
from collision_detection import collision
from player_shoot import shoot
from pygame import Vector2

# Justering av hastighet og fps, skal flyttes til config #
SPEED = 10
TARGET_FPS = 60
clock = pygame.time.Clock()
prev_frame = time.time()


#--------------------------------------------------------#


SCREEN_X = 1024
SCREEN_Y = 768

PLAYER_ONE_SCORE = 0
PLAYER_TWO_SCORE = 0

PLAYER_ONE_SPAWN = 350, 200
PLAYER_TWO_SPAWN = 800, 200
PLAYER_SIZE = (75, 75)

PLAYER_TWO_IMG = "images/Triangle.png"
PLAYER_ONE_IMG = "images/Triangle_red.png"
BACKGROUND_IMG = "images/green_background.png"

STARTING_ANGLE = 0 

pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 36)
game_running = True
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
myBackground = pygame.image.load(BACKGROUND_IMG)

if(__name__ == "__main__"):
    playerOne = ship(PLAYER_ONE_IMG, PLAYER_ONE_SPAWN, PLAYER_SIZE, STARTING_ANGLE)
    playerTwo = ship(PLAYER_TWO_IMG, PLAYER_TWO_SPAWN, PLAYER_SIZE, STARTING_ANGLE)
    players = pygame.sprite.Group()
    players.add(playerOne)
    players.add(playerTwo)
    player_one_shooting = shoot()
    player_two_shooting = shoot()
# -------------------------- GAME LOOP -------------------------- #    

    while game_running:
        # Limit the framerate
        clock.tick(TARGET_FPS)

        keys = pygame.key.get_pressed()
        rotation_player_two = controller.update(keys,pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s) 
        playerTwo.angle += rotation_player_two       
        playerTwo.rotate(rotation_player_two)
        
        rotation_player_one = controller.update(keys,pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN) 
        playerOne.angle += rotation_player_one        
        playerOne.rotate(rotation_player_one)
        if keys[pygame.K_RETURN]:
            player_one_shooting.fire(playerOne.position, playerOne.angle)

        if keys[pygame.K_SPACE]:
            player_two_shooting.fire(playerTwo.position, playerTwo.angle)

        player_one_shooting.update()
        player_two_shooting.update()

        playerTwoCol = collision(playerTwo.rect)
        for bullet in player_one_shooting.bullets:
            if playerTwoCol.checkCollision(bullet.rect):
                bullet.kill()
                PLAYER_ONE_SCORE = PLAYER_ONE_SCORE +1

        playerOneCol = collision(playerOne.rect)
        for bullet in player_two_shooting.bullets:
            if playerOneCol.checkCollision(bullet.rect):
                bullet.kill()
                PLAYER_TWO_SCORE = PLAYER_TWO_SCORE +1


        screen.blit(myBackground, (0, 1))
        player_one_shooting.draw(screen)
        player_two_shooting.draw(screen)
        players.draw(screen)
        score_text_playerOne = font.render(f"Player One Score: {PLAYER_ONE_SCORE}", True, (255, 255, 255))
        score_text_playerTwo = font.render(f"Player Two Score: {PLAYER_TWO_SCORE}", True, (255, 255, 255))
        screen.blit(score_text_playerOne, (10, 10))
        screen.blit(score_text_playerTwo, (750, 10))
        pygame.draw.rect(screen, (0, 255, 0), playerTwo.rect, 2)
        pygame.display.update()


        # Calculate delta time
        this_frame = time.time()
        dt = this_frame - prev_frame
        prev_frame = this_frame

        




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

pygame.quit()
