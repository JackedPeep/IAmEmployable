# Word Count tool (`wc`)

The `wc` tool counts and prints the number of lines, words, and characters (bytes) present in a text file.

*   One byte == one character
*   Words are separated from each other by white space.
    *   Punctuation symbols are treated like other non-white space characters for purposes of counting words.
    *   Thus, these are all "words" to the `wc` tool:
        *   `he's`
        *   `white-space`
        *   `a,few,words`
        *   `done.`
        *   `"what?!?`
        *   `Okay...if+you_say,so`
*   Lines are delimited by the end-of-line (EOL) sequence, which varies from OS to OS
    *   On Windows EOL is a carriage return followed by a newline `\r\n`
    *   On Linux and Mac EOL is a single newline character `\n`
*   Note that, due to differences in the representation of the EOL sequence between operating systems, the byte count you see on Windows may vary from the examples shown here.
    *   These examples were produced on Linux.
    *   The line and word counts should remain the same across all systems.


This example reports that the file `data/num2` contains two lines, two words, and four characters

    $ python src/tt.py wc data/num2
    2   2   4   data/num2


This example reports that the file `data/words200` contains 200 lines, 200 words, and 1790 characters

    $ python src/tt.py wc data/words200
    200 200 1790   data/words200


The file `data/complexity` contains 9 lines, 41 words and 289 characters
    $ python src/tt.py wc data/complexity
    9   41  289    data/complexity


The file `data/wordcount` contains 5 lines, 18 words, and 90 bytes
    $ python src/tt.py wc data/wordcount
    5   18   90    data/wordcount


Multiple files may be given at once.  In this case the grand total is reported at the end:

    $ python src/tt.py wc data/let3 data/random20 data/words200 data/dup5 data/complexity
         3       3       6  data/let3
        20      20      51  data/random20
       200     200    1790  data/words200
         8       8      16  data/dup5
         9      41     289  data/complexity
       240     272    2152  total


You can even give the same file many times; `wc` isn't clever enough to notice or care:

    $ python src/tt.py wc data/let3 data/let3 data/let3 data/let3 data/let3
         3       3       6  data/let3
         3       3       6  data/let3
         3       3       6  data/let3
         3       3       6  data/let3
         3       3       6  data/let3
        15      15      30  total


## Output format

*   These examples show the numeric columns being right-justified and the filenames left-justified.
    *   **This is not a hard requirement**.
    *   So long as the columns are presented in the correct order **AND** are distinct from each other, you can align them however you wish.
*   The columns of output, from left to right, are **lines**, **words**, **characters** and **file names**.


## Help!  My character count never matches these examples!

*   This is most likely due to differences in the representation of the end-of-line (EOL) sequence between operating systems
    *   On Mac and Linux, a newline is exactly **one** byte.
    *   For historical reasons that you don't care about, Windows uses **two** bytes to encode EOL.
    *   These examples were produced on Linux.
    *   The line and word counts should remain the same across all systems.
*   If the character count produced by your program is too great by an amount equal to the number of lines in the file, your program isn't broken...
    *   ...but your OS is :-P



## Handling errors

The program aborts as soon as a non-existent, invalid or inaccessible file is encountered.  You do not need to pre-screen the arguments before you begin processing; just let `open()` raise an exception.

    $ python src/tt.py wc data/let3 data/random20 DOES_NOT_EXIST data/dup5
     3   3   6  data/let3
    20  20  51  data/random20
    Traceback (most recent call last):
      File "src/tt.py", line 74, in <module>
        ops[sys.argv[1]](sys.argv[2:])
      File "/home/fadein/cs1440-falor-erik-assn2/src/WordCount.py", line 5, in wc
        f = open(filePath)
    FileNotFoundError: [Errno 2] No such file or directory: 'DOES_NOT_EXIST'


Your program must use `usage()` to raise an error when too few arguments are given; at a minimum the name of one input file is required.

    $ python src/tt.py wc
    Error: Too few arguments

    tt.py wc FILENAME...
        Print newline, word, and byte counts for each file
