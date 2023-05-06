# CS 1440 Assignment 4: Bingo! - Hints

## Students' advice from last semester

*   Treat computer science like it's fun, not like homework. If you do that, then it will be fun. If you view it as homework it sucks big time. Generally speaking, people are in computer science classes because they enjoy it, so enjoy it.
*   Read the directions carefully and understand the purpose of each class.
*   This assignment is really easy. Just do the design part first and you’ll be straight chilling
*   Make sure you understand the relationships of each classes and what information they share with each other.
*   You should probably figure out how `NumberSet` works before you design everything else.
*   Do not touch the `Menu` and `MenuOption` classes, they're basically done for you at the start. Also, make sure you understand how the `NumberSet` class works!
*   If you don't understand how the starter code is supposed to work after thinking about it for a couple of hours change it to how you think it should work. It will save you lots of time.
*   Use the code that is provided and build upon it. Don´t just throw away the source code. This assignment really helped me learn how to read another programmers code and understand how classes and methods should be implemented. 
*   The advice I would give is to start at the top with the UI then move into the meat of the code instead of the other way around, as then you can figure out what is going wrong as you are coding and then you have a lot less debugging to do jumping around from class to class, to attempt to figure out what you did wrong. 
*   Don't be afraid to change the implementation of the starter code if it makes more sense to you.
*   Make sure you know how all the classes work and plug in together
*   Some classes are a lot easier to implement than others, and some are very easy to overcomplicate if you're not sure what's going on.
*   The size variable in the `NumberSet` class is the max number variable you're looking for and not the size of the card like every other class in the program would have you believe please make note of that that's critical thx
*   Planning is important, but don't forget the time commitment towards testing and debugging.
*   Be sure to check your output thoroughly, the provided unit tests do not cover the program's full functionality.
*   Plan for extra time for the documentation and the diagrams. This one will take a little longer. Try to thoroughly read through the code as much as you can as soon as you get this assignment. It will make it easier to quickly do the UML. If by some ruthless move you are denied a real spring break by the university again, be prepared for some of your other classes to try to cram into one or two days less. If you know these things going into it, you'll be able to not let those classes steamroll you for when you come to finish up Eric's class project (since you generally have more flexibility with his assignments as to pacing than most other classes)
*   Write the manual before anything else. It forces you to read all the READMEs and you have a great baseline of what the program is supposed to look like.
*   Start the assignment early and get your peer reviews done as soon as you can, the last thing you want is to be held up by someone else.
*   Print out your peer review and read it to your friends to check if it makes any sense at all.
*   Write and think through the documentation at the appropriate time, don't wait until the end to fill it out.
*   Keep your UML diagram up to date. It will make it easier to format at the end and will help focus your thoughts as your designing algorithms. 
*   Take the time to create a good design plan but also don't worry too much about it being 100% correct at first since you'll notice flaws during the implementation and testing phases so also make sure to give yourself ample time for those phases.
*   Most of your effort is going into planning, not coding.  It's not a hard problem to solve, you just have to break it up first.
*   Do a good job on your UML and it will be easy.
*   Honestly, the hardest part of this assignment is the design phase and using classes. Understand classes, and spend a lot of time on the design phase.


## Erik's Hints

### Design hints

*   Carefully study the Program Requirements Specification and the starter
    code.
*   Translate the requirements into your own words
*   Write your user's manual first.  You will find it helpful to envision the
    user interface before you realize it in code.
*   Decide which classes are provided for you, and what features each has
*   Decide which classes you need to add to the program.  Ask yourself these
    questions as you work:
      * Does this functionality belong in a class that was provided by the
        starter code?
      * Does this functionality belong in a new class that I must write myself?
      * How will objects of the new class relate to other classes in the
        system?
*   Translate your own rendering of the requirements into pseudocode
*   Translate your pseudocode into Python



### UML hints

*   Unit Tests should not be included in the Class diagram.
*   Focus first on *what* classes are needed and what members and methods they
    will need.
*   When you know what classes your solution contains, then you can decide how
    they will relate to each other.  It is likely that you will need to change
    the design of your classes a few times as you go.
*   It is *much* easier to re-design a class in UML than it is in Python.



### Python hints

*   An easy way to ensure that numeric user input is actually numeric is to use
    Python's `str.isnumeric()` string method.
*   The `NumberSet` class prevents numbers from being re-used on the same card.
    For instance, each card can only have the number `7` once.  But it's okay
    if every card in the deck has the number `7`.
*   Each time I ask the program to print card #7 from the same deck, I should
    see the same numbers in the same positions.  When I generate a new deck,
    however, card #7 will likely look different.
*   Don't re-write or simplify your unit tests just to make them pass.  When a
    test fails it is telling you important information about failures in your
    design.  Reconsider your design.
*   Instructions for running your Unit Tests can be found in the lecture notes
    repository on GitLab.
*   The Python format specification for centered text is `:^N`, where `N` is the width of the field in which to place the text
    *   Using an f-string, The number `123` is centered in a field of 12 columns between `|` chars like this:
        ```python
        f"|{123:^12}|"
        ```
    *   Idem., but using `str.format()`:
        ```python
        "|{:^12}|".format(123)
        ```
    *   [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec) official documentation
*   `open()` can take more than one parameter.  The one you are looking for is an optional *string* parameter that can truncate a file
