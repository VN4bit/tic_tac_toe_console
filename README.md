# Tic-Tac-Toe

A simple command-line Tic-Tac-Toe game implemented in Python using an object-oriented approach.

## Features
- Two-player turn-based gameplay.
- Players take turns choosing a position to place their symbol (`X` or `O`).
- The game checks for a win or a tie after every move.
- The game board is displayed after each turn.

## How to Play
1. The game starts by displaying the Tic-Tac-Toe grid with numbered positions (0-8).
2. Players take turns entering a number (0-8) to place their symbol on the grid.
3. The game continues until a player wins or the game ends in a tie.
4. The winner is determined when a player successfully places three of their symbols in a row, column, or diagonal.

## Code Overview
- `Game`: Handles the game flow, turn-taking, and checking for game-over conditions.
- `Player`: Represents a player with a symbol (`X` or `O`) and takes input for their move.
- `Grid`: Manages the game board, places symbols, prints the board, and checks for winning conditions.

## Example Gameplay
```
['0', '1', '2']
['3', '4', '5']
['6', '7', '8']

Player X, choose position: 4
['0', '1', '2']
['3', 'X', '5']
['6', '7', '8']

Player O, choose position: 0
['O', '1', '2']
['3', 'X', '5']
['6', '7', '8']
...
```

## Future Improvements
- Add an AI opponent for single-player mode.
- Improve input handling to prevent invalid moves.
- Implement a graphical interface.

## License
This project is open-source and available under the [MIT License](LICENSE).

