# CS 1440 Assignment 4: Bingo! - How to Submit this Assignment


## Table of Contents
* [Your GitLab Account](#your-gitlab-account)
* [Repository Naming Convention](#repository-naming-convention)
* [Starter Code Repo](#starter-code-repo)
* [When to Submit Your Work](#when-to-submit-your-work)
* [Verify Your Submission](#verify-your-submission)
* [Python Version](#python-version)
* [Penalties](#penalties)


I am very particular about the format of your assignment submissions.

*   Yes, I have my reasons.
*   No, I do not make exceptions.
*   Failure to follow the assignment submission guidelines **will result in penalties**.

I have made it as easy as possible for your submissions to have the right form.  As long as you don't go out of your way to fight against it you'll be fine.

This document explains the rules that apply to all assignments.

<details>
<summary><strong>Rationale</strong></summary>

### Why am I so picky about how you submit your homework?

0.  **Programming is a very detail-oriented activity**.  The sooner you embrace this fact the happier you will be.
1.  In the workforce **your boss and coworkers will be just as picky as I am** about how you turn in your work, perhaps more so.  It is not good enough if your code works only on your computer.  Your work exists within a larger context that includes your team and your customers.  Being part of a team means following conventions so that everybody can be on the same page.
2.  In a class this large, **every second saved adds up**.  For instance, if it takes 60 seconds to figure out how to run every student's submission in a class of 180 students, then the graders will waste three hours just getting started.  There are seven assignments this semester, which means we collectively we would lose the equivalent of three whole work-days every semester on this trivial detail.

</details>



## Your GitLab Account

*   Unless otherwise instructed, all assignments are submitted to the [course GitLab server](https://gitlab.cs.usu.edu).
    *   This means that there is nothing for you to do on Canvas with respect to submitting assignments.
    *   Your score and the grader's comments the *are* posted on Canvas.
*   Create an account on my GitLab server and _not_ the public GitLab service at https://gitlab.com.
    *   Look for Old Main ![Old Main](assets/oldMain.png "Old Main") instead of the GitLab logo ![GitLab logo](assets/gitlab-icon-rgb.png "GitLab logo") in the site's navigation bar.
    *   Use your school-supplied email address to sign up.
    *   Put your first name and last name into your GitLab username to make it easy for us to identify your account.
*   Other online git services (i.e. GitHub, Bitbucket, Sourcehut) may not be used in this course.
    *   To prevent academic dishonesty, submissions made to public git repositories cannot be accepted and will receive zero points.
    *   Please talk to me if you would like to include your course work as part of your online portfolio after the semester has concluded.
*   I only grade code found in your repository's default branch.
    *   If you don't know what this means it doesn't apply to you ;)
    *   You may freely use other branches to experiment as you work on the assignment.
    *   Pushes to non-default branches are not taken into consideration when deciding if your work is on-time or late.


<details>
<summary><strong>Rationale</strong></summary>

### Why do I make you use Git?

Git is something that I wish somebody taught me when I was a student.

Whenever I speak to industry professionals one of the very first questions they ask me is "do you teach your students how to use git?"  The [Git Software Configuration Management system](https://git-scm.com/) is the most popular version control system in the world today.  Learning git in this class immediately puts you at an advantage over your peers who study in other CS programs:

*   Knowing git = less time spent training you on-the-job.
*   You can post your portfolio to popular online code-hosting services such as GitHub, GitLab, Bitbucket, etc.
*   Version control will help you stay organized in your other classes.

</details>



## Repository Naming Convention

Your work is submitted by using git to push code to repositories (a.k.a. "repos", a.k.a.  "projects") on GitLab.  It is very important that the name of your repo fits this pattern:

`cs1440-lastname-firstname-assn#`

*   Use lowercase to name your repo.
*   Use hyphens `-` to separate words.
    *   **Do not** use underscores `_`, dots `.` or other punctuation.
*   Name your submission such that _LastName_ and _FirstName_ correspond to your "Full Name" in Canvas.  Find your "Full Name" in Canvas by browsing to `Account -> Settings`.
    *   Two first or last names can be used; separate them with hyphens `-`.
    *   You do not need to include your middle name, unless there is a classmate who shares your first and last name.
*   Name your repo with the correct course number.
*   Likewise, you must specify the assignment number exactly as `assn#`
    *   **Do not** use any other variation of the word "assignment".

When you get these details wrong it appears to me that you made no submission.

On the other hand, you may create repositories for your other classes on my GitLab server.  This naming convention avoids confusion between assignment submissions in this course and your repositories for other courses.


#### Good repo names:

*   `cs1440-smith-jane-assn1` (Jane Smith's Assignment #1)
*   `cs1440-jones-bill-assn4` (Bill Jones's Assignment #4)
*   `cs1440-rubio-gould-teresa-assn2` (Teresa Rubio-Gould's Assignment #2 - multiple names are OK)

#### Bad repo names:

*   `cs1000-smith-jane-assn1` (invalid course number: this is **cs1440**, not **cs1000**)
*   `1440-jones-bill-assn4` (invalid course number: it must begin with **cs**)
*   `cs-1440-jones-bill-assn4` (invalid course number: spell it as **cs1440**, not **cs-1440**)
*   `cs1440-rubio-gould-teresa-ass2` (**assn#** is spelled wrong)
*   `cs1440-rubio-gould-teresa-assn-2` (**assn#** is spelled wrong)
*   `cs1440-rubio-gould-teresa-assign2` (**assn#** is spelled wrong)
*   `cs1440-pixelwarrior5010-assn2` (**pixelwarrior5010** isn't your "Full Name" in Canvas)


<details>
<summary><strong>Rationale</strong></summary>

0.  Naming your GitLab project with your Canvas "full name" avoids confusion.  Remember that some of our graders are not native English speakers and don't know that `Dick == Richard`, `Lexi == Alexandria`, `Billy == William`, `Chuck == Charles`, `Becky == Rebecca`, etc.
1.  To deal with the large number of submissions I wrote a program to find your repo by its URL.  The naming convention is rigid because it is a simple program and is very easily confused.
2.  In GitLab your project's *name* can differ from its *path* or URL.  It is possible to fix mistakes in the naming your repo.  Just make sure that you change its **Path** instead of its **Name**.  *See below*

</details>


### Changing your repository's URL on GitLab

If you gave your repo the wrong name, you can fix it in GitLab before the due date and receive **no penalty**.

0.  Open the repo's settings in GitLab by hovering over the gear icon at the bottom of the left sidebar and clicking `General`
1.  Scroll all the way to the _bottom_ and expand the **Advanced** section.  _Do not bother changing the **Project Name** that you see at the top of this page!_
2.  Scroll all the way to the _bottom_ of the **Advanced** section until you see a box titled **Change path**.  Put the correct name into this box and save your changes.
3.  Back on your PC update your repo's remote URL.  Assuming your GitLab remote is nicknamed `origin`, a command like this will update the URL (substitute your own details in this command):
    ```
    git remote set-url origin git@gitlab.cs.usu.edu:YOUR_USERNAME/cs1440-YOUR-NAME-AND-ASSIGNMENT
    ```
4.  After changing the path you *must* make another push before my submission collection program can notice the change.  You may need to edit a file and create a new commit so that you can do a push.  If you don't know what to change, just make a small, cosmetic change in one of the Markdown files.



## Starter Code Repo

In this class assignments will begin from a starter code repo.

*   **Do not start from scratch**.  Clone the starter code repo and continue from there.
*   The starter code includes **instructions**.  Read them before you write.
*   The starter code repo contains **required files that are already in the correct locations**.  Unless you are told otherwise, do not delete, rename or move these files.
*   A well-organized submission makes it **easy for us to help you** and grade your work.
*   Some files and directories are **required** to be present.
*   Some files and directories must **NOT** be part of your submission.
*   **Do not** remove or re-arrange files given to you in the starter code unless specifically told to do so.

This is what a good submission would look like:

```
cs1440-jamieson-phil-assn6/
|-- .gitignore
|-- README.md
|-- src/
|   |-- main.py
|   |-- Fractal.py
|   |-- Mandelbrot.py
|   |-- Gradient.py
|   `-- Grad2Colors.py
|-- demo/
|   `-- interactive.py
|-- data/
|   |-- burningship.frac
|   `-- spiral.frac
|-- test/
|   |-- test_mandelbrot.py
|   `-- test_julia.py
|-- instructions/
|   |-- README.md
|   |-- Hints.md
|   `-- Rubric.md
|-- lsn/
|   |-- README.md
|   |-- 0-ASCIIChars/
|   |-- 1-TextProcessing/
|   `-- 2-FileOperations/
`-- doc/
    |-- Signature.md
    |-- Plan.md
    |-- UML.png
    `-- Manual.md
```


### Files and directories your repo _MUST_ contain

0.  A `README.md` in the top-level directory.
    *   This file is *not* read-only, and you *may* modify it.
    *   If you have any special instructions or explanations for your grader, put them at the top.
1.  A file named `.gitignore`.  This file may be hidden from file listings in the shell.
    *   The contents of `.gitignore` are explained in detail below.
2.  `src/`
    *   Contains your source code
3.  `instructions/`
    *   Contains my instructions to you
    *   Don't modify files in this directory; consider this area read-only
4.  `doc/`
    *   Contains documentation written by you.  Edit the files provided by us, and add new ones.
    *   UML diagrams, user manuals, and other non-code artifacts you create belong here.
    *   `Plan.md` - your *Software Development Plan*, a.k.a. SDP.
        *   This is just a plain-text file that you should write in your code editor.  Do not replace this file with an MS-Word `.docx`, PDF, or file in some other format.
        *   The SDP is a living document.  Update it as you work.
        *   Cite external sources used in your submission (e.g. Stack Overflow, Wikipedia, etc.).
    *   `Signature.md` - the *Sprint Signature*
        *   Record a **brief** log of your accomplishments every day that you worked on the assignment.
        *   One or two sentences per day suffice.
        *   Longer explanations should go into the SDP.
    *   Keep this directory **tidy**.
        *   Delete extraneous and out-of-date files so your grader doesn't have to waste time figuring out what's what.
        *   There should be only ONE `Plan.md` and ONE `Signature.md` per assignment.


### Files and directories your repository _MAY_ contain

0.  A directory called `data/` if extra data files are used by your program.
1.  A directory called `test/` containing any run-able tests for your program.
2.  A directory called `demo/` containing demonstration code for your
3.  A directory called `lsn/` containing code lessons.
4.  Any other subdirectories needed to organize your work as you see fit.


### Files your repository _MUST NOT_ contain

0.  Directories containing pre-compiled files or other generated files created by your IDE or build tools (e.g. `venv`, `*.pyc`, etc.).  Exceptions to this are your IDE's project subdirectory:
    * `.idea/` created by PyCharm.
    * `.vscode/` created by Visual Studio Code.
1.  Zip files or archives.
2.  Backup files or folders.
3.  Screenshots.
4.  Any other detritus left behind from your experimentation.
5.  Extremely large files.  What is considered "extremely large" depends upon the project, but a good rule of thumb is to avoid committing files larger than 20 megabytes.

**Before you make your final submission, clean up your repository!**


#### Block unwanted files with `.gitignore`

The `.gitignore` helps you avoid committing unwanted files and directories to your git repo.  `.gitignore` is a plain text file.  Each line specifies a filename pattern that git will ignore.

The following `.gitignore` file is suitable for assignments in this course:

```
venv
.DS_Store
__pycache__
*.pyc
*.csv
*.zip
*.bak
*.png
```

Assignments beginning from starter code already include this `.gitignore` file.  If you must create this file yourself, understand that Git is *very* particular about the spelling of this file's name.  It must be spelled *exactly* as `.gitignore`:

*   The file name starts with a dot `.`
*   All lowercase
*   No file extension at the end

Git does *not* recognize these files as an ignore file:

*   `gitignore`
*   `.gitignore.txt`
*   `.Gitignore`
*   `.GITIGNORE`


Many text editors on Windows cannot create files with a name beginning with `.`.  Some editors will automatically add an extension (such as `.txt`) to your new file's name.  Any deviation prevents git from recognizing this file.  The most convenient way to create these files on Windows is from the Git Bash command line using the `nano` text editor by running this command:

```
nano .gitignore
```

Copy the contents shown above, one entry per line.  When you are done press `Ctrl-X` (a.k.a. `^X`) to exit Nano and follow the on-screen prompts to save your file.


<details>
<summary><strong>Rationale</strong></summary>

### What difference do the names and locations of my files make?

*   The starter code repo is organized to help you quickly find the files you need to read or edit.
*   Your boss and coworkers will expect you to maintain the organization of code that you write and maintain at your job.
*   This organization prevents guesswork on the part of tutors, TAs and the instructor when you have questions about your code.  We will be able to run your program without fuss and will see exactly the same output on our computer that you get on yours.
*   This layout facilitates quick and efficient grading, freeing us to give you more detailed feedback on your submissions.


### Why do I make you write **doc/Plan.md**?

*   How do you know what code to write if you don't know what program you are creating?
*   You write this file for *you*.  Failing to plan is planning to fail.
    *   Students who write detailed plans learn more and get better scores.
    *   Students who write the SDP as an afterthought right before they turn in an assignment have just wasted hours of their precious lives.
*   I cannot make you into a good programmer; that is something you must do for yourself.
    *   The exercise of writing this document forces you to be thoughtful and intentional about programming.  That is how you will become a good programmer.


### Why do I make you write **doc/Signature.md**?

*   This daily summary helps you stay on-task:
    *   If your daily summary consists of pointless fiddling, you will be more focused tomorrow.
    *   Reviewing the sprint signature helps you recognize when you are getting stuck in the project.
*   Writing a daily log encourages you to work at least a little bit every day, helping you become consistent.

Related question: *Don't git commit messages make this document redundant?*

No.  Git commit messages serve a different purpose than the Sprint Signature.

*   Git commit messages describe just a small portion of your work, often just a few lines of code.
    *   You should make several commits each day, each with its own message.
*   The sprint signature captures a big-picture summary of your daily work.


### Do you even look at these files?

Yes.

</details>



## When to Submit Your Work

_Submitting assignments late results in penalties of up to 100% of a submission's grade_

*   I design assignments around a schedule that I expect you to follow.
    *   When I give you two weeks to work on an assignment it is because I sincerely believe that you need the full 14 days to complete it.
    *   Procrastinators will struggle in my class.  Now is the time to learn how to manage your time.
*   Some assignments build upon previous submissions.  Manage your time wisely so you can keep up.
*   Assignments are due by 11:59:59 PM on the posted due date according to the clock on my GitLab server.
*   No submission is accepted after 48 hours past the due date.
*   A submission arrives when it is *pushed* to the GitLab server.
    *   Commits pushed _after_ the due date are late.
    *   Commits bearing timestamps _before_ the due date but are *pushed* to the GitLab server _after_ the due date are considered late.

|  Lateness   |            Penalty            |
|-------------|-------------------------------|
| < 24 hours  | 25% of total points possible  |
| < 48 hours  | 50% of total points possible  |
| >= 48 hours | 100% of total points possible |

Exceptions to the above can only be made in the event of school-sanctioned travel or for a _serious, unexpected_ emergency.  Inform the instructor as soon as you can, preferably in advance, to work out an arrangement.


### Which clock judges lateness?

The clock on **gitlab.cs.usu.edu** keeps the official time for the class.  When you push code to the server you will see a receipt in your console:

```
***********************************************************************
*           __  ________  __  _____                ____    _          *
*          / / / / __/ / / / / ___/__  __ _  ___  / __/___(_)         *
*         / /_/ /\ \/ /_/ / / /__/ _ \/  ' \/ _ \_\ \/ __/ /          *
*         \____/___/\____/  \___/\___/_/_/_/ .__/___/\__/_/           *
*                                         /_/                         *
*  ,/         \,                                                      *
* ((__,-"""-,__))                                                     *
*  `--)~   ~(--`                                                      *
* .-'(       )'-,                                                     *
* `--`d\   /b`--`  Big Blue says:                                     *
*     |     |                                                         *
*     (6___6)  Your submission arrived Fri 28 Aug 2020 21:17:25 MDT   *
*      `---`                                                          *
*                                                                     *
***********************************************************************
```

The timestamp in this receipt comes from the GitLab server's clock and is the time your submission's arrival is judged by.  If you don't see this receipt, make sure that you are pushing your code to the right GitLab server.


### The Grading Gift

Each student is allowed **one** late submission per semester without penalty and without question.

*   Your assignment **must** be submitted within 48 hours of the due date.
*   The Grading Gift covers **late** submissions only.  It cannot be used to make up points for code that is incomplete or has errors.
*   The Grading Gift **may not** be used on the final assignment.
*   Send an email **to me and to the graders** expressing your intent to use the Grading Gift.
    *   This email must be sent **before** the 48 hour extension period has passed.
    *   You cannot retroactively ask to use the Grading Gift beyond this point.
    *   If you miss this deadline, **email Erik directly**.
*   You do not need to tell us why you are using the Grading Gift.  In fact, we don't want to know.


<details>
<summary><strong>Rationale</strong></summary>

*   Programmers are notorious for failing to meet deadlines.  I want to destroy that stereotype.
*   However, everybody has a bad day now and then.  The Grading Gift lets you gracefully recover when this happens to you.

</details>



## Verify Your Submission

Part of an assignment's score depends on the performance of your code (the **implementation**), and the rest depends on the quality of your documentation and other artifacts.

*   You are graded on what you submit, not on what you *meant* to submit.
    *   It is solely **your** responsibility to ensure that your submission is complete, correct, and on-time.
    *   Your submission should make a convincing argument to me and the graders that you have mastered the concepts of the assignment.
*   Plan enough time to double-check your work *before* and *after* you submit.
    *   Nobody likes surprises.  Test your program frequently!
    *   Document your test cases in your SDP.
*   Test your program from the command-line.
    *   It is not good enough if it only works in your IDE.
    *   It is not good enough if it works on your computer; it must work on your grader's computer, too.


### If your program crashes when your grader runs it...

*   ...but only sometimes, or they can easily fix it
    *   you will receive, at most, half-credit for your **implementation**
*   ...and they cannot quickly figure out why
    *   you will earn 0 points for your **implementation**


### How to verify your work

Sometimes your repo contains extra files that you did not commit.  When we clone your repo these files are missing, causing your program to fail in unexpected ways.

An easy way to avoid this is to re-clone your repo from GitLab into a fresh location.  This will let you experience your submission as the graders will see it.

*   Navigate your shell into a different directory and use `git clone` to download your repo anew.  `git clone` takes a URL as an argument, which you can find by running `git remote -v` from your original repo.
*   Prevent *gitception* by taking precautions to avoid running `git clone` while already in a git repo.  *Always* run `git status` before using `git clone` or `git init`!

Before using `git clone` you want `git status` to give this error:

```
$ git status
fatal: Not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
```

Thoroughly test this fresh copy of your program:

*   Run your program from the command-line instead of your IDE; we don't use the IDE to grade your program.
*   Run the command-line examples shown in the instructions.
*   Run any tests included with the starter code.
*   Run through the test cases you described in the **Testing** section of your SDP.



## Python Version

*   Graders will run your code against the official distribution of Python version 3.8 or greater from https://python.org
*   Python version 2 has reached its end of life.
*   Code written for Python 2.x is not acceptable in this class.

For this class you must either:

*   Install Python version 3.8 or greater on your own computer
*   Find a computer with the correct version of Python
    *   Computers in CS labs and the Engineering Computer lab have the correct version of Python.


### How can I tell if I have the right version of Python installed?

Run `python --version` from the command line:

```
$ python --version
Python 3.8.2
```

If this reports a version number beginning with 2, run `python3` instead:

```
$ python3 --version
Python 3.8.2
```



## Penalties

Every DuckieCorp project is expected to meet a basic standard of quality.  Penalties are applied to submissions that fail to clear this low bar.  This list is not exhaustive; individual assignments are subject to extra penalties.


### Project Layout

0.  **-10 pts** Name of GitLab project is incorrect
1.  **-10 pts** Project is not a clone of the starter code repository
2.  **-10 pts** Required files and directories are missing, renamed or moved from their expected location
3.  **-10 pts** Forbidden files or directories are present
4.  **-10 pts** The project's `.gitignore` is missing or corrupted, even if no forbidden files or directories are present
5.  **-25%** Submission is less than 24 hours late
6.  **-50%** Submission is between 24 and 48 hours late
7.  **-100%** Submission is more than 48 hours late


### Modules and Functions

0.  **-10 pts** A module fails to be imported due to misspelling or incorrect capitalization
1.  **-10 pts** Program attempts to import a module from the `src.` package
    *   This is the result of a PyCharm misconfiguration
2.  **-10 pts** `eval()` or a similar function is used by your program
    *   Use type constructor functions such as `int()` and `float()` instead
3.  **Varies** A library which the grader doesn't happen to have installed is imported
    *   The resulting `ModuleNotFoundError` is treated as a crash and penalized accordingly
4.  **-20 pts** A library not permitted by the instructions is used, but doesn't result in a crash


### Files and Paths

0.  **-10 pts** Program opens files with hard-coded paths, or otherwise does not function when run from certain directories
    *   _Note: module names in `import` statements do not count as "hard-coded"_
1.  **-10 pts** One or more files are not closed after being processed in _ordinary_ situations
    *   In the event of an error your program will display an error message and immediately exit; in such cases you do not need to take special measures to close files
2.  **-10 pts** External programs are called upon to do any work
    *   Do not use `os.system()`, `subprocess`, `pipes` or similar functions and libraries
    *   Write a pure Python solution, not a script that leverages external programs
