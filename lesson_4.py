# Lesson 3: Add Animations. LEFT Button to Slow Down, UP Button to Jump
import pygame
from pygame.locals import *
from sprite_strip_anim import SpriteStripAnim

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLACK = Color('black')
FOLDER_PREFIX = 'images/'
BACKGROUND_PATH = FOLDER_PREFIX + 'bg_environment.png'
HORSE_RIDER_SS_PATH = FOLDER_PREFIX + 'horse_rider_spritesheet.png'
GAME_TITLE = 'Horse Racing - Step 4'
FPS = 30
TICK_FRAMES = 4
GRAVITY = 3

# initializes the pygame engine	
print('The game ' + GAME_TITLE + ' is starting...')
pygame.init()

# Set up the display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

# Load the background image
background_image = pygame.image.load(BACKGROUND_PATH)

# Variables for scrolling
background_x = 0
scroll_speed = 0

# Rider animations
rider_run_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (195,65,64,64), 3, -1, True, TICK_FRAMES, (130, 130)) + \
                    SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,130,64,64), 3, -1, True, TICK_FRAMES, (130, 130))
rider_slow_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,195,64,64), 7, -1, False, TICK_FRAMES, (130, 130))
rider_stop_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,195,64,64), 1, -1, True, TICK_FRAMES, (130, 130))

# Variable for animations
horse_rider_anim = rider_stop_anim
horse_rider_x = 280
horse_rider_y = 200
rider_y_speed = 0

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
                horse_rider_anim = rider_run_anim
                scroll_speed = 5
            if event.key == pygame.K_LEFT:
                horse_rider_anim = rider_slow_anim
                scroll_speed = 2
            if event.key == pygame.K_UP and horse_rider_y == 200:
                rider_y_speed = 30

    # Check if the horse jumps or falls
    if rider_y_speed != 0 or horse_rider_y < 200:
        horse_rider_y = horse_rider_y - rider_y_speed if horse_rider_y - rider_y_speed < 200 else 200
        rider_y_speed = rider_y_speed - GRAVITY if horse_rider_y < 200 else 0

    # Scroll the background
    background_x -= scroll_speed
    if background_x <= -background_image.get_width():
        background_x = 0

    # Update rider image for animation and redraw
    try:
        horse_rider_image = horse_rider_anim.next()
    except StopIteration:
        horse_rider_anim = rider_stop_anim
        scroll_speed = 0
    DISPLAYSURF.blit(horse_rider_image, (horse_rider_x, horse_rider_y))

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
