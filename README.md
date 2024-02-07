# Carrotland
## Portfolio project 3 : Carrotland Game
Carrot Land is a fun game for all ages and for those who likes carrots! You are up for a challenge to find carrots before the rowdy rabbit does!

**Good Luck!**

Johan Lindelöf

![The responsive](https://github.com/jlindeloef/carrotland/blob/main/readme_images/responsive.png)

[Carrotland Game](https://carrotland-bf0212b24b7f.herokuapp.com/)

[Github Repository](https://github.com/jlindeloef/carrotland)

## About the game
### Project planning
This is my first time building a game so after I decided I wanted to create a game with something visual, not only plain text, I searched around for games that had a gameboard and was created only with python. 
I found a couple of games that I played to get in mind what a user wants while playing the game. In my first version of the game I had numeric rows and letters for columns but I decide to change to only numeric for the second version.
The reason is that my daughter who is five years old loves to play the game but found it hard to use first numbers then change to letters. When I changed to only numbers it becaame much easier for her and it became more flow in the game.


To create and plan the structure of the game I made a flowchart which takes me through the game and helped me with the coding. It shows the logic path throughout the game
and can help you when you read this readme.

![Flowchart](https://github.com/jlindeloef/carrotland/blob/main/readme_images/carrotland.fc.png)


### UX
This game are for those who wants to relax and play a non complicated game. I decided to only use numbers in both column and row as earlier mentioned to maybe become easier for the younger player to find it fun.

### Users stories
- As a user I want to enjoy playing Carrotland.
- As a user I want to win the game and get a winning message and scores to be displayed when I win.
- As a user I want to have clear instructions.
- As a user I want to get rewarded on each guess if I win.
- As a user I want clear error messages to help the me enter valid input.

### Technologies and libraries
Technologies:
- Python to create the game.
- app.diagram.net - To create the flowchart.
- Gitpod to write the code.
- github to store the code

Library:
- Random is used for the random placement of the carrots on the board.


## Features

### Existing Features

+ #### Welcome
  - Gives the user the story and the rules.
  - The game starts and the user can begin to play.

 ![Welcone](https://github.com/jlindeloef/carrotland/blob/main/readme_images/storyboard.png)

+ #### Game start
  - An empty gameboard displays and a text that says "Find the carrots, you have 10 turns".
  - The user types in which row and column they want to look for the carrot.
  - It shows the remaining turns.
    
![First gameboard](https://github.com/jlindeloef/carrotland/blob/main/readme_images/first_game_board.png)

  - After the first turn the user will not get the whole story from the storyboard. The information narrows down to:

![second turn](https://github.com/jlindeloef/carrotland/blob/main/readme_images/afterfirstinput.png)

+ #### Feedback during the game
After users input this will display above the gameboard:
If a carrot being found on the gameboard:

Feedback:

![Found carrot](https://github.com/jlindeloef/carrotland/blob/main/readme_images/found_carrot.png)

If a carrot not being found on the game board:

Feedback:

![No carrot](https://github.com/jlindeloef/carrotland/blob/main/readme_images/nocarrot.png)
    
  Under the gameboard this will be displayed:
     - Your remaining turns.
     - New inputs for another turn.

![Second turn](https://github.com/jlindeloef/carrotland/blob/main/readme_images/second_turn.png)

If you press an invalid key part from expected -the game will tell the user.

![Invalid column](https://github.com/jlindeloef/carrotland/blob/main/readme_images/not_valid_column.png)

![Invalid row](https://github.com/jlindeloef/carrotland/blob/main/readme_images/Not_valid_row.png)


+ #### Game end
After 10 turns the game ends in game over or when user found the 5 carrots.
Either user win or loose, the user will always get the question if to play again.

##### Win game
If the user finds the 5 carrots before the 10th turn it will win the game.

![Win game](https://github.com/jlindeloef/carrotland/blob/main/readme_images/win_game.png)

##### Loose game
If the user does not find the carrots during the 10 turns it will be Game over.

![Loose game](https://github.com/jlindeloef/carrotland/blob/main/readme_images/loose_game.png)

##### Play again?
If the user decides after playing the game to play again it will start from the beginning.

+ #### Gameboard
The gameboard starts empty with 5 rows(1-5) and 5 columns(1-5).
  
![Board](https://github.com/jlindeloef/carrotland/blob/main/readme_images/game_board.png)
  
After the user enters their first input and press enter, the board displays the input for the next turn.
The board displays:
  - "X" = If user finds a carrot.
  - "*" = If user do not find a carrot.

![xonboard](https://github.com/jlindeloef/carrotland/blob/main/readme_images/x_on_board.png)
  

### Features to Implement
Further there could be an input that gives the alternative to quit when ever the user want to.
To enter a name and make a scoreboard for those who plays the game.
I would also add more features to the game as I started in my coding. Add different sizes to carrots, or also to find rabbits. Because of my timelimit I will continue to work on this as time follows.

## Testing
I did testing on the game. You can read it [here.](https://github.com/jlindeloef/carrotland/blob/main/Testing.md)
It contains:
- What happens if right input
- What happens if wrong input
- When win games
- when loose game
- Invalid inputs

### Validator Testing
+ CI python Linter
+ Heroku terminal
+ Gitpod terminal

![CI linter](https://github.com/jlindeloef/carrotland/blob/main/readme_images/ci_linter_test.png)

The CI python Linter showed warnings that I tried to fix but I did not succed. The warnings does not effect the game.

### Bugs
+ Solved bugs
  - A variable showed a warning of being unused. I solved it by unnaming the variable with a underscore.
+ Unsolved bugs
  - Only the ones mentioned in the CI python linter. But the errors will not effect the game.
 
## Deployment
  I followed the steps written below to deploy my project to Heroku:
  + First created a Heroku account by flollowing the instructions given from Code Institute.
  + "Create new App".
  + Give the App an unique name and enter region europe.
  + Click on "Create App".
  + Click on "Settings" on your new App Dashboard.
  + Scroll down to Buildpacks and added Python and Nodejs and save changes.
  + These Buildpacks need to be in the same order as below:
    Python
    NodeJS
+ Go to Deploy section tab and scroll down to the Deployment Method.I connect to Github pages and then could search for my Github Repository "Carrotland" and then click connect.
+ Scroll down to Automatic and Manual Deploys sections. I clicked on Manual Deployment.
+ Deploy Branch.
+ After the project has been deployed successfully I clicked the View-button to see the program run in the terminal.

In github:
The site was deployed to Git Hub pages using the following steps:
+ After logging into GitHub I located my repository for my Portfolio Project 3.
+ I then clicked the "Settings" button at the top of my repository
+ Under General, navigate to Code and Automation and select "Pages".
+ In the Build and Deployment section for Source, select 'Deploy from a branch' from the drop-down list.
+ For Branch, select "main" from the drop-down list and "/root" in the next bar and Save.
+ On the top of the page, the link to the complete website is provided.
+ The deployed site will update automatically upon new commits to the master branch.

## Credits
**Code:** Some code parts were taken from W3Schools (https://www.w3schools.com/), Stack Overflow (https://stackoverflow.com/) and different youtube channels modified for the purpose of my game.
The board layout I credit Garrett Broughton on youtube.
Ideas were also taken from The Code Institute's learning plattform and projects.

### Acknowledgements
My mentor Gareth McGirr for guidance and inspiration and reviewing.
Also a great thanks to Code Institutes tutors and Student support who has been a great help during this project.
Ideas were taken from The Code Institute's learning plattform and projects.


