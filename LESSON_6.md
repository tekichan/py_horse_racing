# Lesson 6: Implement Collision Detection

In this lesson, we will add collision detection between the rider and the fox. When the rider collides with the fox, the rider will slow down.

## Step-by-Step Instructions

### 1. Setting Up the Project

Ensure you have the necessary files and folders in place:
- `images/` folder containing `bg_environment.png`, `horse_rider_spritesheet.png`, and `fox_spritesheet.png`.
- `sprite_strip_anim.py` file for handling sprite animations.

### 2. Update the Code

In this lesson, we will add collision detection between the rider and the fox.

#### Add Collision Detection Function

Add the following function to check for collisions:

```python
# Function to check collision between rider and fox
def check_collision(rider_x, rider_y, fox_x, fox_y):
    rider_rect = pygame.Rect(rider_x, rider_y, 100, 100)    # 100x100 is the rider's actual size
    fox_rect = pygame.Rect(fox_x, fox_y, 120, 60)           # 120x60 is the fox's actual size
    return rider_rect.colliderect(fox_rect)
```

#### Add Constants for Fox Hit Slowdown
Add a constant for the amount by which the rider will slow down when hitting a fox:

```python
FOX_HIT_SLOWDOWN = 3  # Amount by which to slow down when hitting a fox
```

#### Check for Collision and Slow Down the Rider
Add the following code inside the game loop to check for collisions and slow down the rider:

```python
# Check for collision with the fox
if is_fox_running and check_collision(horse_rider_x, horse_rider_y, fox_x, fox_y):
    horse_rider_anim = rider_slow_anim
    scroll_speed = max(1, scroll_speed - FOX_HIT_SLOWDOWN)
```

The complete code can be found at [lesson_6.py](lesson_6.py)

### 3. Explanation
- Add Collision Detection Function: We define a function to check if the rider's and fox's rectangles overlap.
- Add Constants for Fox Hit Slowdown: We define a constant for the slowdown amount when the rider hits the fox.
- Check for Collision and Slow Down the Rider: We check for collisions inside the game loop and slow down the rider if a collision is detected.

### 4. Summary
In this lesson, we learned how to:
- Add a function to check for collisions.
- Slow down the rider when a collision is detected.
- In the next lesson, we will add text components to display the remaining distance and elapsed time.

[Continue to Lesson 7](LESSON_7.md)
