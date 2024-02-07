# Carrot Land Testing #
![The responsive](https://github.com/jlindeloef/carrotland/blob/main/readme_images/responsive.png)

[Carrotland Game](https://carrotland-bf0212b24b7f.herokuapp.com/)

## Automated testing ##
I used CI python Linter to validate my python code.

**Here are my results:**

| Page | Screenshot | Notes |
| --- | --- | --- |
| Carrot Land | |  |  |
| Python Code | ![](https://github.com/jlindeloef/carrotland/blob/main/readme_images/ci_linter_test.png) | I got the following warning on line 23, 34, 141, 180: "Continuation line under-indented for visual indent" |

## Manual testing ##
Full testing was made in the following program:

- Gitpod terminal
- Heroku terminal

    
### Testing userstories ###
| Goals | How are they achieved? | images |
| --- | --- | --- |
| **Carrot Land userstories**| |  |  |
| Understand the rules of the game | When game begins there are a rules and story section, and while through the game the rules will display. |:-- |
| Get clear instructions | When play the game, the instruction will display in the story section. You will also be guided through the game of what the user should do next. | :-- |
| Carrot messages | When user find a carrot or user miss a carrot, the game will tell the user. | :-- |
| Error messages | When user type unexpected input, error message will display and give user the information to make a correct input. | :-- |
| Win/loose messages | When winning or loosing the game, the user will get a message if win or loose. | :-- |

### Full testing ###

| Feature | Expected Outcome | Testing Performed | Result | pass/failed |
| --- | --- | --- | --- | --- |
| Row/Column | |  |  |
| Look for carrot on row(1-5) | When user add a number between 1-5, The game continue to choose a column | Enter a number 1-5 | The game continue to choose column |Pass |
| Look for carrot on row(1-5) | When user add a number outside 1-5, an error message should tell the user it is out of range and ask for a number between 1-5.  | Enter a number outside 1-5 | The error message display and user asked for a number between 1-5|Pass |
| Look for carrot on row(1-5) | When user add a letter or a symbol, an error message should tell the user to try again and ask for a number between 1-5.  | Enter a letter and symbol | The error message display and user is asked for a number between 1-5|Pass |
| Look for carrot on row(1-5) | When user add a blank space, an error message should tell the user to try again and ask for a number between 1-5.  | Enter a blank space| The error message display and user is asked for a number between 1-5|Pass |
| Choose a column(1-5) | When user add a number between 1-5, The game continue to a new turn | Enter a number 1-5 | The game continue to a new turn. |Pass |
| Choose a column(1-5) | When user add a number outside 1-5, an error message should tell the user it is out of range and ask for a number between 1-5.  | Enter a number outside 1-5 | The error message display and user asked for a number between 1-5|Pass |
| Choose a column(1-5) | When user add a letter or a symbol, an error message should tell the user to try again and ask for a number between 1-5.  | Enter a letter and symbol | The error message display and user is asked for a number between 1-5|Pass |
| Choose a column(1-5) | When user add a blank space, an error message should tell the user to try again and ask for a number between 1-5.  | Enter a blank space| The error message display and user is asked for a number between 1-5|Pass |
| Board | |  |  |
| Test the whole board | Test the whole board with 25 turns so there are 5 carrots to be found and win message displays. | Play 25 turns, the whole board | There were 5 carrots and a win message display | Pass |
