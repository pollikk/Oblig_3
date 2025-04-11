
import pygame
import time
import config
from player_ship import Ship
from player_controller import controller
from collision_detection import collision
from drawObstacles import obstacles
from player_shoot import shoot
import clamp

# ---------------------------------------- GAME INITIALIZATIONS ---------------------------------------- #
pygame.init()
pygame.font.init()
game_running = True
clock = pygame.time.Clock()
prev_frame = time.time()
font = pygame.font.SysFont(None, 36)
screen = pygame.display.set_mode((config.SCREEN_X, config.SCREEN_Y))
myBackground = pygame.image.load(config.BACKGROUND_IMG)

if(__name__ == "__main__"):

# ----------------- OBJECT INITIALIZATIONS -------------------- #
    players = pygame.sprite.Group()
    obstaclesGroup = pygame.sprite.Group()
    landingpadGroup = pygame.sprite.Group()
    
    playerOne = Ship(config.PLAYER_ONE_IMG, config.PLAYER_ONE_RESPAWN)
    playerTwo = Ship(config.PLAYER_TWO_IMG, config.PLAYER_TWO_RESPAWN)
    obstacle_one = obstacles(*config.obstacleOne_X_Y, *config.obstacleOne_size, *config.obstacleOne_rgb)
    obstacle_two = obstacles(*config.obstacleTwo_X_Y, *config.obstacleTwo_size, *config.obstacleTwo_rgb)
    landingpad_one = obstacles(*config.landingpadOne_X_Y, *config.landingpadOne_size, *config.landingpadOne_rgb)
    landingpad_two = obstacles(*config.landingpadTwo_X_Y, *config.landingpadTwo_size, *config.landingpadTwo_rgb)



    players.add(playerOne)
    players.add(playerTwo)
    landingpadGroup.add(landingpad_one)
    landingpadGroup.add(landingpad_two)
    obstaclesGroup.add(obstacle_one)
    obstaclesGroup.add(obstacle_two)

    
    player_one_shooting = shoot()
    player_two_shooting = shoot()

# ---------------------------------------- GAME LOOP ---------------------------------------- #
    while game_running:
        clock.tick(config.TARGET_FPS)
        
        clamp.clampPlayers(playerOne)
        clamp.clampPlayers(playerTwo)

# -------- Frame rate -------- #
        this_frame = time.time()
        dt = this_frame - prev_frame
        prev_frame = this_frame

# -------- player positioning -------- #
        previous_position_playerOne = playerOne.position
        previous_rect_center_playerOne = playerOne.rect.center
        previous_position_playerTwo = playerTwo.position
        previous_rect_center_playerTwo = playerTwo.rect.center
        
        
# -------- player controlls -------- #
        keys = pygame.key.get_pressed()

        rotation_player_two ,thrust_player_two  = controller.update(keys,pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s) 
        playerTwo.thrust_engaged = thrust_player_two

        rotation_player_one ,thrust_player_one = controller.update(keys,pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN) 
        playerOne.thrust_engaged = thrust_player_one

        if keys[pygame.K_RETURN]:
            player_one_shooting.fire(playerOne.position, playerOne.angle)

        if keys[pygame.K_SPACE]:
            player_two_shooting.fire(playerTwo.position, playerTwo.angle)

# -------- player rotation -------- #
        playerTwo.angle += rotation_player_two * config.ROTATION_SPEED * dt       
        playerTwo.rotate(rotation_player_two * config.ROTATION_SPEED * dt)

        playerOne.angle += rotation_player_one       
        playerOne.rotate(rotation_player_one)

# -------- player update -------- #
        player_one_shooting.update()
        player_two_shooting.update()
        players.update(dt)

# -------- bullet collision -------- #
        playerTwoCol = collision(playerTwo.collision_rect)
        playerOneCol = collision(playerOne.collision_rect)

        for bullet in player_one_shooting.bullets:
            if playerTwoCol.checkCollision(bullet.rect):
                print("test")
                bullet.kill()
                playerOne.respawn(config.PLAYER_ONE_RESPAWN)
                playerTwo.respawn(config.PLAYER_TWO_RESPAWN)
                playerOne.angle = 0
                playerTwo.angle = 0
                config.PLAYER_ONE_SCORE = config.PLAYER_ONE_SCORE +1

            for obstacle in obstaclesGroup:
                if obstacle.col.checkCollision(bullet.rect):
                    bullet.kill()

        for bullet in player_two_shooting.bullets:
            if playerOneCol.checkCollision(bullet.rect):
                bullet.kill()
                playerOne.respawn(config.PLAYER_ONE_RESPAWN)
                playerTwo.respawn(config.PLAYER_TWO_RESPAWN)
                playerOne.angle = 0
                playerTwo.angle = 0
                config.PLAYER_TWO_SCORE = config.PLAYER_TWO_SCORE +1
            
            for obstacle in obstaclesGroup:
                if obstacle.col.checkCollision(bullet.rect):
                    bullet.kill()


# -------- obstacle collision -------- #

        for obstacle in obstaclesGroup:
            if(playerTwoCol.checkCollision(obstacle.rect)):
                if playerTwo.thrust_engaged:
                    playerTwo.position = previous_position_playerTwo
                    playerTwo.rect.center = previous_rect_center_playerTwo
                    playerTwo.velocity = pygame.Vector2(0, 0)
                    playerTwo.thrust_engaged = False
                else:
                    playerTwo.position = previous_position_playerTwo
                    playerTwo.rect.center = previous_rect_center_playerTwo
                    playerTwo.velocity = pygame.Vector2(0, 0) 

        for obstacle in obstaclesGroup:
            if(playerOneCol.checkCollision(obstacle.rect)):
                if playerOne.thrust_engaged:
                    playerOne.position = previous_position_playerOne
                    playerOne.rect.center = previous_rect_center_playerOne
                    playerOne.velocity = pygame.Vector2(0, 0)
                    playerOne.thrust_engaged = False
                else:
                    playerOne.position = previous_position_playerOne
                    playerOne.rect.center = previous_rect_center_playerOne
                    playerOne.velocity = pygame.Vector2(0, 0) 

        for landingpad in landingpadGroup:
            if(playerOneCol.checkCollision(landingpad.rect)):
                playerOne.fuel = 1000

        for landingpad in landingpadGroup:
            if(playerTwoCol.checkCollision(landingpad.rect)):
                playerTwo.fuel = 1000


# -------- draw to screen -------- #
        screen.blit(myBackground, (0, 1))
        player_one_shooting.draw(screen)
        player_two_shooting.draw(screen)

        obstaclesGroup.draw(screen)
        landingpadGroup.draw(screen)
        players.draw(screen)


        score_text_playerOne = font.render(f"Player One Score: {config.PLAYER_ONE_SCORE}", True, (255, 255, 255))
        score_text_playerTwo = font.render(f"Player Two Score: {config.PLAYER_TWO_SCORE}", True, (255, 255, 255))
        screen.blit(score_text_playerOne, (10, 10))
        screen.blit(score_text_playerTwo, (750, 10))


        fuel_text_playerOne = font.render(f"Player One Fuel: {int(playerOne.fuel / 10)}", True, (255, 255, 255))
        fuel_text_playerTwo = font.render(f"Player Two Fuel: {int(playerTwo.fuel/10)}", True, (255, 255, 255))
        screen.blit(fuel_text_playerOne, (10, 40))
        screen.blit(fuel_text_playerTwo, (750, 40))

        pygame.draw.rect(screen, (0, 255, 0), playerTwo.rect, 2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

pygame.quit()
