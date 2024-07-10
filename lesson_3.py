# Lesson 3: Add a Rider Image
import pygame
from pygame.locals import *

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLACK = Color('black')
FOLDER_PREFIX = 'images/'
BACKGROUND_PATH = FOLDER_PREFIX + 'bg_environment.png'
HORSE_RIDER_PATH = FOLDER_PREFIX + 'horse_rider.png'
GAME_TITLE = 'Horse Racing - Step 3'
FPS = 30

# initializes the pygame engine	
print('The game ' + GAME_TITLE + ' is starting...')
pygame.init()

# Set up the display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

# Load the background and rider image
background_image = pygame.image.load(BACKGROUND_PATH)
horse_rider_image = pygame.image.load(HORSE_RIDER_PATH)

# Variables for scrolling
background_x = 0
scroll_speed = 0

# Rider position
horse_rider_x = 280
horse_rider_y = 200

# Frame per second controller
frame_per_sec = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                scroll_speed = 5

    # Scroll the background
    background_x -= scroll_speed
    if background_x <= -background_image.get_width():
        background_x = 0

    # Draw the background and rider
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(background_image, (background_x, 0))
    DISPLAYSURF.blit(background_image, (background_x + background_image.get_width(), 0))
    DISPLAYSURF.blit(horse_rider_image, (horse_rider_x, horse_rider_y))

    # Update the display and clock tick
    pygame.display.update()
    frame_per_sec.tick(FPS)

pygame.quit()   # close the pygame window
print('The game ' + GAME_TITLE + ' has ended')
