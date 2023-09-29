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

### UX
This game are for those who wants to relax and play a non complicated game.

### Users stories
- As a user I want to enjoy playing Carrotland.
- As a user I want to win the game and get a winning message and scores to be displayed when I win.
- As a user I want to have clear instructions.
- As a user I want to get rewarded on each guess if I win.
- As a user I want clear error messages to help the me enter valid input.

## Features
This game was created by using python coding.

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
  
  If a carrot being found on the game board:
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


+ #### Game end
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





+ #### Sign up page
  - On this section the user can sign up for the school. The user have to send in name,email and phonenumber.
  - There is a textfield for entering which instrument that are in interest. User can write multiple instruments if so will.

![Sign up image](https://github.com/jlindeloef/onstage-music-school/blob/main/assets/images/signup.jpg)

+ #### Footer
  - In the footer users find Onstage Music School contacts but also social media links.
  
![Footer image](https://github.com/jlindeloef/onstage-music-school/blob/main/assets/images/footer.jpg)

### Features to Implement
Further there could be a gallery with images and videos from concerts and lessons.

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
+ The site was deployed to Git Hub pages using the following steps:
+ After logging into GitHub I located my repository for my Portfolio Project 1.
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
