# 2048 GAME
#### Video Demo:  <URL https://youtu.be/rM6jqqRQR_4>
#### Description:

The game 2048 was developed by Gabriele Cirulli in 2014, the game was designed for single player. It involes sliding numbered tiles on a grid to combine them, two tiles with the same number adds up. Until a tile with a maximum of 2048 is reached. This project recreates 2048 game, the projects allows users to easily quit and restart the game when necessary and it keeps track of the user's score while playing.

The program was designed using functional programming method, about eight(8) distinct functions was defined and tested; `compress`, `reverse`, `is_mergeable`, `not_full`, `new_board`, `merge`, `transpose`, `get_random` together with a GUI class `Board` that creates a graphical representation of the game. The main game logic was defined in `project.py` and the tests for each functions in `project.py` was defined in `test_project.py` as per the project's specification.

A list of lists was used to represent the game board, the following functions; `reverse`, `transpose` could be implemented without using a copy of the game board, but I decided to use copies to keep the implementation simple and easy to understand, functions like e.g `compress`could not be implemented easily without the use of extra copy.

### Project File Structure
    `project`
       |
       |____> `project.py`
       |____> `README.md`
       |____> `test_project.py`

### Project Function Definations
- `compress`: Moves none-empty board tiles to the left
- `reverse`: Reverses all tiles in board by rows
- `transpose`: Transposes tile matrix
- `is_meargable`: Checks if tile is meargable; Returns True if meargable else False
- `not_full`: Checks if tile matrix is full i.e all elements are not 0; Returns True if meargable else False
- `merge`: Merge two tiles with same number; Returns None
- `get_random`: Place a tile at random position on board
- `update_board`: Updates board(GUI) each time a move is taken by player

A player loses this game of the board is full and not mergeable in all direction, and wins if a tile numbered 2048 is reached...

