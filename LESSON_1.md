# Lesson 1: Start the development with Pygame

## Introduction to Pygame

### What is Pygame?

[Pygame](https://www.pygame.org/) is a set of Python modules designed for writing video games. It supports the creation of games and multimedia programs in Python.

### Why Use Pygame?

- **Ease of Use:** Simple and straightforward API, great for beginners.
- **Python Integration:** Leverages Python’s readability and efficiency.
- **Community Support:** Large community with plenty of resources and tutorials.
- **Ideal for Learning:** Perfect for teaching programming and game development.

## Requirements
- Python 3.12
- [Pygame](https://www.pygame.org/)

## Preparation
1. Install Python 3.12 if you haven't already.
2. Create your project folder, e.g. `py_horse_racing` and change directory to there
3. Create a Virtual Environment by running `python3 -m venv .venv`
4. Activate the Virtual Environment by running `source .venv/bin/activate`
5. Install Pygame by running `pip install pygame`.

## Lesson 1 Code

In this lesson, we'll start a Pygame program that displays a background image. Open the code [lesson_1.py](lesson_1.py)

### Import Pygame

First, import the necessary Pygame modules. Add this code at the top of your script:


```python
import pygame
from pygame.locals import *
```

### Define Constants
Define some constants for the screen dimensions, colors, and file paths:

```python
# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLACK = Color('black')
FOLDER_PREFIX = 'images/'
BACKGROUND_PATH = FOLDER_PREFIX + 'bg_environment.png'
GAME_TITLE = 'Horse Racing - Step 1'
```

### Initialize Pygame
Initialize the Pygame engine and set up the display:

```python
# initializes the pygame engine	
print('The game ' + GAME_TITLE + ' is starting...')
pygame.init()

# Set up the display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)
```

### Load the Background Image
Load the background image that you placed in the images folder:

```python
# Load the background image
background_image = pygame.image.load(BACKGROUND_PATH)
```

### Create the Main Loop
Create the main loop that will keep the game running and handle events:

```python
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

```

### Run the Script
Save your script and run it.

```bash
python lesson_1.py
```

## Summary 
In this code:
- We initialize Pygame and set up the display.
- We load and display a background image.
- We create a game loop that keeps running until the window is closed.
