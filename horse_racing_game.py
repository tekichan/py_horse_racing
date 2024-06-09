import pygame
from pygame.locals import *
from pygame import mixer
from sprite_strip_anim import SpriteStripAnim

# Define unchanged variables
FPS = 30
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MIDDLE_X = 280
GROUND_Y = 200
BLACK = Color('black')
GAME_TITLE = 'Horse Racing'
FOLDER_PREFIX = 'images/'
TICK_FRAMES = 4
HORSE_RIDER_SS_PATH = FOLDER_PREFIX + 'horse_rider_spritesheet.png'
BACKGROUND_PATH = FOLDER_PREFIX + 'bg_environment.png'
HORSE_RIDER_SCALE = (130, 130)  # Scaling width and height of the rider image
MEDIA_PREFIX = 'media/'
MAX_SCROLL_SPEED = 10
GRAVITY = 5

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
rider_start_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,0,64,64), 7, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE)
rider_run_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (195,65,64,64), 3, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE) + \
                    SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,130,64,64), 3, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE)
rider_slow_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,195,64,64), 7, -1, False, TICK_FRAMES, HORSE_RIDER_SCALE)
rider_stop_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,195,64,64), 1, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE)

# Variable for rider animations
horse_rider_anim = rider_stop_anim
horse_rider_x = MIDDLE_X
horse_rider_y = GROUND_Y
rider_y_speed = 0

# Background music
mixer.init()
mixer.music.load(MEDIA_PREFIX  + 'dark-happy-world.ogg')
mixer.music.play(loops=-1)

# Text Font
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

# Distance
remain_distance = 3000

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
                scroll_speed = scroll_speed + 2 if scroll_speed < MAX_SCROLL_SPEED else MAX_SCROLL_SPEED
            # LEFT arrow to slow down
            if event.key == pygame.K_LEFT:
                horse_rider_anim = rider_slow_anim
                scroll_speed = scroll_speed - 1 if scroll_speed > 1 else 1
            # UP arrow to jump
            if event.key == pygame.K_UP and horse_rider_y == GROUND_Y:
                rider_y_speed = 30 
            # ESC key to quit
            if event.key == K_ESCAPE:
                print('The game ' + GAME_TITLE + ' is ending...')
                running = False
    
    # Check if the horse jump or fall
    if rider_y_speed != 0 or horse_rider_y < GROUND_Y:
        horse_rider_y = horse_rider_y - rider_y_speed if horse_rider_y - rider_y_speed < GROUND_Y else GROUND_Y
        rider_y_speed = rider_y_speed - GRAVITY if horse_rider_y < GROUND_Y else 0

    # Scroll the background
    background_x -= scroll_speed
    if background_x <= -background_image.get_width():
        background_x = 0

    # Distance text
    if remain_distance > 0:
        remain_distance = remain_distance - scroll_speed
        distance_message = f'Distance: {remain_distance//10} m left'
    else:
        distance_message = 'GOAL~ Congrats!!!'
    text_surface = my_font.render(distance_message, False, (0, 0, 0))

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
        if scroll_speed == 1:
            horse_rider_anim = rider_stop_anim
            scroll_speed = 0
        else:
            horse_rider_anim = rider_run_anim
            scroll_speed = scroll_speed - 1

    DISPLAYSURF.blit(horse_rider_image, (horse_rider_x, horse_rider_y))

    DISPLAYSURF.blit(text_surface, (200,0))

    # Update the display and clock tick
    pygame.display.update()
    frame_per_sec.tick(FPS)

pygame.quit()   # close the pygame window
print('The game ' + GAME_TITLE + ' has ended')
