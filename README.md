# Snake Game 🐍

Welcome to my Snake Game project, a classic game developed in Python that served as an excellent learning opportunity for object-oriented programming (OOP), and working with the Turtle module.

## Project Details

### Learning Purpose

- Language: Python
- Tech details: Python, OOP, Turtle module
- Focus Areas: File handling, game logic, user interface, and gameplay mechanics.

### Project Structure

The Snake Game project includes the following files:

1. **data.txt** - Stores the high score achieved by the player.
2. **food.py** - Defines the `Food` class responsible for food placement and refreshing when the snake eats it.
3. **scoreboard.py** - Implements the `Scoreboard` class, which tracks the player's score and high score, displayed at the top center of the screen.
4. **snake.py** - Contains the `Snake` class that manages the snake's behavior, including creatio and movement.
5. **main.py** - The heart of the game. It initializes the game screen, scoreboard, snake, and food objects. The game starts when the player presses the 'space' key. It handles game logic, including collisions and score updates.

## Features

### Scoreboard

- **High Score**: The game keeps track of the highest score achieved, which is stored in the `data.txt` file.
- **Increasing Score**: The player's score increases as the snake eats food.
- **Reset Score**: The player's score resets, and the high score is updated if needed, at snake collision with walls or tail.

### Snake Behavior

- **Snake Creation**: The Snake class creates the snake.
- **Eating Food**: When the snake eats food, it grows in length and score increase.
- **Reset Snake**: The snake's position resets at collision with walls or tail.
- **Movement**: The snake's movement is controlled by the player (up, down, right, left).

## To-Do List (Work in Progress)

### Scoreboard Enhancements

- Save the player's snake name to a file.
- Add the player's snake score to the scoreboard when the game is over.
- Reset the high score according to players base (`data.txt`).

### Game Over Feature

- Display "Game Over" when the snake collides with a wall or its tail.
- Show the player's score and the top 5 high scores.
- Ask the player if they want to continue playing without resetting the snake's name.
  - Press 'Y' to continue (reset the player's score).
  - Press 'N' to stop playing (clear the screen and display the high score for the top 5 snakes).
- Add an option to exit the game or start fresh with a new snake (player) name.

### Additional Features

- Add a timer before the snake starts moving (press 'Start').
- Incorporate game music to enhance the gaming experience.

## Known Bugs

- Reset snake segments' colors to green (R=0, G=100, B=0) when G >= 255.

**Have fun playing the Snake Game!** 🎮
