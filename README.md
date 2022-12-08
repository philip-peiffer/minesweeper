# MineSweeper

A python implementation of the classic Mine Sweeper game.

## Specifications
The game follows the rules given below:
* A player can choose the size of their board.
* The player must select a space that they suspect is free of mines.
    * If the chosen space is a mine, the game is over and the user loses.
    * If the chosen space is a neighbor to a mine, the space will be replaced with a number showing the number of mines touching this space. "Touching" occurs to each side of the space as well as the diagnol, so there are 8 total opportunities to touch a space.
    * If the chosen space is not a mine, and not a neighbor, then all spaces touching this space are revealed. This process continues recursively until a mine neighbor is revealed.
* A user can flag if they suspect a space contains a mine.
* The game is over when one of two things happen:
    * The player chooses a mine.
    * The player reveals all spaces that are not mines.
