# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

*   Rewrite the instructions in your *own words*
    *   What does the solution *need to have* or *surround* conceptually?
    *   What does a good solution *look like*?
*   List the things that you *already* know how to do
*   Write down any *challenges* you anticipate

---------------------
### Creating the text editing tools
#### Step one cat/tac
 * For *cat* we will create a program that can take any number of files and return them combined.
 * For *tac* do this but reverse the order in which you print the lines of each file.

#### Step two wc/head
* For *wc* create a program that counts lines words and bytes for each file and displays a total.
* For *head* create a program that displays the first ten lines of all files unless assigned otherwise. 

#### Step three tail/sort/grep
* For *tail* we will create a program that displays the first ten lines of all files unless assigned otherwise.
* For *sort* create a program that takes all files and sorts them all collectively into using ascii character order.
* For *grep* create a program that identifies a string pattern and returns the lines that the pattern was found on.
#### Step four cut/paste
* For *paste* create a program that coma separates each file assigned as an argument as rows and returnes the file as a csv.
* For *cut* create a program that prints specific columns from a csv file.
## Phase 1: System Analysis *(10%)*

*   Considering the overall program:
    *   List all kinds of *input* taken in by the program
    *   Describe what form its *output* will take
*   Write brief descriptions of *some* key functions your program may need
    *   Write the function's *name* its *inputs*, and *outputs*
    *   Explain what each function will do in *one sentence*
*   Use English; **NO CODE YET**
----------------------------------
### Inputs and Outputs
#### cat/tac
* *cat()* input(files) output(annealed files)
* Puts multiple files together or prints single file.
* *tac* input(files) output(annealed files)
* Puts multiple files together or prints single file backwards line by line.
#### wc/head
* *wc()* input(files) output(lineCount, wordCount, byteCount, Totals)
* counts multiple files lines, words, and bytes prints them and their totals added up over multiple files.
* *head* input(files) output(annealed files)
* Puts multiple files together or prints the first 10 lines or number specified.
#### tail/sort/grep
* *tail()* input(files, numLines) output(last 10 lines, unless specified)
* prints the last 10 lines of files unless specified otherwise.
* *sort* input(files) output(sorted lines)
* Puts multiple files together and sorts them using ascii order.
* *grep()* input(files, and search) output(related lines)
* searches for lines that have the search query in them and prints them.
#### cut/paste
* *cut()* input(files, columns) output(columns)
* prints the columns in the cvs file.
* *paste()* input(files) output(cvs file)
* prints a cvs format file by making each file into a column separated by comas.


## Phase 2: Design *(30%)*

*   **DO NOT COPY AND PASTE YOUR PYTHON CODE HERE!!!**
*   Write *pseudocode* that captures how each function works
    *   **Pseudocode != source code**
    *   If we find too much finished code here, *you will receive a zero*!
    *   It should look like *basic English* with extra indentation
*   Explain what happens to your functions in the face of *good and bad input*
    *   Make a note about *bad inputs* down in **Phase 4**; these will become your *test cases*
--------------------------------
### Functions to write
#### cat()
    opens files
    reads files into variable
    print(variable)
    close file
#### tac()
    opens files
    reads files into a list
    reverse the list
    for every line in list
        print(line)
    close file
#### head()
    opens files
    reads files into a list
    for line til line 10(or specified)
        print (line)
#### tail()
    opens files
    reads files into a list
    get length of file list
    go to 10(or specified) lines above end of file
    for line til line 10(or specified)
        print (line)
#### wc()
    opens files
    for file in files
        count lines in file
            count words in line
            count characters in line
    print (count for each file, and total)
#### sort()
    opens files
    reads files into a list
    sorts files by ascii order
    prints(list)
#### grep()
    for file in files
        opens files
        reads files into a list
        for line in file length
            iterate through characters untill you fine the input.
        print(line)
#### cut()
    for file in files
        opens files
        reads files into a list
            iterate through column(selected)
        print(column)
#### print()
    for file in files
        opens files
        reads files into a list
            iterates through to find append each file toe a column.
    print (cvs file)
        
            
    
        

## Phase 3: Implementation *(15%)*

*   **DO NOT COPY AND PASTE YOUR PYTHON CODE HERE!!!**
*   Write *code* in the `src/` directory
    *   Copy the outlines from Phase 2 into your `.py` files, and *translate* from English into Python
*   As you translate, you will *encounter problems* that were not foreseen earlier
    *   E.g. things that you learned, things that didn't go according to plan, etc.
    *   Here you can write a brief description of *what* changed and *why*
*   If everything went swimmingly, say so here

--------------------------------------------------------
I learned that this was the most time consuming project I have ever had.
The second most ime consuming was last project. I can get it all done if I start early enough.
Today I needed the grading gift, but I'll save it for later.

## Phase 4: Testing & Debugging *(30%)*

* For the bad inputs you thought of back in **Phase 2**, write a *test case* that you can run to prove that your functions work as expected
    *   It is not necessarily bad if a function crashes if you can explain *why* and *how* it happens
* Write the test cases you have *personally run*
    *   The *exact command* you used
    *   Copy & paste the program's *output*
    *   Be precise so that your grader can replicate your experience
* For any bugs discovered, describe their *cause* and *remedy*
* ---------------------------------------------------------------------------
I ran all of the tests provided in the scripts section on the functions I was able to complete and compaired the results to the example files.
* we got a bug in the head and tail functions while running -n in bash.
* To remidy this i used a .isdigit operator to figure out if -n "blah" was an int.


## Phase 5: Deployment *(5%)*

*   *Important:* complete **Phase 6** first!
    *   (I know it's backwards, just go with it)
*   **YOU DON'T NEED TO WRITE ANYTHING IN THIS PHASE**
    *   Just follow this checklist
*   **Push** your final commit to GitLab
*   **Verify** that your final commit was received by *browsing* to its project page on GitLab
    *   Ensure the project's *URL is correct*
    *   Review that all required files are present *in the correct location*
    *   Check that unwanted files *have not* been committed
    *   Add *final touches* to your documentation, including the Sprint Signature and this Plan
*   **Validate** that your submission is complete and correct by *cloning* it to a new location on your computer and re-running it
	*	Run your program from the *command line* so you can see how it will behave when your grader runs it
        *   **Testing in PyCharm is not good enough!**
    *   Re-run your *test cases* to avoid nasty surprises



## Phase 6: Maintenance

*   Write *brief and honest* answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are *sloppily written* and *hard to understand*?
        *   Are there parts of your program which you *aren't quite sure* how/why they work?
        *   If a bug is reported in a few months, *how long would it take you to find the cause*?
    *   Will your documentation make sense to...
        *   ...anybody *besides yourself*?
        *   ...*yourself* in six month's time?
    *   How easy will it be to *add a new feature* to this program in a year?
    *   Will your program *continue to work* after upgrading...
        *   ...your computer's *hardware*?
        *   ...the *operating system*?
        *   ...to the *next version* of Python?
*   Fill out the *Assignment Reflection* survey on Canvas
--------------------------------------------
* My cut and past functions were sloppy i never actually tested them outside of python.
* The parts I don't know are the tt.py file.
* I wouldn't want to fix this program. 
* Yes
* in 6 months yes
* not easy
* not sure
* nope
* no