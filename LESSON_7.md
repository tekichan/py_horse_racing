# Lesson 7: Display Text Components

In this final lesson, we will add text components to display the remaining distance and elapsed time.

## Step-by-Step Instructions

### 1. Setting Up the Project

Ensure you have the necessary files and folders in place:
- `images/` folder containing `bg_environment.png`, `horse_rider_spritesheet.png`, and `fox_spritesheet.png`.
- `sprite_strip_anim.py` file for handling sprite animations.

### 2. Update the Code

In this lesson, we will add text components to display the remaining distance and elapsed time.

#### Add Font Initialization

Add the following code to initialize the font:

```python
# Text Font
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
```

#### Update Distance and Time Display
Modify the game loop to update and display the distance and time:

```python
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
```

#### Display Texts
Add the following code to display the text components:

```python
# Display texts
DISPLAYSURF.blit(left_text_surface, (8,0))
right_text_x = SCREEN_WIDTH - len(time_message) * 18     # Calculate the x position of the message, aligned to right
DISPLAYSURF.blit(right_text_surface, (right_text_x,0))
```

The complete code can be found at [horse_racing_game.py](horse_racing_game.py)

### 3. Explanation
- Add Font Initialization: We initialize the font to be used for displaying text components.
- Update Distance and Time Display: We calculate and update the remaining distance and elapsed time in the game loop.
- Display Texts: We render and display the text components on the screen.

### 4. Summary
In this final lesson, we learned how to:
- Initialize font for text rendering.
- Calculate and display remaining distance and elapsed time.
- Complete the tutorial series on creating a horse racing game using Pygame.

# Congratulations!

You have completed the tutorial series on creating a horse racing game using Pygame. You have learned how to:

- Start a program with a background image.
- Add rider animation and control.
- Integrate a fox character with animation.
- Implement collision detection between the rider and the fox.
- Display text components for distance and time.
- Feel free to explore further and enhance your game with additional features and improvements.

Well done on completing the tutorial series! Have fun exploring and expanding your game development skills with Pygame.
