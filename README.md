# Carrotland
## Portfolio project : Carrotland Game
Carrot Land is a fun game for all ages and for those who likes carrots! You are up for a challenge to find carrots before the rowdy rabbit does!

**Good Luck!**

Johan Lindelöf

![The responive image](https://github.com/jlindeloef/carrotland/blob/main/readme_images/responsive.png)

[Carrotland Game](https://carrotland-bf0212b24b7f.herokuapp.com/)

[Github Repository](https://github.com/jlindeloef/carrotland)

## About the game
### Project planning
This is my first time building a game so after I decided I wanted to create a game with something visual, not only plain text, I searched around for games that had a gameboard and was created only with python. 
I found a couple of games that I played to get in mind what a user wants while playing the game.

I used Balsamiq to structure an idea for my game but it wasn't the easiest way to do it. Considering the choices users can select in the game and all the paths and turns I only manage to structure the main board and the initial choices. But the process in Balsamic gave me the name of the game and an idea of how my game board should look like. Here is my Balsamic wireframe: [Carrotland Balsamic]()

To create and plan the structure of the game I made a flowchart which take me through the game and helped me with the coding. It shows the logic path throughout the game
and can help you when you read this readme.

![Flowchart](https://github.com/jlindeloef/carrotland/blob/main/readme_images/carrotland.png)


### UX
This game are for those who wants to relax and play a non complicated game.

### Users stories
- As a user I want to enjoy playing Carrotland.
- As a user I want to win the game and get a winning message and scores to be displayed when I win.
- As a user I want to have clear instructions.
- As a user I want to get rewarded on each guess if I win.
- As a user I want clear error messages to help the me enter valid input.

### Technologies
1. Python - To create the game.
2. app.diagram.net - To create the flowchart
3. Balsamiq - To create a wireframe

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
  
![first input](https://github.com/jlindeloef/carrotland/blob/main/readme_images/firstdep.png)

+ #### Feedback during the game
  After users input this will display above the gameboard:
  
  If a carrot being found on the gameboard:
  - Feedback: ![Found carrot](https://github.com/jlindeloef/carrotland/blob/main/readme_images/foundcarrot.png)
    
  If a carrot not being found on the game board:
  - Feedback: ![No carrot](https://github.com/jlindeloef/carrotland/blob/main/readme_images/nocarrot.png)
    
 Under the gameboard this will be displayed:
  - Your remaining turns.
  - New inputs for another turn.

![second turn](https://github.com/jlindeloef/carrotland/blob/main/readme_images/secondturn.png)

If you press an invalid key part from expected -the game will tell you.

![Invalid input](https://github.com/jlindeloef/carrotland/blob/main/readme_images/not%20valid%20input.png)

![Invalid column](https://github.com/jlindeloef/carrotland/blob/main/readme_images/not%20valid%20column.png)

![Invalid row](https://github.com/jlindeloef/carrotland/blob/main/readme_images/Not%20valid%20row.png)


#### Game end
After 10 turns the game ends in game over or when user found the 5 carrots.
Either you win or loose you will always get the question if you want to play again.

##### Win game
If the user finds the 5 carrots before the 10th turn it will win the game.

![Win game](https://github.com/jlindeloef/carrotland/blob/main/readme_images/win.png)

##### Loose game
If the user does not find the carrots during the 10 turns it will be Game over.

![Loose game](https://github.com/jlindeloef/carrotland/blob/main/readme_images/loose.png)

##### Play again?
If the user decides after playing the game to play again it will start from the beginning.
If the user decides to not play the game it will exit the game.

![Not play again](https://github.com/jlindeloef/carrotland/blob/main/readme_images/playagainno.png)


+ #### Gameboard
  The gameboard starts empty with 5 rows(1-5) and 5 columns(A-E).
  
  ![blank board](https://github.com/jlindeloef/carrotland/blob/main/readme_images/board.png)
  
  After the user enters their first input and press enter, the board displays the input for the next turn.
  The board displays:
  - X = If user finds a carrot.
  - Line = If user do not find a carrot.

  ![xboard](https://github.com/jlindeloef/carrotland/blob/main/readme_images/xonboard.png)
  

### Features to Implement
Further there could be an input that gives the alternative to quit when ever the user want to.
To enter a name and make a scoreboard for those who plays the game.

## Testing
+ I tested the site, and it works in different web browsers: Chrome, Firefox, and Microsoft Edge.
+ On mobile devices, I tested the my site on a Samsung Galaxy A13 with the Samsung browser and an iPhone SE with the Safari browser.
+ I confirmed that the site is responsive and functions on different screen sizes using the devtools device toolbar.
+ I confirmed that the navigation and the sections Home/About us, Courses and Sign up are readable and easy to understand.
+ I confirmed that the form works: it requires entries in every field, only accepts an email in the email field, and the submit  button works.

### Validator Testing
+ HTML No errors were returned when passing through the official W3C validator
+ CSS No errors were found when passing through the official (Jigsaw) validator

### Testing using Google Lighthouse:
I used Google Lighthouse via devtools to assess the website.

![Lighthouse image](https://github.com/jlindeloef/onstage-music-school/blob/main/assets/images/lighthouse.png)

  ### Bugs
+ Solved bugs
  - A column gap settings expanded the width outside the page but my mentor helped me solve it with flexbox properties.
+ Unsolved bugs
  - The fixed navigation bar covered the content when dropping down to the choosen section. I solved it by linking the navigation bar links a bit higher up on the page then it actually should be. This can be a little noticed in some screensizes.
 
  ## Deployment
  I followed the steps written below to deploy my project to Heroku:
  + First created a Heroku account by flollowing the instructions given from Code Institute.
  + "Create new App".
  + Give the App a unique name and enter region.
  + Click on "Create App".
  + Click on "Settings" on your new App Dashboard.
  + Scroll down to Buildpacks and added Python and Nodejs and save changes.
  + These Buildpacks need to be in the same order as below:
Python
NodeJS
+ Go to Deploy section tab and scroll down to the Deployment Method.I connect to Github pages and then could search for my Github Repository "Carrotland" and then click connect.
+ Scroll down to Automatic and Manual Deploys sections. I clicked on Manual Deployment.
+ Deploy Branch.
+ After the project has been deployed successfully I clicked the View-button to see the program run in the terminal

In github:
+ The site was deployed to Git Hub pages using the following steps:
+ After logging into GitHub I located my repository for my Portfolio Project 3.
+ I then clicked the "Settings" button at the top of my repository
+ Under General, navigate to Code and Automation and select "Pages".
+ In the Build and Deployment section for Source, select 'Deploy from a branch' from the drop-down list.
+ For Branch, select "main" from the drop-down list and "/root" in the next bar and Save.
+ On the top of the page, the link to the complete website is provided.
+ The deployed site will update automatically upon new commits to the master branch.

  ## Credits
  **Code:** Some code parts were taken from W3Schools (https://www.w3schools.com/), Stack Overflow (https://stackoverflow.com/) modified for the purpose of my website. 
Some code used in "Coders Coffehouse" and "Love Running Challenge" was used and changed for my website.

### Acknowledgements
My mentor Medale Oluwafemi for guidance and inspiration and reviewing.
Ideas were taken from The Code Institute's "Coders Coffee House" and "Love Running project".
