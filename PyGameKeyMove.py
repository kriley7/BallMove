# pygame demo 3(b) - one image, continuous mode, move as long as a key is down

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
N_PIXELS_TO_MOVE = 3      #how many pixels it moves on key press

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
ballImage = pygame.image.load('images/ball.png')

# 5 - Initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    # Check for user pressing keys
    keyPressedTuple = pygame.key.get_pressed()

    if keyPressedTuple[pygame.K_LEFT]:  # moving left
        ballX = ballX - N_PIXELS_TO_MOVE

    if keyPressedTuple[pygame.K_RIGHT]:  # moving right
        ballX = ballX + N_PIXELS_TO_MOVE

    if keyPressedTuple[pygame.K_UP]:  # moving up
        ballY = ballY - N_PIXELS_TO_MOVE

    if keyPressedTuple[pygame.K_DOWN]:  # moving down
        ballY = ballY + N_PIXELS_TO_MOVE


    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    window.blit(ballImage, (ballX, ballY))  # draw the ball

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait