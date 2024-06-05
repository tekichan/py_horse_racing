import pygame
from pygame.locals import *
from sprite_strip_anim import SpriteStripAnim

# Define unchanged variables
FPS = 30
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLACK = Color('black')
GAME_TITLE = 'Horse Racing'
FOLDER_PREFIX = 'images/'
TICK_FRAMES = 4
HORSE_RIDER_SS_PATH = FOLDER_PREFIX + 'horse_rider_spritesheet.png'
BACKGROUND_PATH = FOLDER_PREFIX + 'bg_environment.png'
HORSE_RIDER_SCALE = (130, 130)  # Scaling width and height of the rider image

# initializes the pygame engine	
print('The game ' + GAME_TITLE + ' is starting...')
pygame.init()

# Define Frames per second
frame_per_sec = pygame.time.Clock()

# Initiate Display screen size and surface 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(BLACK)

# Set Game Title
pygame.display.set_caption(GAME_TITLE)

# Load the background image
background_image = pygame.image.load(BACKGROUND_PATH)

# Variables for scrolling
background_x = 0
scroll_speed = 0

# Initiate spritesheet animations
rider_start_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,0,65,65), 7, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE)
rider_run_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (195,65,65,65), 3, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE) + \
                    SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,130,65,65), 3, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE)
rider_slow_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,195,65,65), 7, -1, False, TICK_FRAMES, HORSE_RIDER_SCALE)
rider_stop_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,195,65,65), 1, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE)

# Variable for rider animations
horse_rider_anim = rider_stop_anim
horse_rider_x = 280
horse_rider_y = 200

# Game loop begins
# where all the game events occur, update and get drawn to the screen
running = True  # start running
while running:
    # Define how to handle the captured events
    for event in pygame.event.get():
        # When the event belongs to QUIT
        if event.type == QUIT:
            print('The game ' + GAME_TITLE + ' is ending...')
            running = False
        # Capture Key down event
        if event.type == pygame.KEYDOWN:
            # RIGHT arrow to run
            if event.key == pygame.K_RIGHT:
                horse_rider_anim = rider_run_anim
                scroll_speed = 2
            # LEFT arrow to slow down
            if event.key == pygame.K_LEFT:
                horse_rider_anim = rider_slow_anim
                scroll_speed = 1
            # ESC key to quit
            if event.key == K_ESCAPE:
                print('The game ' + GAME_TITLE + ' is ending...')
                running = False
    
    # Scroll the background
    background_x -= scroll_speed
    if background_x <= -background_image.get_width():
        background_x = 0

    # Redraw screen
    DISPLAYSURF.fill(BLACK)

    # Draw the background twice to cover the scrolling area
    DISPLAYSURF.blit(background_image, (background_x, 0))
    DISPLAYSURF.blit(background_image, (background_x + background_image.get_width(), 0))

    # Update rider image for animation and redraw
    try:
        horse_rider_image = horse_rider_anim.next()
    except StopIteration:
        # when rider animation stop, show its stop image
        rider_slow_anim.iter()
        horse_rider_anim = rider_stop_anim
        scroll_speed = 0
    DISPLAYSURF.blit(horse_rider_image, (horse_rider_x, horse_rider_y))

    # Update the display and clock tick
    pygame.display.update()
    frame_per_sec.tick(FPS)

pygame.quit()   # close the pygame window
print('The game ' + GAME_TITLE + ' has ended')
