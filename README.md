![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome to my very very first Python Project!

This project is part of the learning material for Code Institute's Fullstack Web Developer program.

It's taken a lot of experimentation, trial, and at times, mostly error.  

You can check it out on Heroku [here](https://battleshipsjk2.herokuapp.com/)



## Project Description

This project was created in order to get familiar with common development tools like Git & GitHub, and how to use them to write and manage python code. 

The Battleships game is played on grids on which each player's fleet of battleships are marked. 

The locations of the fleets are concealed from the other player. 

Players call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

The application provides a working battleships game for a single user to play against the computer.

Current game set to 8*8 board, 1 cell ship size and 10 turns.

To play, try to guess the rows & colums (grid reference) that contain enemy ships.

Entering a row and column will fire a missile at the grid reference.

You have 10 missiles / tries to win.

Good luck !!!



### Subject

The classic Battle Ships game.



### Audience

Anyone who likes simple games with a nostalgic retro touch



## Technology

This project was written on github using Python.

Code can be found [here](https://github.com/johnk2022/battleships)

## Game

Legend:

"X" shows a hit.

"-" shows a miss.

" " (space) not guessed yet.

![GameBoard.png](GameBoard.png)




## Project Wireframe
![BSWireframe.png](BSWireframe.png)



## Credits

GitHub for the development tools and website hosting.

Python code taken from taken from YouTuber Knowledge Mavens - excellent tutorials.

CodeInstitute and my fellow students for the assistance, encouragement and general moral boosters.



## Version History

16/07/22 

Initial Commit.

Create code for 8*8 Game, 10 turns.

Deployed to Heroku

Add Player1 name

20/08/22

Add validation on player1 variable.  Blank input not allowed

Add validation on row and column input.  Blank input not allowed.

Validate code against PEP6 Online Validator.



## Test Plan

Test do not accept blank Name

Test valid row.  Row number must be between 1 & 8

Test valid column.

Test row/column already guessed.

Test code against PEP8 online validator



## Test Results


Do not accept blank Name

![BlankName.png](BlankName.png)

Enter Your Name text repeats until valid input is received.





Test valid row.  No blanks and Row number must be between 1 & 8

![VaildateRow.png](VaildateRow.png)

Please select a valid row 1 to 8 repeats until valid input is received.





Test valid column.  No blanks and Column letter must be between A & H

![VaildateColumn.png](VaildateColumn.png)

Please select a valid column A to H repeats until valid input is received.





Test Row/column already guessed.

![AlreadyGuessed.png](AlreadyGuessed.png)

Player is prompted to guess again


Do not accept blank Name

![BlankName.png](BlankName.png)

Enter Your Name text repeats until valid input is received.


Test code against PEP8 online validator.

![PEP8AllRight.png](PEP8AllRight.png)

PEP8 online validator returns All right.



## Bugs




## Future Development

Allow player to set board size.

Alow player set the number of turns.

Add multiple ship sizes


## FAQ 

N/A

---

Happy coding!

johnk2022
July 2022