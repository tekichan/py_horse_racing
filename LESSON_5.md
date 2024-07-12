# Lesson 5: Add an Enemy

In this lesson, we will add a fox character with its own animation.

## Step-by-Step Instructions

### 1. Setting Up the Project

Ensure you have the necessary files and folders in place:
- `images/` folder containing `bg_environment.png`, `horse_rider_spritesheet.png`, and `fox_spritesheet.png`.
- `sprite_strip_anim.py` file for handling sprite animations.

### 2. Update the Code

In this lesson, we will add a fox character with its own animation.

#### Define Constants for Fox Animation

Add constants for the fox animation settings:

```python
FOX_SS_PATH = FOLDER_PREFIX + 'fox_spritesheet.png'
FOX_SCALE = (160, 96)
```

#### Initialize Fox Animation
Add the following code to initialize the fox animation:

```python
fox_anim = SpriteStripAnim(FOX_SS_PATH, (0,0,80,48), 8, -1, True, TICK_FRAMES, FOX_SCALE)
```

#### Add Variables for Fox Position and Speed
Add variables to control the fox's position and speed:

```python
fox_x = SCREEN_WIDTH
fox_y = GROUND_Y + 20
fox_speed = 10
is_fox_running = False
```

#### Update Fox Image for Animation and Redraw
Add the following code to update and draw the fox image:

```python
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
```

The complete code can be found at [lesson_5.py](lesson_5.py)

### 3. Explanation
- Define Constants for Fox Animation: We define constants for the fox sprite sheet path and scale.
- Initialize Fox Animation: We initialize the fox animation using the SpriteStripAnim class.
- Add Variables for Fox Position and Speed: We add variables to control the fox's position and speed.
- Update Fox Image for Animation and Redraw: We update and draw the fox image, making it move across the screen.

### 4. Summary
In this lesson, we learned how to:
- Add a fox character with sprite animation.
- Update and draw the fox image.
- In the next lesson, we will add collision detection to make the game more interactive.


[Continue to Lesson 6](LESSON_6.md)
