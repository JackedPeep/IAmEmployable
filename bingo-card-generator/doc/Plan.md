# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

<tt>A comprehensive package system that creates and prints decks of bingo cards that users can also save decks at their leisure.</tt>

**A good solution for creation of the program:**

* Should contain *cards* that display:
    * random numbers, with a certain number of rows in height and a certain number of columns in length with a free space in the middle.
    * A unique ID# to identify the card.
* Should contain a *deck* that can:
  * piece together all of the different cards created.
  * print the deck of cards or a certain card in the deck
  * save a text file of the deck for the user.
  
**The things I know how to accomplish are:**

  * Creating the card layout and randomising the lengths.
  * Creating a txt file for the user to take.
  * Creating an interactive starter menu.

## Phase 1: System Analysis *(10%)*


**The data:**

* User input will be all that should be required for this program to run.
   * User inputs how many cards in the deck.
   * User retrieves card or cards from the deck.
   * User card size
   * User max bingo numbers

**The output:**

* Output will be dependent on valid user input.

   * When printing a card:
      * card ID
      * Column Name
      * Cell contents
     
**The Formula:**

* Unique classes will be used:
   * Decks made use card subclass to keep track of the cards inside the decks.
   * Card class will be a randomly generated number grid with user inputs guiding the calculations for length, width, max deck size, and max randomly generated numbers for the boxes.
     
## Phase 2: Design *(30%)*

Organization will be as follows.

*Function title: Inputs--> Outputs*

    Documentation strings that explane functionality.


**In card:**
    

*ID: card number--> Random number unique to the card*

    ID = Random number generated with identifying flags 
    return ID


*number_at: Row, Column--> returns the value in the bingo square specified*

    return value at row (row) and column (column) 
    
*len: ID--> returns the length of the card*

    return len of the card with matching ID 

*str: ID--> returns the printed BINGO card*

    return a string equivilent of a printed bingo card 

**In Deck:**

*len: deck item--> returns the number of cards in the deck*

    return length of the deck array 

*getitem: ID--> returns the printed BINGO card*

    runs the str() method of the card with the unique ID. 

*str: --> returns the entire deck in string format*

    for every card in deck
        return a string equivalent of a bingo card

**In Menu:**

*iadd: menu item--> appends a menu option to the menu screen*

    prints the option to the menu screen 

*getitem: --> returns a menu option*

    return a menu option 

*len: --> returns number of menu options*

    returns length of menu 

*dIsValidCommand: --> returns boolien*

    if menu option is in list of commands
        return true
    if menu option is not in the list of comands
        return false

*prompt: User command--> returns none*

    if bIsValidCommand is true 
        runs the comands of the user

**In MenuOption:**
    
*chCommand: specified user input--> returns the command letter that activates this command*

    return string command button

*szDescription: --> returns a user friendly function info*

    return information on the command 

*str: --> returns both chCommand and szDescription*

    return a command letter and description.

*RandNumberSet: --> returns a random ID#*

    return a random ID#

*User interface: --> creates an interface for the user to interact with and run valid commands*

    parent class of the program.

**In the face of good input:**

* The user will be able to run comands that create and print decks of bingo cards that are uniquly identified and print them to save on txt files.

**In the face of bad input:**
* The program will not run and return to the previous menu to ensure that the user doesn't break the program.
## Phase 3: Implementation *(15%)*


I learned that understanding predeveloped code requires a lot of reading documentation andfollowing instructions.
It took longer than I thought because I didn't know how things worked and so I wrote code that didn't work.

## Phase 4: Testing & Debugging *(30%)*


## Main menu tests

**test case 1:**

Make sure that the user stays on the main menu if an invalid argument is used.

Prebuilt and worked as is

**test case 2:**

ensure options can be added to menu

Prebuilt and worked as is

**test case 3:**

ensure options can be retrieved from menu

Prebuilt and worked as is

## Test MenuOption
**Test 1:**

create 5 menu objects to test

Prebuilt and worked as is

**test 2:**

ensure each option's letter is set correctly

Prebuilt and worked as is

**test 3:**

ensure each option's description is set correctly

Prebuilt and worked as is

**test 4:**

ensure the __str__ dunder works correctly

Prebuilt and worked as is

## Test RandNumberSet
**test 1:**

ensure test length is as expected

Prebuilt and worked as is

**Test 2:**

len()
* retirieves the same number each time
* raises index error for out of bound requests
* shuffling does not effect boundries

Prebuilt and worked as is

**Test 3:**

nextRow() 
- returns none when exausted
- is reset by shuffle
- retrieves different rows each time it is called

Prebuilt and worked as is

**Test 4:**

noDuplicates()
- ensures there is no duplicates... DUH 

Had to change the range in this one to get it to work


## Card

none of the tests worked because cards were initialized incorrectly

Creat 5 cards of different sizes

**Test 1:**

len()
- test that each card's size is as expected



**Test 2:**

ID()
- tests if the ID# is as expected

**Test 3:**

freeSquares()
- check if odd size cards have free squares and evens do not

**Test 4:**

noDuplicates()
- ensure that cards do not have any duplicate numbers

## Test Deck

none of these worked I'm not sure why

create 3 decks

**Test 1:**

len()
- ensure the deck has the right number of cards

**Test 2:**

card()
- ensure that cards can be accessed within a deck



## Phase 5: Deployment *(5%)*

did not complete assighnment


## Phase 6: Maintenance

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   Fill out the Assignment Reflection on Canvas.

1) most of the code I didn't write. The code I wrote should be easily understood.
2) yes most of the program dealing with the menu for the user interface
3) 2 seconds because im pretty confident in incomplete program is the cause
4) yes
5) yes
6) easy. just get it to work BOOM new feature
7) no, its not working now
8) no
9) no
