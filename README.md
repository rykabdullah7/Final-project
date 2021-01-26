# CHESSOPOLY

By PyGAMERS 
  - Saif Ullah
  - Lamees
  - Faiq Jamal
  - Muhammad Abdullah Khan Abbasi

Submitted to Dr. Arham Muslim

The game Chessopoly is the combination of two of the world's most famous games, Chess and Monopoly. It suppports a 1 vs 1 gameplay, both teams being manually controlled.

The game features the basic moves of Chess and the concept of dealing with money from Monopoly.

## Features

Main menu with three basic options.

Two background audios.

Interactive 2D board.

Thrilling decision making moments. 

Interactive prompts on reaching shops and while capturing.

Character movement using mouse clicks.

Undo movement using 'Z' key.

Six different types of characters.

Each character with different moves.

Variable amount of assets for each character.

## Technical Architecture

Main module focusing on GUI using:
  - Tkinter
  - pygame.display
  - PIL.ImageTk
  
Sound modules using:
  - pygame.mixer
  
Interactive gameplay using:
  - pygame
  - Tkinter
  - PIL
  
Self-defined functions:
  - Engine.py for:
      - Generating all valid moves
      - Movement of characters
      - Undo moves
      - Agreements on shops
      - Assets dealings while capturing
      - Comparison of assets at the end 
  - Modules.py for:
      - Background Audio
      - Displaying prompts
      - Commands on clicking buttons
      - Drawing board, characters and gridlines
  - Chessopoly.py for:
      - Centralized main function
      - Calling other modules

## How To Play
 
To move a character, click that character and then click its new location.

To undo a move, press 'Z'.

Remember! Pressing 'Z' does not bring back the assets you sold or traded.

If mistakenly clicked on an opponent's character, simply 'X' the prompt and then undo the move.

Also, press 'Z' to toggle between the teams' turns at the start of the game only.

You can either capture a character and delete its assets

OR you can take a part of its assets and switch places with it.

To end the game, capture the 'Rector' of a team.

Then assets of both the teams are compared.

The team with more assets wins the game.
   
## Dependencies

- Python 3.9.0 
- Pygame
- PIL
- Tkinter

## How to Run the Program

Run the 'Chessopoly.py' file to run the program

HAVE FUN!  
