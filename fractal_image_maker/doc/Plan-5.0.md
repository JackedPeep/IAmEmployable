# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

The purpose of this program is to out put an image using `.png` files 
(*figuring out how these files are read in would be a good idea*).

**A good program should smell nice!**

**MY Job:**
- create the proper git tags by:
  - completing the analyzed phase by understanding the documentation and sorce code.
  - completing the designed step by identifying the code smells, a rough draft of the user's manual (*dolt didn't write it when they gave it to me!*), and unit tests are written.
  - completing the implemented phase by making sure the source code it readable, noting changes to the design.
  - completing the deployed phase by making sure everthing is "up to snuff" delete all scaffolding, make sure your code runs the same , but make sure your code looks emaculate.
<br><br/>
- refactor the code by:
  - looking for bad code names!
  - rename the code to be more understandable (*be sure to make sure the code works the same*).
  - git commit a lot!
  - document at least one of each code smell discussed in class **there should be 11 in total**!

## Phase 1: System Analysis *(10%)*




**Template of analysis:**


**Method**(*input data and location*) -->
`output`
-----
**userArgument**(*user input fractal choice*) -->
`passes to userFractal`

**fractalCast**(*takes userArgument and reads the dictionary and gets measurements*) -->
`prints out the image based on the measurments of the user's input`

**UserFractal**(*obtains key from main, and uses "fractalCast()"*) -->
`prints and saves .png image`


## Phase 2: Design *(30%)*


    ```
    def main():
        if users input is valid:   # makes sure user input is valid and returns errors or casts the image.
            return lists and functions provided by pheonix and mbrot
            print fractal to screen
        else:
            return command line options

    def pixelColor(x, y):    # returns the location of the color to be used in fractalCasting
        for each color in the color palettte:
            if the absolute value of the imaginery number is greater than 2:
                return color quordinates.
    
    
    def fracalCast(userClick):   # creates the image or "paints" the fractal
        for each row in the number of rows:
            for each column in the number of columns:
                calculate the pixel color
                print pixel color in location[row][column]
                save as a .png into program directory
            

    ```



## Phase 3: Implementation *(15%)*

**Major Changes**
- Created additional files:
  - I missed that the end result needed a minimum of 6 files so when I
  reread the requirements I completely changed the structure of my code
  based on the requirements.
- Created new functions:
  - ImagePainter has a paintImage function based on malbrot's paint function
  - ImagePaiter has a main function based on malbrot's main function
  - Malbrot had its colorOfThePixel function renamed
  - Phoenix had its getColorFromPalette function renamed

**Interesting Events**

**Deliver:**

*   (More or less) working code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

**Testing from command line**

- Give invalid argument 
  - No noteworthy problems
- Run without a specific image
  - No noteworthy problems
- Run a phoenix image 
  - Window not poping up
    - I tried to test ImagePainter before finishing main and the window would not pop up
    My code looked fine, so I tried running my code on a different computer and it worked
    fine. Restarting my computer fixed the problem, but I did not try this until I had spent
    a lot of time trying other things.
- Run a malbrot image 
  - Out of range error
    - When running spiral0 I would get an out of range error. I had not accounted for 0 indexing

**Tests are already created**

The unit tests were functional, but with name changes and file changes many no longer worked. I 
edited the tests so they tested the same basic functionality, but now from my new files.
- Phoenix had an out of range error due to the same problem I had with malbrot earlier.
- Phoenix was getting #002277 instead of #004E91 on two of the tests. This was because the old
phoenix function only went to the 102nd position of the palette rather then all the way to the 
end. I changed the tests to use the end value.

**Image Comparision**
- Phoenix
  - I ran all the phoenix images and compared them to those in the Readme and noticed the blue was 
  darker in mine. I changed my Phoenix.py to use 101 as the max palette length and that fixed the issue
  but I am not sure if that is what I should do since we have additional values in the palette. I decided
  to use the whole palette even though the results are different.
- Mandlebrot
  - These appeared identical.

## Phase 5: Deployment *(5%)*

## Phase 6: Maintenance

1. Overall the code is much better. 'i don't know of any sloppy parts
2. I think I understand how the tkinter stuff works, but I am not sure
3. If the bug is with the tkinter stuff it could take a while otherwise I
could fix it in under an hour most likely.
4. Yes
5. Yes
6. Hopefully easy since I need to add stuff next assignment
7. Yes
8. Maybe
9. Quite possibly not
