# COMP 472/6721 Project Winter 2018

##Candy Crisis 
In this project you will implement a heuristic search to play a puzzle called Candy Crisis. Candy Crisis is a type of
sliding puzzle played with 14 tokens representing different types of candies in a box. The box has 15 predetermined
positions arranged in a box of 3 rows and 5 columns.

Initially, the player is given a random arrangement of candies in it, and the goal of the game is to rearrange the candies
into a symmetrical arrangement by sliding them one at a time into the empty space. Only a candy directly next to the
empty space, not including diagonally, can be moved into it.

A symmetrical arrangement (a goal state) is one which is balanced around the middle row, and there are no constraints
on the middle row. In other words, if the top row is identical to the bottom row, then the puzzle is solved.

###Play Modes
Your program should be able to run in manual mode and in automatic mode. This means that you should be able to run
your program with:
1. Manual entry for the player, i.e. a human indicating the moves by hand.
Note that if a human enters an illegal move, your program should give a warning and allow the user to enter a new move.
2. Automatic mode, i.e. your “AI” solving and indicating the moves.
Note that if your program generates an illegal move, the entire puzzle solution will be considered wrong.
After each move, your program must display the new configuration of the candy box.

## Instructions:
The main file to run the game is `main.py` and requires `python 3` to run.
If automatic mode is selected (AI mode), the input games to solve will be taken from the 4 input files in`input{#}.txt`. 
The four files represent four sets of games of different difficulty level. Each line of each file represent a new board 
configuration game to solve. 
If manual mode is selected, the player will solve the games in `input_manual.txt`