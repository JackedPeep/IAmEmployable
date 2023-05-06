# CS 1440 Assignment 4: Bingo!

*   [Instructions](./instructions/README.md)
    *   [Output examples](./instructions/examples/)
    *   [Hints](./instructions/Hints.md)
    *   [Rubric](./instructions/Rubric.md)
    *   [How to Submit this Assignment](./instructions/How_To_Submit_Assignments.md)
*   C++ Team [Software Development Plan](./instructions/Cpp_Team_Plan.md)
*   C++ Team [UML Class Diagram](./instructions/Cpp_Team_UML.pdf)

*Note: this file is a placeholder for your own notes.  When seeking help from the TAs or tutors replace the text in this file with a description of your problem and push it to your repository on GitLab*

## Get the starter code

*   Assignment instructions, sample data files and example output are provided on the course GitLab server.
*   Clone this repository and use it as a basis for your work.
    *   Run each of these commands one-at-a-time, without the `$' (that represents your shell's prompt):
    *   Replace, `LAST`, `FIRST` and `USERNAME` with *your* own names.

```bash
$ git clone git@gitlab.cs.usu.edu:erik.falor/cs1440-falor-erik-assn4 cs1440-assn4
$ cd cs1440-assn4
$ git remote rename origin old-origin
$ git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-assn4.git
$ git push -u origin --all
```


## Important!
**I have instructed the CS Coaches to _not_ help you write code for this assignment until you have completed the Design phase and tagged your repository `designed`.  Don't even think about writing code until you have carefully considered the design.  Countless software projects have gone awry because the design phase was neglected.  Don't become a statistic - think first, code after.**


## Overview

For your next project at DuckieCorp you are tasked with writing an interactive Bingo card generator.  This project was started by our C++ team, but partway through the customer and the project manager decided that Python would be a better platform for this system.  I translated the partially-completed C++ program into Python before the project was assigned to you.  Some traces of the original C++ coding style are still evident.

You will create a complete *programming product* consisting of

*   A clean program that can be easily modified
*   Documentation (both technical and user-oriented)
*   Unit Tests

As you well know, creating a *programming product* can take up to 3x as much time as just making a simple program.  Plan for this and carefully manage your time so that you can meet the deadline.

## Running the starter code

Unlike previous projects, this program uses an interactive menu and *does not*
take command line arguments.

```
$ python src/bingo.py

'########::'####:'##::: ##::'######::::'#######::'####:
 ##.... ##:. ##:: ###:: ##:'##... ##::'##.... ##: ####:
 ##:::: ##:: ##:: ####: ##: ##:::..::: ##:::: ##: ####:
 ########::: ##:: ## ## ##: ##::'####: ##:::: ##:: ##::
 ##.... ##:: ##:: ##. ####: ##::: ##:: ##:::: ##::..:::
 ##:::: ##:: ##:: ##:. ###: ##::: ##:: ##:::: ##:'####:
 ########::'####: ##::. ##:. ######:::. #######:: ####:
........:::....::..::::..:::......:::::.......:::....::

    Welcome to the DuckieCorp Bingo! Deck Generator

Main menu:
C - Create a new deck
X - Exit the program

Enter a Main command (C, X)
```

At the beginning, option `X` is the only menu item that functions.  Pressing
`C` or any other key simply repeats the main menu.

Additionally, the menu is case-insensitive.  For instance, both `x` and `X`
will make the program exit.


## Objectives

*   Design before you code
*   Write a users' manual at an appropriate level of detail
*   Study existing resources to identify requirements
    *   Read source code to identify which parts are already implemented
    *   Extract the customer's requirements from the specification
    *   Create UML Class diagrams from source code
*   Extend a software system with new classes and features
    *   Design classes in UML first, then in code later
    *   Implement code to achieve the design
    *   Validate that your program is "doing the right thing"
*   Support your implementation work with unit tests
    *   Design code to meet the test's specifications
    *   Create or modify tests as your design evolves
    *   Verify that your program is "doing the thing right"
