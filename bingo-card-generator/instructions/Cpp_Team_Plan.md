# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

Create an interactive program that generates Bingo cards.  Bingo cards are squares of randomly-chosen numbers.  Their appearance is specified by the customer.  Numbers on a Bingo card are unique - there are no repeats.  Further, columns of numbers on a Bingo card increase from left to right, and the range of numbers that can appear in a column do not overlap.

The program will feature two levels of menus - a "Main" menu and a "Deck" menu.  Menus are *case-insensitive*, which means that both upper-case and lower-case input is acceptable.

*   The "Main" menu gives the user the option to create a new deck or quit the program.
*   The "Deck" menu lets the user view their cards, save the deck to a file, or return to the "Main" menu.

The user is guided through the deck creation process with prompts which ask the user for details such as the size of cards and number of cards in the deck (integers).  If the user inputs a number that is too large or too small, the prompt is repeated until an acceptable input is given.

In addition to the program itself, Unit Tests will be delivered to assist our Quality Assurance (QA) teams in their testing, as well as to assure our customer that the program has been written correctly.  This project follows Test Driven Development (TDD): the Unit Tests are written before the classes they are meant to test.  We are able to do this because we have carefully planned each class ahead of time.

A users manual and UML class diagrams will also be delivered with this project.


### Things we already know how to do:

*   Display menus and prompts
*   Accept and validate user input
    *   Repeat a prompt when invalid input is given
*   Convert strings into integers
*   Print a Bingo card according to the customer's format
    *   Ensure the center square of odd-sized cards is a "FREE!" square (use math)


### Things we need to figure out:

*   Print output to a file instead of the screen
*   Write Unit Tests
    *   Run Unit Tests
*   Pick numbers for Bingo cards such that
    *   They are random
    *   They are unique (no repeats on the same card; the same number may appear on many cards in the deck)
    *   Are arranged in columns of increasing value



## Phase 1: System Analysis *(10%)*

### Input used by the program

*   Menu entries given by the user
    *   Single characters
    *   Letters are accepted both in upper and lower case
*   Size of Bingo cards
    *   Integers in the range from 3 to 16
*   Range of numbers that may appear on a Bingo card, depends on the size of the card `N`
    *   The smallest number that can be on a Bingo card is 1
    *   The biggest number `M` can be as low as $2 * N^2$, or as great as $floor(3.9 * N^2)$


### Output created by the program

*   Menus and Prompts
    *   A reasonably attractive main menu with a cool logo
*   Bingo Cards
    *   The format of cards is shown in the requirements specification, and examples of each size of card have been provided
    *   Cards are numbered by their position in the deck
    *   Columns of numbers on the cards have a letter for a name.  Combined with a number, it is easy to see if that number exists on your card.
    *   Cells on Bingo cards are printed with dashes `-`, plus signs `+` and pipes `|`
    *   The cards can be printed to the screen one-at-a-time, or as a full deck
    *   The entire deck can be saved in a file


### Algorithms and Formulae

The requirement that Bingo cards have random numbers that are not repeated demands careful attention.  If we just use the computer's random number generator to pick the numbers, the program will inevitably make cards with duplicates.

The numbers will be stored in a list; as random numbers are picked the program could go look at the list to see if the current number has already been chosen... but this seems clunky.  Maybe a better approach is to treat numbers like a deck of playing cards.  A deck of cards does have any duplicates, and when it is shuffled it is in a random order.  We can create a list of numbers from 1 to `M` in order, then randomize it.  This ensures that the program cannot pick the same number twice.

The requirement that columns of the card contain non-overlapping ranges of numbers sounds difficult at first, but can be achieved by applying the above idea `N` times, the first column gets the first $\frac{1}{N}$ of numbers, then second column gets numbers in the $\frac{2}{N}$ range, the third column $\frac{3}{N}$, etc.


## Phase 2: Design *(30%)*

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.

*Note: pseudocode is removed for brevity*

### `MenuOption` class

Represents a part of a menu.  A `MenuOption` consists of a character that the user inputs to select it, and a string that gives a full description of what the option means in the program.

When a `MenuOption` object is printed, it displays like this: `A) This is option A`.

The `MenuOption` constructor will take two parameters: the character and description string.  These will be stored in private member variables, and public accessor methods are provided


### `Menu` class

This class contains a collection of `MenuOption` objects (most likely a `std::vector`).  In order to keep the constructor simple, these options will be added/appended to this collection after the `Menu` object is instantiated.  A `Menu` will have a title or header (string) to indicate the purpose of the menu.

To keep the code consistent, the `Menu` will be written to behave like a familiar collection (again, a `std::vector` feels like the right choice) so that the programmer can just treat this like any other collection from the standard library.  This means the `Menu` will implement the addition operation for "append", and the subscript operator `[]` allowing direct access to a `MenuOption` at a specified location.  The `Menu` will also support the `length()` operation to retrieve the number of `MenuOption`s contained within.

This object also has a `prompt()` operation, which displays the menu and awaits user input.  The first character of the string entered by the user is compared, case-insensitively, against the `MenuOption`s.  If a match is found, the character of the option is returned to the caller so it can determine which option was picked.  Otherwise, the menu is repeated forever until the user picks a valid option.


### `UserInterface` class

This class ties the whole app together.

There will be only one `UserInterface` object at a time in the program.

Initially, it will print the program logo and present the main `Menu`.  From the main menu the user can exit the program, or proceed to create a Deck. When the user chooses to proceed, the `Deck` creation menu is created and presented.  The `UserInterface` will then hold on to the `Deck` object until the user returns back to the main `Menu`; at that time the `Deck` is discarded.

This class also contains private methods that facilitate input/output for the user.

*   `string get_str(string prompt)` - Prompt the user with a `prompt`, then collect their input.  Return the `string` the user typed
*   `int get_int(string prompt, int lo, int hi)` - Prompt the user with a `prompt`, then collect their input.  If the input is not numeric, show the prompt again.  Repeat the prompt if the input is an integer but less than `lo` or greater than `hi`.
*   `create_deck()` - Guide the user through the questions that constrain how they create a Deck of Bingo Cards.
    *   Specifically, the user is asked for
        *   Size of Card $[ 3 \ldots 16 ]$ (use `get_int`)
        *   Max number to appear on Card $[ 2 * N^2 \ldots floor(3.9 * N^2) ]$ (use `get_int`)
        *   Size of Deck $[ 2 \ldots 8192 ]$ (use `get_int`)
*   `print_card()` - Prompt the user for a `Card` ID number to print.
    *   Use `get_int`
    *   Check that input is not greater than number of Cards in Deck
*   `save_deck()` - Prompt the user for a filename in which to save the current `Deck`.
    *   Uses `get_str` to ask the user for a filename
    *   The requirements don't ask us to validate the user's input - just trust that they know what they're doing and crash if something goes wrong.
    *   Printing a `Deck` to a file is just the same as printing it to the screen - the difference is that a file object is provided instead of `STDOUT`


### `RandNumberSet` class

The requirements for Cards are strict and require careful consideration to get right.  After going back and forth on this, it has been decided to keep the Bingo Card as simple as possible by treating it as a simple 2D array of numbers.  The complex logic needed to fill it in correctly will be sequestered into this class.

One requirement on `Card`s is that no number can be duplicated on a `Card`.  The most elegant solution we can come up with is to make one list of numbers running from 1 to the maximum number on the `Card`, and to shuffle it like a deck of cards, then draw numbers from the top until the Bingo `Card` is filled.  This requirement only holds within one `Card`: it is okay if the same number is shared among `Card`s within the `Deck`.

There is a requirement that numbers within columns of the Bingo `Card` be drawn from increasing subsets of numbers such that the leftmost column contains the smallest numbers, and increase toward the right side of the `Card`.  These subsets cannot overlap.  This seemed difficult at first, but is easily solved by dividing the `Card` into $N$ segments, and applying the "shuffle a set of numbers" idea to each segment individually.

*   Thus, the `RandNumberSet` will support a public `shuffle` operation which shuffles each segment and resets the object so that a new `Card` can be created.
    *   Reusing the object will conserve resources in the computer
*   Numbers for an entire row of a `Card` will be provided by the public `next_row()` method.
    *   The `RandNumberSet` will have a private data member `nRowPos` which keeps track of which row is the next to be returned by `next_row()`
*   The `RandNumberSet` constructor will need to know the size of `Card` it is being used to create (so it can know how many segments to divide its numbers into), as well as the maximum number that may appear on the card.
    *   This class relies on its caller to validate its input.
*   The `Card` size, maximum number and array of segments are stored in private members.
*   For testing purposes, `operator<<` will be overloaded to enable programmers to get a look at this object
*   The size of the `RandomNumberSet` is defined to be the size of the `Card` it can create.  This value will be given by the public `size()` method.
*   A specific row of Bingo numbers can be accessed by `operator[]`


### `Deck` class

This class is essentially a container of `Card` objects (kinda like real life!).  Will possibly use a plain array, since the size of the `Deck` is known at the time of initialization.

The constructor will create each `Card` it will contain.  It will initialize a `RandNumberSet` to help with this process.  The constructor will take these parameters:

*   `int card_size` - the size of a `Card`, from 3 to 16
*   `int num_cards` - number of cards in the `Deck`, from 2 to 8192
*   `int max_num` - the highest number that may appear on a card, needed by the `RandNumberSet`

The usual assortment of public methods/overloads will be provided:

*   `size()` returns the number of `Cards` contained within
*   `operator[]` returns a specific `Card`
*   `operator<<` prints each `Card` in the `Deck`.  This method will rely on the `Card` object also overloading `operator<<`


### `Card` class

This object will have private data members to hold:

*   `int id` - the `Card`'s ID number, needed when it prints itself out
*   `int size` - the number of rows in the `Card`, needed when determining whether the center square is **Free**
*   `int rows[][]` - the 2D array that holds on the numbers
    *   The **Free** square will contain a negative value; when the Card is printed the string `"FREE!"` will be printed instead.

All of the interesting work of instantiating this object is handled by the `RandNumberSet`.  The algorithm for creating the card goes like this:

```
0.  Shuffle the RandNumberSet to ensure that fresh numbers are at the top
1.  Until the card is full
    *   Grab the next row of numbers from the RandNumberSet
    *   Copy into the Card
2.  If the size of the Card is odd, replace the center square with the value `-1` to represent **Free**
```

*   A public `id()` method provides read-only access to the private `id` member
*   `int number_at(row, col)` returns the number stored at cell `(row, col)`

The usual assortment of public methods/overloads will be provided:

*   `size()` returns the size of the `Card`
*   `operator<<` prints the `Card`.
    *   The ID # of the card is displayed above the `Card` itself
    *   ASCII-art rows and columns are drawn with dashes `-`, plus signs `+` and pipes `|`, according to the requirements
    *   Each number is centered within its cell
    *   It is easy to print the card to the screen or to a file by directing the output to `STDOUT` or to a file stream object.


## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan

*   `MenuOption` - C++ doesn't have a standard way to make a `tostring()` method, but we can do the next best thing - override the `<<` operator and send the output to a `std::stringstream`


## Phase 4: Testing & Debugging *(30%)*

### `MenuOption` class

Create no fewer than 5 `MenuOption` objects to test

3 Unit Tests

1.  Ensure each option's letter char is set correctly
2.  Ensure each option's description is set correctly
3.  Ensure the `MenuOption` is correctly converted to a String


### `Menu` class

3 Unit Tests

1.  Ensure that options can be added to a Menu
2.  Ensure that menu options can be retrieved from Menus
3.  Ensure Menu can distinguish bad commands from the good ones


### `UserInterface` class

The methods in this class depend upon user input/output, and are not straightforward to test in our C++ testing framework.


### `RandNumberSet` class

4 Unit Tests

Create an assortment of `RandNumberSet` objects to test

1.  Ensure that a `RandNumberSet`'s length is as expected
2.  Ensure that a `RandNumberSet`
    *   Retrieves the same data each time the same row is requested
    *   Raises an error for requests of out-of-bounds rows
    *   Shuffling the `RandNumberSet` does not affect the boundaries
3.  Ensure that the `RandNumberSet.next_row()` method:
    *   Returns a sentinel value when exhausted
    *   Can be reset by `.shuffle()`
    *   Retrieves different rows each time it is called
4.  Ensure that a `RandNumberSet` contains no duplicates


### `Deck` class

2 Unit Tests

Create a mixture of decks of different-sized cards.

*   Create Decks of few cards, as well as Decks of many cards.
*   Create one Deck of the smallest size (2) and one of the largest size (8192)

1.  Ensure that Decks contain expected number of cards
2.  Ensure that specific Cards can be accessed from within a Deck


### `Card` class

4 Unit Tests

Create a mixture of odd and even-sized cards, from very small to very large, no fewer than 5 cards

1.  Assert that each card's size is as expected
2.  Assert that each card's ID number is as expected
3.  Ensure that odd-sized cards have 1 "Free!" square in the center
    *   Also test that even-sized cards do not have a "Free!" square by examining the 2x2 region about their centers
4.  Ensure that Cards do not contain duplicate numbers
    *   Because numbers are randomly assigned there *may* be a chance that a duplicate slips through.  Without auditing the source code, we can't prove there is no possibility this could happen.  The best we can do with an automated test is to generate a bunch of cards (like 10,000 of them), and check them all for duplicates until we are confident enough


**Remainder of plan trimmed**
