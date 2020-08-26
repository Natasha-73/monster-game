# This program is a variation of the example game where a player moves across a screen and three monsters approach it from different directions
# If the player collides with any of these monsters, the player fails.
# If the player collides with a cherry prize the player wins.

# The program makes use of pygame which is imported using the pygame modules.
import pygame

# The monsters are being generated at random heights on the screen and makes use of the random module.
import random 

# This Initialises the pygame modules.
pygame.init() 

# This creates the screen of specified width and height
screen_width = 1200
screen_height = 650
screen = pygame.display.set_mode((screen_width,screen_height)) 

# This creates the player, monsters and prize from images in the folder
# Images obtained from:
# <a href="https://lovepik.com/images/animals.html">Png vectors created by 30000008988 - lovepik.com</a>
player = pygame.image.load("player.jpg")
monster1 = pygame.image.load("pink_monster.png")
monster2 = pygame.image.load("blue_monster.png")
monster3 = pygame.image.load("green_monster.png")
prize = pygame.image.load("prize1.png")

# This gets the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or
# know when the image is off the screen).
image_height = player.get_height()
image_width = player.get_width()
monster1_height = monster1.get_height()
monster1_width = monster1.get_width()
monster2_height = monster2.get_height()
monster2_width = monster2.get_width()
monster3_height = monster3.get_height()
monster3_width = monster3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

# Stores the positions of the player and monster as variables so that you can change them later. 
playerXPosition = 250
playerYPosition = 50

# Make the monsters start off screen and at a random y position. All start on the right of the screen except for Monster2.
monster1XPosition =  screen_width
monster1YPosition =  random.randint(0, screen_height - monster1_height)

monster2XPosition = 0
monster2YPosition = random.randint(0, screen_height - monster2_height)

monster3XPosition = screen_width
monster3YPosition = random.randint(0, screen_height - monster3_height)

prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)

# This checks if the up, down, left or right key is pressed.
keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# This game loop refreshes the screen to represent real time.
# This is a looping structure that will loop the indented code until the program is exited by quitting.

while 1:
    
    # Clears the screen.    
    screen.fill(0) 

    # This draws the player image to the screen at the postion specfied (250, 50).
    screen.blit(player, (playerXPosition, playerYPosition))

    # This draws the monsters and prize images to the screen 
    screen.blit(monster1, (monster1XPosition, monster1YPosition))
    screen.blit(monster2, (monster2XPosition, monster2YPosition))
    screen.blit(monster3, (monster3XPosition, monster3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    # This updates the screen. 
    pygame.display.flip()
    
    # This loops through events in the game.
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user presses a key down.
        if event.type == pygame.KEYDOWN:

            # This tests if the key pressed is either up, down, right or left.
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
                    
        # This event checks if a key is up (not depressed).
        if event.type == pygame.KEYUP:
        
            # This tests if the key released is either up, down, right or left       
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window is that the top left corner is (0, 0).
    #  Increase of Y position means the image moves down, increase of the X position moves the image to the right. 
    
    if keyUp == True:
        
        # This makes sure that the user does not move the player above the game window
        if playerYPosition > 0: 
            playerYPosition -= 1
    if keyDown == True:
        
        # This ensures that the user does not move the player below the game window.
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1
       
    if keyLeft == True:
        
        # This ensures that the user does not move the player outside of the left side of the game window  
        if playerXPosition > 0:
            playerXPosition -= 1

    if keyRight == True:

        # This ensures that the user does not move the player outside of the right side of the game window 
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1
    
    # Check for collision of the monster with the player by bound boxes around the images for the player, monsters and prize.
    # If any boxes intersect, there is a collision.
    
    # Bounding box for the player, monsters and prize and update of their position in relation to the image:
    playerBox = pygame.Rect(player.get_rect())      
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
        
    monster1Box = pygame.Rect(monster1.get_rect())
    monster1Box.top = monster1YPosition
    monster1Box.left = monster1XPosition

    monster2Box = pygame.Rect(monster2.get_rect())
    monster2Box.top = monster2YPosition
    monster2Box.left = monster2XPosition

    monster3Box = pygame.Rect(monster3.get_rect())
    monster3Box.top = monster3YPosition
    monster3Box.left = monster3XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
        
    # This test collision of any of the boxes:
    if playerBox.colliderect(monster1Box) or playerBox.colliderect(monster2Box) or playerBox.colliderect(monster3Box):

        # Display losing status to the user: 
        print("You lose!")
       
        # Quite game and exit window        
        pygame.quit()
        exit(0)
        
    # If the monster is off the screen the user wins the game:
    if playerBox.colliderect(prizeBox):
      
        # Display wining status to the user: 
        print("You win!")

        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
    
    # This makes the monsters and the prize approach the player. Note that Monster 1 and 3 also move vertically and Monster 2 approaches
    # from the left of the player.
    monster1XPosition -= 0.3
    monster1YPosition -= 0.1
    monster2XPosition += 0.2
    monster3XPosition -= 0.2
    monster3YPosition -= 0.1
    prizeXPosition -= 0.2
    
   


