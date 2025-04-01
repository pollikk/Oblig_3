
from testing_object import ship
import pygame
from pygame import Vector2

SCREEN_X = 1024
SCREEN_Y = 768

PLAYER_SPAWN = 350, 200
PLAYER_SIZE = (30, 30)

PLAYER_TWO_IMG = "images/Triangle.png"
PLAYER_ONE_IMG = "images/Triangle_red.png"
BACKGROUND_IMG = "images/green_background.png"

pygame.init()
game_running = True
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
myBackground = pygame.image.load(BACKGROUND_IMG)

if(__name__ == "__main__"):

    while game_running:
        screen.blit(myBackground, (0, 0))

        # ------- RECIPE FOR MAKING A OBJECT, GROUPING IT, AND DRAWING TO SCREEN ----------- #
        playerOne = ship(PLAYER_ONE_IMG, PLAYER_SPAWN, PLAYER_SIZE)
        players = pygame.sprite.Group()
        players.add(playerOne)
        players.draw(screen)
        # ------- END OF RECIPE ----------- #

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

pygame.quit()
