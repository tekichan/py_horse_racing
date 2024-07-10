###
# Horse Racing Game
# a simple game where you control a horse rider to race
#
# @Author: Teki Chan
# @Date: 10 Jul 2024
###
from random import choices, randint
import time
import pygame
from pygame.locals import *
from pygame import mixer
from sprite_strip_anim import SpriteStripAnim

# Constants: Define unchanged variables
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MIDDLE_X = 280
GROUND_Y = 200
BLACK = Color('black')
GAME_TITLE = 'Horse Racing'
FOLDER_PREFIX = 'images/'
BACKGROUND_PATH = FOLDER_PREFIX + 'bg_environment.png'
HORSE_RIDER_SS_PATH = FOLDER_PREFIX + 'horse_rider_spritesheet.png'
FOX_SS_PATH = FOLDER_PREFIX + 'fox_spritesheet.png'
FPS = 30
TICK_FRAMES = 4
GRAVITY = 3
HORSE_RIDER_SCALE = (130, 130)  # Scaling width and height of the rider image
FOX_SCALE = (160, 96)
MEDIA_PREFIX = 'media/'
MAX_SCROLL_SPEED = 10
TOTAL_DISTANCE = 30000
FOX_SHOW_FLAGS = [0, 1]
FOX_SHOW_WEIGHTS = [0.95, 0.05]
FOX_HIT_SLOWDOWN = 3  # Amount by which to slow down when hitting a fox

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

fox_anim = SpriteStripAnim(FOX_SS_PATH, (0,0,80,48), 8, -1, True, TICK_FRAMES, FOX_SCALE)

# Variable for animations
horse_rider_anim = rider_stop_anim
horse_rider_x = MIDDLE_X
horse_rider_y = GROUND_Y
rider_y_speed = 0
fox_x = SCREEN_WIDTH
fox_y = GROUND_Y + 20
fox_speed = 10
is_fox_running = False

# Background music
mixer.init()
mixer.music.load(MEDIA_PREFIX  + 'dark-happy-world.ogg')
mixer.music.play(loops=-1)

# Text Font
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

# Distance
remain_distance = TOTAL_DISTANCE

# Function to check collision between rider and fox
def check_collision(rider_x, rider_y, fox_x, fox_y):
    rider_rect = pygame.Rect(rider_x, rider_y, 100, 100)    # 100x100 is the rider's actual size
    fox_rect = pygame.Rect(fox_x, fox_y, 120, 60)           # 120x60 is the fox's actual size
    return rider_rect.colliderect(fox_rect)

# Game loop begins
# where all the game events occur, update and get drawn to the screen
running = True  # start running
count_time = 0  # Time counted
start_time = time.time()
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

    # Distance and Time texts
    if remain_distance > 0:
        remain_distance = remain_distance - scroll_speed
        distance_message = f'Distance: {remain_distance//10} m left'
        end_time = time.time()
        count_time = int(end_time - start_time)
    else:
        distance_message = 'GOAL~ Congrats!!!'
    time_message = f'Time: {count_time}'
    left_text_surface = my_font.render(distance_message, False, (0, 0, 0))
    right_text_surface = my_font.render(time_message, False, (0, 0, 0))

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

    # Update fox image for animation and redraw
    if remain_distance > 0 and remain_distance < TOTAL_DISTANCE:
        try:
            if not is_fox_running:
                is_fox_running = choices(FOX_SHOW_FLAGS, FOX_SHOW_WEIGHTS)[0] == 1
                fox_speed = randint(5, 15)
            if is_fox_running:
                fox_image = fox_anim.next()
                fox_relative_speed = fox_speed + scroll_speed
                if fox_x > fox_relative_speed:
                    fox_x = fox_x - fox_relative_speed
                    DISPLAYSURF.blit(fox_image, (fox_x, fox_y))
                else:
                    fox_x = SCREEN_WIDTH
                    is_fox_running = False
        except StopIteration:
            print('ERROR: Unexpected Stop Iteration')
    else:
        # ensure fox is not running if the rider does not start or game over
        fox_x = SCREEN_WIDTH
        is_fox_running = False

    # Check for collision with the fox
    if is_fox_running and check_collision(horse_rider_x, horse_rider_y, fox_x, fox_y):
        horse_rider_anim = rider_slow_anim
        scroll_speed = max(1, scroll_speed - FOX_HIT_SLOWDOWN)

    # Display texts
    DISPLAYSURF.blit(left_text_surface, (8,0))
    right_text_x = SCREEN_WIDTH - len(time_message) * 18     # Calculate the x position of the message, aligned to right
    DISPLAYSURF.blit(right_text_surface, (right_text_x,0))

    # Update the display and clock tick
    pygame.display.update()
    frame_per_sec.tick(FPS)

pygame.quit()   # close the pygame window
print('The game ' + GAME_TITLE + ' has ended')
