# Lesson 3: Add the Hero

In this lesson, we will add a rider image to our game and display it on the screen.

## Step-by-Step Instructions

### 1. Setting Up the Project

First, ensure you have the necessary files and folders in place:
- `images/` folder containing `bg_environment.png` and `horse_rider.png`.

### 2. Update the Code

Here's the updated code for this lesson:

Define the rider image path, x coordinate of the rider image sitting in the middle of the screen, and y coordinate of the rider image as the same level of the ground:
```python
HORSE_RIDER_PATH = FOLDER_PREFIX + 'horse_rider.png'
MIDDLE_X = 280
GROUND_Y = 200
```

Load the rider image into the rider image object:
```python
horse_rider_image = pygame.image.load(HORSE_RIDER_PATH)
```

Draw the rider image object in each loop:
```python
# Draw the rider
DISPLAYSURF.blit(horse_rider_image, (MIDDLE_X, GROUND_Y))
```

The complete code can be found at [lesson_3.py](lesson_3.py)

### 3. Explanation
- Initialize the Pygame Engine: We start by initializing the Pygame engine and setting up the display.
- Load the Background and Rider Images: Load the background image and the rider image from the images/ folder.
- Handle Events: In the main loop, we listen for key events. If the RIGHT arrow key is pressed, we move the background to the left by decreasing background_x.
- Draw the Background and Rider: We draw the background image at the updated position and the rider image at a fixed position (MIDDLE_X, GROUND_Y).
- Update the Display: Finally, we update the display to reflect the changes.

### 4. Summary
In this lesson, we learned how to:
- Load and display a rider image.
- Handle key events to scroll the background.
- In the next lesson, we will add animations to the rider and handle additional

[Continue to Lesson 4](LESSON_4.md)