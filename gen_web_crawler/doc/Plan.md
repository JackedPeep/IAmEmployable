# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**First Read Documentation; urllib.parse;  urljoin.py; Requests; BeautifulSoup** 


After that I will create a draft of a users manual on what the program is supposed to do And how to run it. 
This assignment is to make a interactive **recursive** web crawler that gracefully crashes and lets the user know what inputs they need to implement.
If wrong inputs are given the default depth is set to 3 and run as normal.

The problems I can see happening are not being able to handel broken links, so I will just have to make a test for those.

## Phase 1: System Analysis *(10%)*

**Key:**
`main`
(*Takes User arguments 'URL' and 'Depth'*; Input comes from user. Can be zero arguments or wrong arguments.) -> **New visited URLs**


`crawl`
(*url, depth*; main) -> **return new url visited, no repeats, skips and reports broken urls**


`keyboardInterupt`
(*any keys*; from user) -> **Stops program returning the activity report**



## Phase 2: Design *(30%)*

```
    def main():
        if no comand line arguments are given
            display usage message 
            exit program
        elif URL argument is given only
            if URL is absolute
                set depth to 3 and run
            else:
                display usage message
    
        elif both arguments are given
            if URL is absolute
                if depth is valid +int  
                    url = user input for URL
                    depth = user input for depth
                    print "Starting URL: url\nMaximum Depth: depth"
                    crawl(url,depth)
    
                else:
                     url = user input for URL
                    depth = 3
                    print "Starting URL: url\nMaximum Depth: depth"
                    crawl(url,depth)
            else:
                display usage message(URL is not absolute)
    
        else:
            display usage message(too many arguments)
                
```
```
    def crawl(url, depth, z):
        for line in website
           aline = split line into an array
            for data in aLine
                if data is an absolute URL
                    url = aLine[i]
                    depth -= 1
                    crawl(url, depth)
        
```

## Phase 3: Implementation *(15%)*

I learned that the @ symbol screws with your url.

## Phase 4: Testing & Debugging *(30%)*

    ```
    # Command: python3 src/crawler.py http://cs.usu.edu 5
    # Bug Found: The comand didn't get through, and went directly through to print time.
    # Bug Fixed: I was checking to see if it was an int wrong.
    ```
    ```
    # Command: python3 src/crawler.py http://cs.usu.edu 5
    # Bug Found: The program printed 3 every time for the maxDepth.
    # Bug Fixed: Took the assignmetn out of the try statement.
    ```
    ```
    # Command: python3 src/crawler.py http://cs.usu.edu
    # Bug Found: The program threw and exception saying the respons didn't have an atribute len
    # Bug Fixed: passed in html.text instead
    ```

## Phase 5: Deployment *(5%)*



## Phase 6: Maintenance

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   Fill out the Assignment Reflection on Canvas.

1) the package is hard to understand so read the sorce code
2) the package at first until I read the demos
3) I would not fix it
4) yes
5) yes
6) I don't know...
7) yes
8) maybe if suporting librarys are up to date
9) probs
