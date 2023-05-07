# CS 1440 Assignment 2: Text Tools

*   [Instructions](./instructions/README.md)
    *   [Examples of Expected Output](./instructions/examples)
    *   [Hints](./instructions/Hints.md)
    *   [Troubleshooting your program](./instructions/Troubleshooting.md)
    *   [Rubric & Penalties](./instructions/Rubric.md)
*   [*Optional* Test Scripts](./scripts/README.md)

*Note: this file is a placeholder for your own notes.  When seeking help from the TAs or tutors replace the text in this file with a description of your problem and push it to your repository on GitLab*

## Get the starter code

*   Assignment instructions, sample data files and example output are provided on the course GitLab server.
*   Clone this repository and use it as a basis for your work.
    *   Run each of these commands one-at-a-time, without the `$' (that represents your shell's prompt):
    *   Replace, `LAST`, `FIRST` and `USERNAME` with *your* own names.

```bash
$ git clone git@gitlab.cs.usu.edu:erik.falor/cs1440-falor-erik-assn2 cs1440-assn2
$ cd cs1440-assn2
$ git remote rename origin old-origin
$ git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-assn2.git
$ git push -u origin --all
```


## Overview

A client has sought DuckieCorp's services to process a large quantity of textual data.  Specifically, the data is in the form of a Comma Separated Values (CSV) file which is far too large to load as a spreadsheet in an application such as LibreOffice Calc or Microsoft Excel.

I explained to the client that it would be easier for them to install Linux and use its built-in text processing tools for this job.  Fortunately for our bottom line (and your job security), this client is adamant that installing Linux is out of the question.  Instead, DuckieCorp will recreate the classic suite of Unix text processing programs in Python.

I made a start at this project, but only got as far as creating a general outline and finishing the `usage()` routine before my other responsibilities at DuckieCorp became too great.  I will leave this project to you, my favorite intern, to complete.  If you do good work I am confident that this small job will turn into a standing contract.



## Objectives

-   Processing command-line arguments in `sys.argv`
-   Organize code into modules
-   Process string data with Python's built-in functionality
-   Efficiently process large quantities of data
-   Use the IDE's interactive debugger



## Shell Tutor Lessons

Included with this assignment are 2 new Shell Tutor lessons in [shell-tutor](./shell-tutor/).  Together they are worth 10 points.  Run `make-certificate.sh` and commit the resulting certificate file in the `shell-tutor` directory to pass this off.

You should complete the lessons sometime before you begin *testing* your text tools.  They will help you do that more effectively.

As always, if you run into a problem with the tutorial, run `tutor bug` and email the output to your instructor.



## Program Expected Behavior

Read the [example](./instructions/examples) files to see what a correct program's output might look like.  Test your program against the files under `data/` and compare your output to the provided examples.  Your program should match the example output in the essentials; extra leading or trailing white space is generally permissible, except where its presence changes the meaning of the output.

In the provided samples, lines beginning with `$` represent the command I typed into my shell.  When you run the same command you should not copy the `$`.
