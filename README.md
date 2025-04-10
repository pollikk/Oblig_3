``` python
--------------------------- DRAWOBJECTS ---------------------------
The object that will be drawn will be a child of the sprite.Sprite class which has a group functionality.
The sprite.group method has a draw function which is used for drawing objects onto the screen.
recipe: 
        # ------- RECIPE FOR MAKING A OBJECT, GROUPING IT, AND DRAWING TO SCREEN ----------- #
        playerOne = ship(PLAYER_ONE_IMG, PLAYER_SPAWN, PLAYER_SIZE, TEST_ANGLE)
        players = pygame.sprite.Group()
        players.add(playerOne)
        players.draw(screen)
        # ------- END OF RECIPE ----------- #

---------------------------  ROTATION: ```---------------------------
All objects that is going to be rotatable has to inherit from the rotatable class. When using the rotate function the classes rotate method will be used with an angle that its going to rotate towards. for example:
        # ------- RECIPE FOR ROTATION ----------- #
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("Left arrow key pressed!")
                    playerOne.rotate(-1)
        # ------- END OF RECIPE ----------- #

This rotates the object by -1 every time the left key button is pressed.
The rotation does not work perfectly as it is, but is a start. The rotation does not maintain the true center of the image when it rotates which makes it look abnormal.

--------------------------- COLLISION: ---------------------------
The object that will be checked for collision will be used as follows: first a collision checker object will be initialized with the 
collision class. This will take in the position of the main object. Then when the object is going to be checked if its colliding the 
checkCollision class is called to check if the two objects are colliding. This will return true on collision and false if not.
        # ------- RECIPE FOR COLLISION ----------- #
            main_object_collision = collision(main_object_collision.rect)
            if main_object_collision.checkCollision(incoming_object.rect):
                print("colliding")
        # ------- END OF RECIPE ----------- #

--------------------------- SHOOTING: ---------------------------
Instantiates a bullet using the angle from the player object. Shoots a projectile known as bullet from the bullet class. Uses the sprite sprite
class to group the bullets. can later be used with collision detection to check if a bullet collides with a player or obstacle.
        # ------- RECIPE FOR SHOOTING ----------- #
            if keys[pygame.K_SPACE]:
                player_shooting.fire(playerOne.position, playerOne.angle)
            player_shooting.update()
        # ------- END OF RECIPE ----------- #

--------------------------- HIT DETECTION: ---------------------------
Hitting using playerTwo as a testobject. First makes a collision detection object. Then iterates through the bullets to check for 
collision with playertwo. This has to be done for every object that is beign checked for collision. Bad way to do it as this will 
use allot of memory as the game gets bigger.
        # ------- RECIPE FOR HIT DETECTION ----------- #
            playerTwoCol = collision(playerTwo.position)
            for bullet in player_shooting.bullets:
                if playerTwoCol.checkCollision(bullet.rect):
                    bullet.kill()
        # ------- END OF RECIPE ----------- #

--------------------------- SCORESCREEN: ---------------------------
increment the scorescreen with playerone or playertwo with the given recipe. score can be reset with setting the score back to 0
        # ------- RECIPE FOR SCORE INCREMENT ----------- #
        PLAYER_ONE_SCORE = PLAYER_ONE_SCORE +1
        # ------- END OF RECIPE ----------- #





```