# CS 1440 Assignment 2: Text Tools - Instructions

## Table of Contents

[[_TOC_]]



## Description

In this assignment you will write your own versions of classic Unix text-processing programs.  The tools you write for this assignment are not intended to be perfect clones of the programs they are mimicking.  I have relaxed requirements that your code should meet.

This assignment is essentially a re-implementation of the classic Unix text-processing programs in Python.  Each tool will be a Python function which takes as input a list of arguments supplied by the user from the command line.



## Previous Semester Assignment Statistics

Statistic                        | Value
--------------------------------:|:---------------
Average Hours Spent              | 11.9
Average Score % (Grade)          | 85.0% (B)
% students thought this was Easy | 16.36%
... Medium                       | 56.36%
... Hard                         | 25.45%
... Too Hard/Did not complete    | 1.82%



## Requirements

### Shell Tutor Lessons

Included with this assignment are 2 new Shell Tutor lessons in [shell-tutor](./shell-tutor/).  Together they are worth 10 points.  Run `make-certificate.sh` and commit the resulting certificate file in the `shell-tutor` directory to pass this off.

You should complete the lessons sometime before you begin *testing* your text tools.  They will help you do that more effectively.

As always, if you run into a problem with the tutorial, run `tutor bug` and email the output to your instructor.



### Code organization

This program consists of several functions grouped into modules of related functionality:

| Tool   | Module                                        | Description
|--------|-----------------------------------------------|--------------------------------------------------
| `cat`  | [Concatenate.py](examples/Concatenate.md#cat) | Concatenate files and print on the standard output
| `tac`  | [Concatenate.py](examples/Concatenate.md#tac) | Concatenate and print files in reverse
| `cut`  | [CutPaste.py](examples/CutPaste.md#cut)       | Remove sections from each line of files
| `paste`| [CutPaste.py](examples/CutPaste.md#paste)     | Merge lines of files
| `grep` | [Grep.py](examples/Grep.md#grep)              | Print lines of files matching a pattern
| `head` | [Partial.py](examples/Partial.md#head)        | Output the first part of files
| `tail` | [Partial.py](examples/Partial.md#tail)        | Output the last part of files
| `sort` | [Sorting.py](examples/Sorting.md#sort)        | Sort lines of text files
| `wc`   | [WordCount.py](examples/WordCount.md#wc)      | Print newline, word, and byte counts for each file


*   Do not rename functions or modules given in the starter code.
    *   Nor should you change the parameter list of the provided functions.
    *   Your job is to fill in the blanks.
*   You may create extra helper functions as you see fit.
    *   You may organize these helper function(s) into new module(s) of your own.
    *   This isn't meant to be a sly hint implying that you need to make your own new functions and modules; 99% of students are able to complete the assignment without adding these.
    *   You do not need to write your own sorting algorithm; use what is provided by Python.


### The `tt.py` driver program

*   This project uses a single program called a "driver" to unify multiple tools into a combined interface.
    *   You are familiar with a program that has this kind of UI; the `git` program plus its subcommands operate this way
*   The driver's job is to collect the user's input and dispatch control to the appropriate tool.
    *   If the driver does not have enough or correct information, display a message that helps the user learn how to use it.
*   A good driver is very simple and short, leaving most of the processing and decision-making up to the tools.


### How do each of the text tools work?

*   Explanations of how each tool works are given in the [examples](./examples/) directory.
    *   Make your program match the example output as closely as you can.
    *   Study these documents to understand what each tool does in **best case** scenarios as well as the **worst cases**.
    *   Look to the [test scripts](./scripts/README.md) for a way to easily compare your program's output to these examples.
*   If the tool's description under the examples directory doesn't have anything to say about a certain behavior (i.e. I've left it *undefined*), you have latitude in how you approach it
    *   Mention such situations in your Software Development Plan
*   Refrain from adding extra features that aren't required
    *   Deviations from the expected makes grading unnecessarily difficult for us
    *   You can always revisit this project and improve it later


### Text tools do not modify their input files

*   The tools *do not* change the contents of their input files.
*   If you open a file in any mode besides **read-only mode** `"r"` you're doing it wrong!
    *   The default mode used by `open()` *is* read-only; as long as you don't go out of your way to change this, you are safe.


### Text tools trust the user's input

*   The tools do not need to overcome user error.
    *   It is not the program's job to "fix" mistakes made by the user.
    *   The best thing to do is report the error and quit.
*   It is the user's responsibility to provide correct file names.
    *   Do not try to make the user's life easier by assuming that all files live in a particular directory, or that all filenames will end in `.txt`.


### Command-Line Interface

This program will be run from the command line like so:

    $ python src/tt.py TOOL [OPTIONS] FILENAME...

This form of command should feel familiar to you after having used `git` over the past weeks.

0.  `python` invokes the Python interpreter
    *   Some of you will need to write `python3` instead
1.  Next comes the name of the driver program `src/tt.py`
2.  `TOOL` is the name of one of the available text tools listed in the table below.
    *   The name of the tool must be spelled exactly as shown in the table, in lower-case.
3.  Some tools may take an option, which is entered in the position of `[OPTIONS]`
    *   Note that the user does not type the square brackets; in documentation for command-line programs brackets indicate optional arguments
4.  Each tool must be given at least one filename.
    *   The ellipsis means that one *or more* filenames are acceptable.

*   Your program **must not** prompt the user for any input.
    *   In other words, your program **will not** use `input()`.
*   When `src/tt.py` is launched without naming a `TOOL`, or when an invalid `TOOL` is given, a usage message is printed and the program immediately quits.
    *   This has already been written for you.
    *   Study the starter code to find it and learn how to use it.


### PyCharm Run Configurations

When PyCharm runs your code, it does so through a command line.  To help PyCharm form the correct command, fill in the *Run Configuration* dialog like so:

*   Set **Script path** as the path to the driver program `src/tt.py`
*   Text corresponding to `TOOL [OPTIONS] FILENAME...` goes into **Parameters**
*   Use your default Python interpreter as the **Python interpreter**
*   Leave **Interpreter options** empty
*   Set the **Working Directory** to your repository's *root directory*

Create as many run configurations as you want.  One run configuration may invoke the `grep` tool at the click of a button, while another configuration launches the `paste` tool.  Make different run configurations to run the same tool with different input files.


### Handling Errors

The principle we follow for this assignment is to closely mimic the classic Unix text tools.  In situations when they would crash, so, too should your program.

*   Ordinarily, we strive for programs that do not crash
    *   programs that crash *unexpectedly* face a 50% penalty
    *   However, there are exceptions to this rule in situations when your program *should* crash:
        *   In such cases you are allowed to let fatal errors raised by Python's internal functions (such as `open()`) to occur.
        *   For example, when a file is inaccessible or non-existent, you should just allow `open()` to crash your program.
        *   **Do not import `os` to use `os.access()` in an attempt to prevent errors related to inaccessible files**.  I enforce a [penalty](./Rubric.md#penalties) for importing extraneous modules.
    *   There are two reasons for this rule:
        1.  Python's default error messages are very informative.
        2.  In these situations there isn't any point in trying to go on; the best thing to do is quit.
    *   Read the sections below as well as the [examples](./examples/) so you'll know when it's okay to let your program crash!
*   Some errors are easily detected in the `src/main.py` driver and may be dealt with immediately before calling on one of the functions contained in a module.
    *   For example, the best place to decide whether or not a valid `TOOL` has been named is in the driver.
*   Other errors are best left to each individual tool.
    *   For example, the `head` tool may be given an `OPTION` formed from two arguments: a flag `-n` followed by a space, then a number.  It is an error to supply `-n` without a number.  It is also an error when `-n` is followed by a *non-positive* number.  The natural place to handle this is in the `head()` function.
    *   Including this logic in the driver will make it more complex than it needs to be.

Rely on the `usage()` function defined in `Usage.py` to display consistent error messages.  The usage text in this file is provided to guide you about the correct form of command-line arguments.  Before you ask a question about how a tool is to behave, make sure that your answer isn't already spelled out in `Usage.py`.


#### Too few or invalid arguments

When the `src/tt.py` driver is invoked with an empty or invalid `TOOL` name the `usage()` function should be called with no arguments to output the full usage message:

    $ python src/tt.py
    Error: Too few arguments

    Python Text Tools Usage:
    ========================
    ...


    $ python src/tt.py derp
    Error: derp is not a valid subcommand

    Python Text Tools Usage:
    ========================
    ...


#### File access errors

Let Python's `open()` function signal an error when a non-existent file is named

    $ python src/tt.py cat data/DOES_NOT_EXIST
    Traceback (most recent call last):
      File "src/tt.py", line 69, in <module>
        cat(sys.argv[2:])
      File "/home/fadein/cs1440-falor-erik-assn2/src/Concatenate.py", line 4, in cat
        f = open(fl, 'r');
    FileNotFoundError: [Errno 2] No such file or directory: 'data/DOES_NOT_EXIST'


Let Python's `open()` function signal an error when a directory (or another non-file object) is named instead of a file:

    $ python src/tt.py cat .
    Traceback (most recent call last):
      File "src/tt.py", line 19, in <module>
        cat(sys.argv[2:])
      File "/home/fadein/cs1440-falor-erik-assn2/src/Concatenate.py", line 4, in cat
        f = open(fil, 'r');
    IsADirectoryError: [Errno 21] Is a directory: '.'


Let Python's `open()` function signal an error when the user does not have permission to access a file:

    $ python src/tt.py cat /dev/mem
    Traceback (most recent call last):
      File "src/tt.py", line 19, in <module>
        cat(sys.argv[2:])
      File "/home/fadein/cs1440-falor-erik-assn2/src/Concatenate.py", line 4, in cat
        f = open(fil, 'r');
    PermissionError: [Errno 13] Permission denied: '/dev/mem'


#### Too few or incorrect arguments to a subcommand

Your program must detect and report the case where too few arguments are given; at a minimum the name of one input file is required for all tools.  Call the `usage()` function with the `error` and `tool` keyword arguments to print an appropriate error message.

For example, when the `cat` tool is invoked without at least one filename, call `usage(error="Too few arguments", tool='cat')` to display the following message:

    $ python src/tt.py cat
    Error: Too few arguments

    tt.py cat|tac FILENAME...
            Concatenate and print files in order or in reverse



## The `>` redirection operator is a feature of your shell

As you study the files in [examples](./examples) you will come across some commands that use the `>` symbol.  This is explained in detail in a [Shell Tutor lesson](../shell-tutor/1-redirection.sh).

In a nutshell, `>` is the *redirection operator*.  It causes output that would be printed to the screen to instead be *redirected* into a file.  It is a feature of your shell and is *not* something that you have to make work in Python.  In fact, neither the redirection operator nor the associated filename appears in `sys.argv`; your Python program never knows that its output is being redirected.



## Don't use evil `eval()`

This assignment requires you to convert strings such as `"10"` into integers.  While you were taught to do this with `eval()` in CS 1400, it is time to grow up and do this the big-kid way with type constructors:

*   `int()` for integers
*   `float()` for real numbers
*   `complex()` for complex numbers

The problem with `eval()` is that it is just **too** powerful.  `eval()` will run *any* Python expression, including expressions that can erase your hard drive or download a function.  Your program accepts input from users, and users should never be trusted.  For this reason use of `eval()` is considered [poor practice](https://thepythonguru.com/python-builtin-functions/eval/#evil-eval).
