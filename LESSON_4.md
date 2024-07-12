# Lesson 4: Add Animations and Controls

In this lesson, we will add animations for the rider and controls for slowing down and jumping.

## Step-by-Step Instructions

### 1. Setting Up the Project

Ensure you have the necessary files and folders in place:
- `images/` folder containing `bg_environment.png` and `horse_rider_spritesheet.png`.
- `sprite_strip_anim.py` file for handling sprite animations.

### 2. Update the Code

In this lesson, we will add animations for the rider and controls for slowing down and jumping.

#### Import the SpriteStripAnim Module

Add the following import statement at the beginning of your code to use the sprite animation helper:

```python
from sprite_strip_anim import SpriteStripAnim
```

#### Define Constants for Animations

Add constants for animation settings:

```python
TICK_FRAMES = 4
HORSE_RIDER_SS_PATH = FOLDER_PREFIX + 'horse_rider_spritesheet.png'
HORSE_RIDER_SCALE = (130, 130)  # Scaling width and height of the rider image
GRAVITY = 3
```

#### Initialize Sprite Animations

Add the following code to initialize sprite animations:

```python
rider_start_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,0,64,64), 7, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE)
rider_run_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (195,65,64,64), 3, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE) + \
                 SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,130,64,64), 3, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE)
rider_slow_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,195,64,64), 7, -1, False, TICK_FRAMES, HORSE_RIDER_SCALE)
rider_stop_anim = SpriteStripAnim(HORSE_RIDER_SS_PATH, (0,195,64,64), 1, -1, True, TICK_FRAMES, HORSE_RIDER_SCALE)

horse_rider_anim = rider_stop_anim
rider_y_speed = 0
```

#### Update Event Handling

Add event handling for slowing down and jumping:

```python
if event.type == pygame.KEYDOWN:
    # RIGHT arrow to run
    if event.key == pygame.K_RIGHT:
        horse_rider_anim = rider_run_anim
        scroll_speed = min(scroll_speed + 2, MAX_SCROLL_SPEED)
    # LEFT arrow to slow down
    if event.key == pygame.K_LEFT:
        horse_rider_anim = rider_slow_anim
        scroll_speed = max(scroll_speed - 1, 1)
    # UP arrow to jump
    if event.key == pygame.K_UP and horse_rider_y == GROUND_Y:
        rider_y_speed = 30
```

#### Handle Jump and Fall

Add logic to handle jump and fall:

```python
if rider_y_speed != 0 or horse_rider_y < GROUND_Y:
    horse_rider_y = max(horse_rider_y - rider_y_speed, GROUND_Y)
    rider_y_speed = max(rider_y_speed - GRAVITY, 0) if horse_rider_y < GROUND_Y else 0
```

#### Update Rider Image for Animation

Update the rider image for animation:

```python
try:
    horse_rider_image = horse_rider_anim.next()
except StopIteration:
    rider_slow_anim.iter()
    if scroll_speed == 1:
        horse_rider_anim = rider_stop_anim
        scroll_speed = 0
    else:
        horse_rider_anim = rider_run_anim
        scroll_speed -= 1
```

The complete code can be found at [lesson_4.py](lesson_4.py)

### 3. Explanation
- Import the SpriteStripAnim Module: We import the module to handle sprite animations.
- Define Constants for Animations: We define constants for the sprite sheet path, tick frames, scale, and gravity.
- Initialize Sprite Animations: We initialize different animations for starting, running, slowing down, and stopping.
- Update Event Handling: We handle key events for running, slowing down, and jumping.
- Handle Jump and Fall: We add logic to make the rider jump and fall based on gravity.
- Update Rider Image for Animation: We update the rider image to display the correct frame of the animation.

### 4. Summary
In this lesson, we learned how to:
- Add sprite animations for the rider.
- Handle key events to control the rider's actions.
- In the next lesson, we will add a fox with its own animation.

[Continue to Lesson 5](LESSON_5.md)
