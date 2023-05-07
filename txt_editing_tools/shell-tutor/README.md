# Shell Tutor

Interactive Unix command shell tutorials that accompany the CS1440 Text Tools assignment.

## Table Of Contents
*   [Quickstart](#quickstart)
*   [Submission Instructions](#submission-instructions)
*   [Lesson Contents](#lesson-contents)
*   [Hints](#hints)
*   [Reporting Bugs](#reporting-bugs)

## Quickstart

*In the code examples below a dollar sign `$` represents the shell prompt.  This is to distinguish commands that you will input from their output. Do not type the `$` when you run these commands yourself. Output may be replaced by `...` to shorten these instructions.*

0.  Clone this repository and set up the remotes properly, according to the instructions in the [project root README.md](../)
1.  Use `cd` to enter the `shell-tutor` directory in this repository
    ```
    $ pwd
    .../cs1440-assn2
    $ cd shell-tutor
    $ pwd
    .../cs1440-assn2/shell-tutor
    ```
2.  Execute one of the `.sh` files from Bash or Zsh
    ```
    $ ./0-shortcuts.sh
    Tutor: Shell Shortcuts Lesson
    Tutor: 
    Tutor: In this lesson you will learn
    Tutor: 
    Tutor: * To use the shell's History to re-use commands you have already typed
    Tutor: * Line editor shortcuts to easily navigate and change command lines
    Tutor: * How Tab completion can write parts of your commands for you
    Tutor: 
    Tutor: Let's get started!
    ```
    *   **NOTE FOR UBUNTU USERS:** Your shell's default `sh` is not compatible with the shell tutor. You will have to launch the shell tutor lessons by typing `bash ./0-shortcuts.sh` instead of just `./0-shortcuts.sh`.

## Submission Instructions

When you finish the shell tutor lessons provided here, you will run the `./make-certificate.sh` script. This script will produce a `certificate.txt` file in this directory. Be sure to `git add`, `git commit`, and `git push` this `certificate.txt` file in your assignment 2 repository, and your grader will be able to assess that you have completed the shell tutor lessons associated with this assignment.

## Lesson Contents

You can always view a brief summary of the lesson by running `./LESSON_FILE.sh -h`.

*   `0-shortcuts.sh`
    *   The shell's command history
    *   Line editor shortcuts
    *   Tab completion
*   `1-redirection.sh`
    *   Redirect shell command output to a file
    *   Append shell command output to a file
    *   The STDOUT file descriptor
    *   The STDERR file descriptor
    *   Control printing to STDOUT or STDERR in Python
    *   Remove unneeded command output by sending output to `/dev/null`

## Hints

*   Interact with the tutor through the `tutor` command.
    *   When you get lost or forget what to do next, run `tutor hint`.
*   You can leave the tutorial early by exiting the shell.  There are many
    ways to do this:
    *   The `exit` command
    *   The `tutor quit` command
    *   Type the End-Of-File character (EOF) `Ctrl-D`
*   Lessons are designed to be brief; the average student will finish a lesson
    in 20 minutes.  If you are stuck longer than 20 minutes you can seek help
    from the instructor, TAs or CS Coaching Center.


## Reporting Bugs
*   When you encounter a problem with a lesson, please send a bug report so I can fix it
    *   Run `tutor bug` 
        *   Scroll up a before the problem started and copy the text on your terminal, including these details:
        -   Which lesson you are running
        -   Which step of the lesson you were on
        -   The instructions for that step
        -   The command you ran
        -   The erroneous output
        -   The output of the `tutor bug` command
*   Send this text to me in an email: `erik DOT falor AT usu DOT edu`
    *   **Do not** send screenshots; plain text is much easier to work with
    *   **CC Jaxton Winder on the email as well** : `jaxton DOT winder AT usu DOT edu`