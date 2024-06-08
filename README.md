# Memory Game Using Pygame

This project implements a memory game using Pygame. The game involves matching pairs of icons hidden behind boxes, with the goal of finding all pairs.

## Features

- **Graphical Interface**: The game uses Pygame for graphical rendering.
- **Interactive Gameplay**: Players click on boxes to reveal icons and try to find matching pairs.
- **Animated Transitions**: Smooth animations for revealing and covering boxes.
- **Win Detection**: The game detects when all pairs have been found and celebrates with an animation.

## Screenshot

Here's what the game looks like:

![image](https://user-images.githubusercontent.com/72575802/197366781-27dd8f96-f4a8-45e6-bc23-a3e31a4cfe32.png)

## Requirements

- Python 3.x
- Pygame

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/memory-game.git
    cd memory-game
    ```

2. **Install Pygame**:
    ```bash
    pip install pygame
    ```

## Usage

Run the game by executing the main script:

```bash
python main.py
```


## Code Structure

- **main.py**: The main script that sets up and runs the game.
- **Functions**:
  - `main()`: Initializes the game, handles the game loop, and manages user input.
  - `generateRevealedBoxesData(val)`: Generates the initial state of revealed boxes.
  - `getRandomizedBoard()`: Randomizes the icons on the board.
  - `leftTopCoordsOfBox(boxx, boxy)`: Converts board coordinates to pixel coordinates.
  - `getBoxAtPixel(x, y)`: Identifies the box at a given pixel position.
  - `drawIcon(shape, color, boxx, boxy)`: Draws an icon on the board.
  - `getShapeAndColor(board, boxx, boxy)`: Retrieves the shape and color of an icon.
  - `drawBoxCovers(board, boxes, coverage)`: Draws boxes being covered/revealed.
  - `revealBoxesAnimation(board, boxesToReveal)`: Animation for revealing boxes.
  - `coverBoxesAnimation(board, boxesToCover)`: Animation for covering boxes.
  - `drawBoard(board, revealed)`: Draws the game board.
  - `drawHighlightBox(boxx, boxy)`: Highlights a box when hovered.
  - `startGameAnimation(board)`: Plays the start game animation.
  - `gameWonAnimation(board)`: Animation for winning the game.
  - `hasWon(revealedBoxes)`: Checks if the player has won.

## Game Logic

1. **Initialization**: Pygame initializes and sets up the display.
2. **Game Loop**: The main game loop processes events, updates game state, and renders the board.
3. **User Input**: The game responds to mouse movements and clicks to reveal boxes.
4. **Matching Logic**: If two revealed icons match, they remain uncovered; otherwise, they are covered again.
5. **Winning Condition**: The game checks if all pairs have been found and plays a winning animation.

## Configuration

- **Board Dimensions**: Adjust `BOARDWIDTH` and `BOARDHEIGHT` to change the size of the board.
- **Box Size and Gap**: Modify `BOXSIZE` and `GAPSIZE` to change the size of the boxes and the gaps between them.
- **Colors and Shapes**: Customize `ALLCOLORS` and `ALLSHAPES` to add new colors and shapes.

## Future Improvements

- **More Shapes and Colors**: Add more shapes and colors to increase variety.
- **Levels and Difficulty**: Implement multiple levels with increasing difficulty.
- **Sound Effects**: Add sound effects for clicks, matches, and winning.

Feel free to contribute to this project by opening issues or submitting pull requests on GitHub. Happy coding!
```

 




