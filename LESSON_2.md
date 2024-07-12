# Lesson 2: Scroll the background

In this lesson, we will add functionality to scroll the background to the left when the RIGHT arrow key is pressed.

## Step-by-Step Instructions

### 1. Setting Up the Project

First, ensure you have the necessary files and folders in place:
- `images/` folder containing `bg_environment.png`.

### 2. Update the Code

Here's the updated code for this lesson:

Define a constant of scrolling speed: 
```python
SCROLL_SPEED = 5  # Speed of background scrolling
```

Define background image object loaded from the given image path and initate the x coordinate of the background image
```python
# Load the background image
background_image = pygame.image.load(BACKGROUND_PATH)
background_x = 0  # Initial position of background
```

Handle the key event of RIGHT arrow:
```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RIGHT:
        background_x -= SCROLL_SPEED  # Move background to the left
```

The complete code can be found at [lesson_2.py](lesson_2.py)

### 3. Explanation

- Initialize the Pygame Engine: We start by initializing the Pygame engine and setting up the display.
- Load the Background Image: Load the background image from the images/ folder.
- Handle Events: In the main loop, we listen for key events. If the RIGHT arrow key is pressed, we move the background to the left by decreasing background_x.
- Draw the Background: We draw the background image at the updated position.
- Update the Display: Finally, we update the display to reflect the changes.

### 4. Summary

In this lesson, we learned how to:
- Initalise the game asset.
- Load and display a background image.
- Handle key events to scroll the background.

In the next lesson, we will add a rider image to our game.

[Continue to Lesson 3](LESSON_3.md)