# CS 1440 Assignment 3: Big Data Processing

*   [Instructions](./instructions/README.md)
    *   [Hints](./instructions/Hints.md)
    *   [Rubric & Penalties](./instructions/Rubric.md)
    *   [Installing the Text Tools](./instructions/Installing_Text_Tools.md)
    *   [How to Submit this Assignment](./instructions/How_To_Submit_Assignments.md)
*   [Testing Data](./data/README.md)
*   [Shell Tutor Lessons](./shell-tutor/README.md)

*Note: this file is a placeholder for your own notes.  When seeking help from the TAs or tutors replace the text in this file with a description of your problem and push it to your repository on GitLab*

## Get the starter code

*   Assignment instructions, sample data files and example output are provided on the course GitLab server.
*   Clone this repository and use it as a basis for your work.
    *   Run each of these commands one-at-a-time, without the `$' (that represents your shell's prompt):
    *   Replace, `LAST`, `FIRST` and `USERNAME` with *your* own names.

```bash
$ git clone git@gitlab.cs.usu.edu:erik.falor/cs1440-falor-erik-assn3 cs1440-assn3
$ cd cs1440-assn3
$ git remote rename origin old-origin
$ git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-assn3.git
$ git push -u origin --all
```


## Overview

Your last project was a great success! The customer was very pleased with their
new Text Tools and so impressed with the quality of your work that they have
decided to contract you to finish the entire project for them.

Your task is to analyze a large body of data and produce a report of the
findings.  This program summarizes national employment data collected by the
U.S. Bureau of Labor Statistics in 2021.  The report consists of two sections,
a summary across all industries and a summary across the software publishing
industry.  I worked with the customer far enough to develop the format of the
report.  It is your task to analyze a 493MB CSV file to pull out the data
needed by the report.



## Objectives

-   Use [Git tags](./instructions/README.md#following-the-software-development-plan) to mark development milestones
-   Learn how to process a large body of data
-   Use Python's built-in string operations
-   Research programming documentation
-   Reading, understanding, and following instructions
-   Using advanced data structures (list, dictionary, set)
-   Apply debugging techniques
    -   Direct debugging with the IDE
    -   Indirect debugging
    -   Wolf-Fence debugging



## Shell Tutor Lessons on using Git tags

Included with this assignment are 2 Shell Tutor lessons under
[shell-tutor](./shell-tutor/).  These lessons should be the **first thing** you
do on this assignment.

Together they are worth 10 points.  Run `make-certificate.sh` and commit the
resulting certificate file in the `shell-tutor` directory to pass this off.

As always, if you run into a problem with the tutorial, run `tutor bug` and
email the output to your instructor.



## Program Expected Behavior

Each subfolder of [data/](data) contains a file named `output.txt`.
Your program's output for that data set should match that file exactly.

Instructions are provided for creating testing data sets using the Text Tools
from Assignment #2.  These crafted input files will be the basis of your
testing efforts.
