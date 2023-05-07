# Cut and Paste tools (`cut` and `paste`)

Because `paste` is used to create input data for the `cut` tool, I'll explain its use first.


## paste
Paste joins two or more files together, inserting a single comma `,` in between

    $ python src/tt.py paste data/let3 data/num2
    a,1
    b,2
    c,


Paste works by opening each file listed on the command line and storing the resulting file object in a list.  Then a `for` loop iterates over the list of file objects, reading one line from each file and printing it with a comma instead of a newline.  After the last file is read a newline is printed.  The `for` loop over the files is repeated until all files are exhausted.

The output of the `paste` command is as long as the longest file; missing fields are just empty strings

    $ python src/tt.py paste data/num2 data/let3
    1,a
    2,b
    ,c


    $ python src/tt.py paste data/num2 data/let3 data/words5
    1,a,babbles
    2,b,sneakiness
    ,c,trimly
    ,,agree
    ,,frankly


    $ python src/tt.py paste data/num2 data/words5 data/let3
    1,babbles,a
    2,sneakiness,b
    ,trimly,c
    ,agree,
    ,frankly,


When only one file is given `paste` behaves like `cat`

    $ python src/tt.py paste data/num10
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10


### Creating the file `data/people.csv`

`paste` is used to create a single Comma Separated Values (CSV) file from multiple input files.  `paste` works by joining lines from multiple files by a single comma `,`.

    $ python src/tt.py paste data/names8 data/ages8 data/colors8 data/verbs8
    Name,Age,Favorite Color,Locomotion Style
    Adrianna,22,Royal Blue,crawl
    Julian,36,Midnight Blue,traipse
    Tiffany,24,Light Salmon,push
    Savannah,39,Antique White,march
    Abraham,26,DarkSea Green,trot
    Michael,23,Dodger Blue,lurch
    Marcus,29,Dark Goldenrod,slink
    Julianna,17,Snow,wriggle


The resulting data can be redirected to a new file with the shell's redirection operator `>`.  The output then goes into the file instead of the screen.  This example illustrates how to create a file named `data/people.csv` which is used to demonstrate the `cut` tool:

    $ python src/tt.py paste data/names8 data/ages8 data/colors8 data/verbs8 > data/people.csv
    $


Notice that after running this command the prompt immediately returns and nothing else is printed to the screen.  The output was redirected into the new file `data/people.csv` instead of being displayed on the screen.

#### Help!  I just can't figure out `paste`!

If you get stuck on the `paste` tool and want to proceed to `cut`, you can create the test file `data/people.csv` using the `paste` tool that comes with your shell:

    $ paste -d, data/names8 data/ages8 data/colors8 data/verbs8 > data/people.csv
    $



## cut
`cut`, in contrast to `paste`, extracts fields (or columns) of data from a single CSV file given as an argument. Lines are split into fields on each comma `,`.  By default the 1st field is printed while the rest are ignored:

    $ python src/tt.py cut data/people.csv
    Name
    Adrianna
    Julian
    Tiffany
    Savannah
    Abraham
    Michael
    Marcus
    Julianna


Use the `-f` flag to specify which field to extract by its number.  Unlike lists in Python, `cut`'s field numbers begin with `1` and not `0`.  You'll need to take this into account.

    $ python src/tt.py cut -f 2 data/people.csv
    Age
    22
    36
    24
    39
    26
    23
    29
    17


A list of fields (possibly non-consecutive) may be specified.  Separate each field in the list with commas.

    $ python src/tt.py cut -f 2,4 data/people.csv
    Age,Locomotion Style
    22,crawl
    36,traipse
    24,push
    39,march
    26,trot
    23,lurch
    29,slink
    17,wriggle


When the user specifies an out-of-order list, `cut` will nevertheless print the fields in ascending order, as though the field specification is sorted within the program.  Notice that this command's output is identical to the command above:

    $ python src/tt.py cut -f 4,2 data/people.csv
    Age,Locomotion Style
    22,crawl
    36,traipse
    24,push
    39,march
    26,trot
    23,lurch
    29,slink
    17,wriggle


`cut` can process multiple files; each file is handled in the order given on the command line.  First, create a new CSV file called `data/kids.csv`:

    $ python src/tt.py paste data/num10 data/names10 data/words5 > data/kids.csv


Now run `cut` with the `-f` option and both CSV files:

    $ python src/tt.py cut -f 2 data/kids.csv data/people.csv
    Jerry
    Bailey
    Frank
    Kai
    Angela
    Mikayla
    Hazel
    Karen
    Alexa
    Isabel
    Age
    22
    36
    24
    39
    26
    23
    29
    17


Field numbers greater than the number of fields present in a file are treated as though they were empty.  Care must be taken to prevent Python from raising an `IndexError`.  Notice the excess of blank lines produced by this command:

    $ python src/tt.py cut -f 13 data/people.csv










    $



Notice the excess of blank lines produced by this command; half of the lines in `data/kids.csv` have a blank 3rd field.

    $ python src/tt.py cut -f 3 data/kids.csv
    babbles
    sneakiness
    trimly
    agree
    frankly





    $


*If you want to compare your version of `cut` with the "real" one, remember to give it the `-d,` argument so that it cuts on commas instead of Tabs.*


## Handling errors

The program aborts as soon as a non-existent, invalid or inaccessible file is encountered.  You do not need to pre-screen the arguments before you begin processing; just let `open()` raise an exception.

    $ python src/tt.py cut data/let3 DOES_NOT_EXIST data/complexity
    a
    b
    c
    Traceback (most recent call last):
      File "/home/fadein/cs1440-falor-erik-assn2/src/tt.py", line 39, in <module>
        cut(sys.argv[2:])
      File "/home/fadein/cs1440-falor-erik-assn2/src/CutPaste.py", line 39, in cut
        f = open(filePath)
    FileNotFoundError: [Errno 2] No such file or directory: 'DOES_NOT_EXIST'


Your program must use `usage()` to raise an error when too few arguments are given; at a minimum the name of one input file is required.

    $ python src/tt.py cut
    Error: Too few arguments

    tt.py cut [-f LIST] FILENAME...
        Remove comma-separated sections from each line of files
        -f  List of comma-separated integers indicating fields to output



`cut` must report an error when the `-f` switch is not given an argument

    $ python src/tt.py cut -f
    Error: A comma-separated field specification is required

    tt.py cut [-f LIST] FILENAME...
        Remove comma-separated sections from each line of files
        -f  List of comma-separated integers indicating fields to output



The argument to `-f` is a comma-separated list of positive integers.  Ignore
any numbers that are `<= 0`.  If all arguments to `-f` were invalid, continue
as if no arguments were given to `-f`:

    $ python src/tt.py cut -f 0,-1
    Error: A comma-separated field specification is required

    tt.py cut [-f LIST] FILENAME...
        Remove comma-separated sections from each line of files
        -f  List of comma-separated integers indicating fields to output
