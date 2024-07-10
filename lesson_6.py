# Lesson 6: Add Collision Check, Fox Can Make Rider Slow
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
FOX_SS_PATH = FOLDER_PREFIX + 'fox_spritesheet.png'
GAME_TITLE = 'Horse Racing - Step 6'
FPS = 30
TICK_FRAMES = 4
GRAVITY = 3
HORSE_RIDER_SCALE = (130, 130)  # Scaling width and height of the rider image
FOX_SCALE = (160, 96)
FOX_HIT_SLOWDOWN = 3

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
rider_run_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (195,65,64,64), 3, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE) + \
                    SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,130,64,64), 3, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE)
rider_slow_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,195,64,64), 7, -1, False, TICK_FRAMES, HORSE_RIDER_SCALE)
rider_stop_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,195,64,64), 1, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE)

# Fox animation
fox_anim = SpriteStripAnim(FOX_SS_PATH, (0,0,80,48), 8, -1, True, TICK_FRAMES, FOX_SCALE)

# Variable for animations
horse_rider_anim = rider_stop_anim
horse_rider_x = 280
horse_rider_y = 200
rider_y_speed = 0
fox_x = SCREEN_WIDTH
fox_y = 220
fox_speed = 10
is_fox_running = False

# Frame per second controller
frame_per_sec = pygame.time.Clock()

# Function to check collision between rider and fox
def check_collision(rider_x, rider_y, fox_x, fox_y):
    rider_rect = pygame.Rect(rider_x, rider_y, 100, 100)  # 100x100 is the rider's actual size
    fox_rect = pygame.Rect(fox_x, fox_y, 120, 60)  # 120x60 is the fox's actual size
    return rider_rect.colliderect(fox_rect)

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

    # Update fox image for animation and redraw
    try:
        fox_image = fox_anim.next()
        fox_x -= fox_speed
        if fox_x < -160:  # Fox off screen, reset position
            fox_x = SCREEN_WIDTH
        DISPLAYSURF.blit(fox_image, (fox_x, fox_y))
    except StopIteration:
        print('ERROR: Unexpected Stop Iteration')

    # Check for collision with the fox
    if check_collision(horse_rider_x, horse_rider_y, fox_x, fox_y):
        horse_rider_anim = rider_slow_anim
        scroll_speed = max(1, scroll_speed - FOX_HIT_SLOWDOWN)

    # Draw the background and rider
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(background_image, (background_x, 0))
    DISPLAYSURF.blit(background_image, (background_x + background_image.get_width(), 0))
    DISPLAYSURF.blit(horse_rider_image, (horse_rider_x, horse_rider_y))
    DISPLAYSURF.blit(fox_image, (fox_x, fox_y))

    # Update the display and clock tick
    pygame.display.update()
    frame_per_sec.tick(FPS)

pygame.quit()   # close the pygame window
print('The game ' + GAME_TITLE + ' has ended')
