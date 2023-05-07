# CS 1440 Assignment 2: Text Tools - *Optional* Test Scripts

This directory contains simple *shell scripts* to help you conveniently test your Text Tools.

Compare the output produced by these programs with what is shown in the [Examples of Expected Output](../instructions/examples).

## IMPORTANT!!

*   These scripts must be run from the project's root directory!
*   Do not re-name your Text Tools main driver code program `src/tt.py`!


## Configuration With `python.conf`

Because everyone at DuckieCorp uses a different system, the command for Python 3 might differ.  The file [`python.conf`](python.conf) tries to auto-detect the right Python interpreter for your computer.  If it fails, you should edit it to use the same Python command you use on the command line.  **Do not add any white space around the `=` sign in this file!**

In the scripts, you may see the line `source scripts/python.conf`. This is where the shell script reads the `python.conf` file, sets the variable `PY_CMD`, and allows access to the set variable with `$PY_CMD`.

## Running The Scripts

**These scripts are meant to be run from the project's root directory.** Your *current working directory* must be at the lowest level of the assignment 1 repository; outside of `src`, `scripts` and `data`.  These scripts assume the Text Tools driver code is located in `src/tt.py`.

The scripts can be run 2 different ways:
*   `./scripts/testUsage.sh`
    *   If this doesn't work, you may need to `chmod +x` the specified script to mark it as an *executable*
*   `bash scripts/testUsage.sh`

Executing the `testUsage.sh` script should produce output like the following:

```
~/cs1440-falor-erik-assn2 $ ./scripts/testUsage.sh
TEST$ python src/tt.py
Python Text Tools Usage
=======================

tt.py cat|tac FILENAME...
    Concatenate and print files in order or in reverse
...
```

## Provided Scripts
*   [`testUsage.sh`](testUsage.sh)
    *   Test various inputs to `tt.py` that should produce usage messages for `tt.py` and/or the `tool` 
*   [`testCat.sh`](testCat.sh)
    *   Test the `cat` tool against valid input and non-existent files
*   [`testTac.sh`](testTac.sh)
    *   Test the `tac` tool against valid input and non-existent files
*   [`testHead.sh`](testHead.sh)
    *   Test the `head` tool against valid input and non-existent files
*   [`testTail.sh`](testTail.sh)
    *   Test the `tail` tool against valid input and non-existent files
*   [`testGrep.sh`](testGrep.sh)
    *   Test the `grep` tool against valid input and non-existent files
*   [`testWC.sh`](testWC.sh)
    *   Test the `wc` tool against valid input and non-existent files
*   [`testSort.sh`](testSort.sh)
    *   Test the `sort` tool against valid input and non-existent files
*   [`testPaste.sh`](testPaste.sh)
    *   Test the `paste` tool against valid input and non-existent files
*   [`testCut.sh`](testCut.sh)
    *   Test the `cut` tool against valid input and non-existent files
*   [`testInvalidUsage.sh`](testInvalidUsage.sh)
    *   Test a few different tools with invalid invocations

## Output Result To External File
If you'd like to store the output of one of these test scripts into an external file, use the shell redirection operator `&>`. In general, output redirection on the shell is `[Command and arguments] &> OUTPUT_FILE_PATH.txt`. *Note: use the special `&>` redirection operator instead of `>` to combine ordinary output from `STDOUT` with error output from `STDERR` into the same file.*

```
~/cs1440-falor-erik-assn2 $ ./scripts/testUsage.sh &> UsageTest.log
~/cs1440-falor-erik-assn2 $ cat UsageTest.log
$ python src/tt.py
Python Text Tools Usage
=======================

tt.py cat|tac FILENAME...
    Concatenate and print files in order or in reverse
...
```

## Understanding Shell Scripts

For the curious, you will see these features in the provided shell scripts:

*   `#!/usr/bin/env bash`
    *   A special line called a *shebang*. Instructs the Operating System to execute this text file with the `bash` shell
    *   Not necessary for every shell script
*   `# ...`
    *   `#` introduces a comment, just like in Python
*   `source FILE`
    *   Read `FILE` and execute its contents as shell commands. *This sets the variable `PY_CMD=python` when we source the `python.conf` file.*
*   `PY_CMD=''`
    *   Variable assignment; assign the empty string to a variable called `PY_CMD`
    *   Like Python, assignments in the Shell use the `=` operator
    *   Unlike Python, white space *cannot* surround the `=` operator!
    *   It is common for the names of Shell variables to be *UPPER_CASE*
*   `$PY_CMD`
    *   Access the value stored in the `PY_CMD` variable
    *   `$` is used to *expand* a variable when you want to use its value
    *   Do not use `$` when *assigning* a value to a variable!
        *   Thus, `$PATH` expands to the value of the `PATH` environment variable
        *   `$PY_CMD` expands to the `PY_CMD` variable set in `python.conf`
*   `echo "TEST\$ ..."`
    *   Print the command that is to be run
    *   `\$` is needed to put a `$` character in a string literal, since `$` has special meaning in `*sh` scripting!
*   `$PY_CMD src/tt.py ...`
    *   Execute `src/tt.py` using your computer's preferred Python interpreter
