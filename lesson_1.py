# Lesson 1: Start a Program with Background Image Only
import pygame
from pygame.locals import *

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLACK = Color('black')
FOLDER_PREFIX = 'images/'
BACKGROUND_PATH = FOLDER_PREFIX + 'bg_environment.png'
GAME_TITLE = 'Horse Racing - Step 1'

# initializes the pygame engine	
print('The game ' + GAME_TITLE + ' is starting...')
pygame.init()

# Set up the display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

# Load the background image
background_image = pygame.image.load(BACKGROUND_PATH)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    # Draw the background
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(background_image, (0, 0))

    # Update the display
    pygame.display.update()

pygame.quit()
print('The game ' + GAME_TITLE + ' has ended')
