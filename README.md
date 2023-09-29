# Carrotland
## Portfolio project : Carrotland Game
Carrot Land is a fun game for all ages and for those who likes carrots! You are up for a challenge to find carrots before the rowdy rabbit does!

**Good Luck!**

Johan Lindelöf

![The Responsive image]()

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


## Website structure
The website has four sections:
+ **Home/About us:** I combined these two Sections mostly because of layout on the page. 
+ **Courses:** A clear view of the courses the school has to offer and also prizing.
+ **Sign up:** A sign up form to send to school with name, phonenumber, email and wich instrument/instruments that are in interest.
+ **Footer:** With contact information and links to social media.

### Colours
**Background:** I decided to use a darkyellow background on the navigation section and the "About Us" section. I tried different variants of colour but found this as a working colour with the dark image in the logo and the white background colour from the "Courses" section below. The logo background is an image that I found suiting for the schools visions and philosophy. The "Courses" section, as i mention has a white background with content in boxes with borders as same darkyellow colour used before. The "Sign up" section has an image as background that I found as a good choice and the footer has the darkyellow colour.

**The colors used was:**
+ Darkyellow rgb(196, 174, 133- for background.
+ White #FFF -used for the background and text.
+ Black #000- For text and shadows.
+ Turquoise #81cfd4- For the apply button.

### Technologies
1. HTML - To create a basic site
2. CSS - To create a nice, standout front-end and to give a great user experience
3. Balsamiq - To create a wireframe

## Features

### Existing Features

+ #### Navigation Bar
  - The navigation bar will follow the user when it scrolls down through the website so you can easily navigate to where you want to go where ever you are on the website.
  - The "Home/About Us"-button will take you to the top of the page where you also can read about the school.

 ![The Navigation bar.](https://github.com/jlindeloef/onstage-music-school/blob/main/assets/images/navigationbar.jpg)

+ #### Head Image with Logo
  - The first you will notice when entering the website is the main image with a girl playing piano on stage with Onnstage Music School logo on the image.
  - This section indroduces the very philosophy and strategy of the School, to learn but also to play music!

![The logo with image.](https://github.com/jlindeloef/onstage-music-school/blob/main/assets/images/logo.png)

+ #### About Us
  - Here are information about the school, from what ages they teach. But also their visions and what they think is important of learning music.
  - The "About Us"- section is linked together with "Home" up in the navigation bar.

![About us image](https://github.com/jlindeloef/onstage-music-school/blob/main/assets/images/about-us.jpg)

+ #### Courses
  - On this section you will find the different courses the School has to offer but also the prizing.
  - It has a different colour to stand out from the rest of the sections with bordders around every course for easy display for the user.

![Courses image](https://github.com/jlindeloef/onstage-music-school/blob/main/assets/images/courses.jpg)

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
