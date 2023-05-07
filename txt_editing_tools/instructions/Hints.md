# CS 1440 Assignment 2: Text Tools - Hints

## Students' advice from last semester

*   Future students should REALLY focus on the examples. They are literally the backbone of this assignment and are critical for getting all of the different requirements.
*   Make sure to take your time thinking through the assignment before you start.  It is pretty easy once you have a detailed plan and an idea how to implement it.
*   Plan, like really plan. And break up the coding into different days so you don't get burned out like I did.
*   Spend a day planning and then implementing each tool.  They aren't hard when you break them down one at a time. 
*   Use a whiteboard to design the elements of the program, and design each element independently from the rest.  
*   I should have been a little more detailed in my plan, then I could have spent less time trying to figure things out as I code and instead spend time just implementing and testing.
*   Even with the plan I created, I got ahead of myself sometimes and got lost in the code/loops.
*   Good pseudocode saves you a lot of time
*   Keep your code simple.  This lets you adapt it to fit different purposes later on.
*   Learn to reach out to your classmates on Discord!
*   Don't overthink things.  Most answers are only a few lines long.
*   Work on the basic tools first, do the more difficult ones like `paste` last. If you are careful, you will end up being able to transfer a chunk of code from tool to tool as you work your way up to the more difficult tools, saving you time and allowing you to focus more on the specific needs of each tool.
*   Definitely go in the order Prof. Falor suggests. Trying to start out on harder tools would have been a nightmare.
*   Figuring out how to do `cut`/`paste` took a different way of thinking than I was used to.
*   `paste` didn't follow the same pattern as `cat`, so it was much harder to solve.
*   Using command line to run programs was a lot easier than setting up a million PyCharm configurations.
*   Experiment in the REPL to get the right step of codes down.
*   Start early on it, even a half hour a day will get you far.
*   Assuming the last two text tools would be comparable in difficulty to the others led to time constraints and I ended up finishing the last tool late.
*   Give yourself a good 8 hours for debugging, and use multiple terminals to test.


## Erik's Hints

### Look for Analogies

*   Each text tool shares the same structure: `Input -> Process -> Output`
*   Once you've written the first tool the rest are a variation on this theme
*   I suggest that you implement the tools in this order, beginning with `cat`: ![The Assignment #2 Tech Tree](./Tech_Tree.png)
*   Remember that these Python tools mimic existing Unix tools that you already have in your shell; when you are really stuck, just run the "real" tool to see what *it* would do


### Did you study the [examples](./examples)?

*   Before you ask for clarification about what your program should do, look for an answer in the examples.


### Cite external sources in `doc/Plan.md`

*   If you found help online, make note of it in your SDP.
*   This is how you will avoid accusations of plagiarism.


### Don't re-invent the wheel

*   All functions built-in to Python are fair game
    *   Here is the [complete list](https://docs.python.org/3/library/functions.html)
*   All methods of the built-in `list` type are fair game in this assignment
    *   Anything that you read in the output of `help(list)`
    *   Lists can be `.sort()`ed and `.reverse()`ed
*   All methods of the built-in `str` type are fair game in this assignment
    *   Anything that you read in the output of `help(str)`
    *   Python's `str` class has some handy methods such as `str.split()` and `str.join()`
*   You don't need to implement your own sorting algorithm in this assignment; use the one built-in to Python


### Python's list collection is your friend

*   Remember that files can be treated as lists of strings
*   Many of these text tools use a list or two at their heart
*   You job is made easier when you use methods of the `str` class which convert strings to/from lists
*   Python's lists can contain *anything*, even open files.
    *   Instead of reading many files into many lists, try putting the opened file objects into a single list.
*   Don't forget about Python's `in` operator.


### The contents of `sys.argv` are always strings

*   When your program must interpret an argument from `sys.argv` as a number, remember that you must convert it to a number yourself
*   Use `int()` instead of `eval()` to convert strings into numbers
    *   `eval()` is evil.
    *   While `eval()` is very convenient it suffers from the major drawback of executing *anything* the user enters as a Python statement; this is a dangerous ability to entrust to your user
    *   **Do not use `eval()` to convert strings into numbers**


### Segregate responsibilities

*   I've started you off with modules that keep related code together; embrace this organization and don't fight it
*   Decide which actions should happen in the driver program and which actions should occur in the module code
    *   Handle errors as soon as you can reasonably detect them, but do not go out of your way to detect them earlier than necessary; find a balance
    *   Don't open files too early in your program
    *   Don't wait too long to inspect the argument list
*   Don't worry about supporting optional command-line arguments until you have a tool's default behavior working right


### Close files when you are done with them

*   For every call to `open()` you should have a corresponding call to `close()`
*   When you let `open()` throw an error which causes your program to exit,
    Python will automatically close the file for you


### Use `exit()` to terminate your program immediately

*   When your program detects a serious error and cannot proceed, call `exit()` with a non-zero integer parameter to indicate that your program has terminated unsuccessfully
*   `sys.exit()` is equivalent to `exit()`; it doesn't matter which one you use


### The `>` operator is a feature of your shell

*   Your program is only responsible for printing text to the console with `print()`.
*   The `>` redirection operator is part of your shell.
    *   You don't have to write anything in Python to enable it (nor can you!)


### Efficiency matters, but only if your code works at all

*   Focus on writing **correct** code before making it **fast**
    *   You are graded on functionality, *not* performance
*   Most tools deal with files *one at a time*
    *   *Exception* `paste` may have multiple files open at once
*   Process files from top to bottom, one line at a time
    *   Work line-by-line instead of slurping an entire file into a string or list variable
    *   Some tools, however, must accumulate lines of text into a list to be processed in a later step
*   One tool works best when open file objects are stored in a list that you loop over
