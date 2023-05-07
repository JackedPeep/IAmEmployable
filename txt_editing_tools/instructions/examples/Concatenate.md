# Forward and reverse concatenation tools (`cat` and `tac`)


## cat
Concatenate two files into one output

    $ python src/tt.py cat data/let3 data/num2
    a
    b
    c
    1
    2


Ordinarily, `cat` is used by Unix hackers to print a file to the screen

    $ python src/tt.py cat data/complexity
         "There are two ways of constructing a software design:

                    one way is to make it so simple
               that there are obviously no deficiencies,

               and the other is to make it so complicated
                that there are no obvious deficiencies."

        -- Tony Hoare



`cat` can accept any number of filename arguments >= 1:

    $ python src/tt.py cat data/ages8 data/colors8 data/complexity data/debugging data/dup5 data/let3 data/names10 data/names8 data/num10 data/num2 data/random20 data/verbs8 data/wordcount data/words200
    Age
    22
    36
    24
    ...
    reconfigurations
    activates
    autobiographies
    adverbs


## tac
`tac` works just like `cat`, only backwards.  That is, the lines of each file are printed in reverse order.  The files themselves *are* still processed in the order given on the command line:

    $ python src/tt.py tac data/let3 data/num2
    c
    b
    a
    2
    1


    $ python src/tt.py tac data/complexity
        -- Tony Hoare

                that there are no obvious deficiencies."
               and the other is to make it so complicated

               that there are obviously no deficiencies,
                    one way is to make it so simple

         "There are two ways of constructing a software design:


Like `cat`, `tac` also accepts any number of filename arguments >= 1:

    $ python src/tt.py tac data/ages8 data/colors8 data/complexity data/debugging data/dup5 data/let3 data/names10 data/names8 data/num10 data/num2 data/random20 data/verbs8 data/wordcount data/words200
    17
    29
    23
    26
    ...
    cranky
    implicitly
    insomniac
    social


## Handling errors

The program aborts as soon as a non-existent, invalid or inaccessible file is encountered.  You do not need to pre-screen the arguments before you begin processing; just let `open()` raise an exception.

    $ python src/tt.py cat data/let3 DOES_NOT_EXIST data/debugging
    a
    b
    c
    Traceback (most recent call last):
      File "/home/fadein/cs1440-falor-erik-assn2/src/tt.py", line 19, in <module>
        cat(sys.argv[2:])
      File "/home/fadein/cs1440-falor-erik-assn2/src/Concatenate.py", line 14, in cat
        f = open(filePath, 'r')
    FileNotFoundError: [Errno 2] No such file or directory: 'DOES_NOT_EXIST'


Your program must use `usage()` to raise an error when too few arguments are given; at a minimum the name of one input file is required.

    $ python src/tt.py tac
    Error: Too few arguments

    tt.py cat|tac FILENAME...
        Concatenate and print files in order or in reverse
