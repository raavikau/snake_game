## Snake Game implemented in python using pygame graphical package.
### Initial state
* Initialize pygame and set up the display screen.
* Create the snake and move only on forward direction.
### Running State
* Generate the food on a random position on screen.
* Increase the size of the snake whenever eat the food and also update the score.
* Update the snake head position by calling our_snake() function and maintaining the snake length by removing the tail. 
### Terminal State
* When snake hit the boundaries the game is over and give option want to continue or quit game.
* Check if snake has collided with itself then the game is over.
