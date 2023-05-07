# Code Smells Report - 5.0

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
    *   You do not need to list code smells in any particular order
*	Describe the smell and why it is a problem
*	Copy the offensive code between `` ``` ``
*	Describe how you can fix it
    *   We will follow up on these notes to make sure it was really fixed!


### These are some of the code smells you may find in the starter code:





0. **Magic** numbers
    * Numeric literals in critical places without any context or meaning
    * "Does `256` over here have anything to do with the `256` over there?"
 


1. **Global** variables
    *   Used to avoid passing a parameter into a function
    *   Used to return an extra value from a function
    *   There are better ways to meet both of these needs!


2. **Poorly-named** variables
    *   Short variable names are okay in some contexts:
        *   `i` or `j` as a counter in a brief `for` loop
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
        *   Otherwise, short names should be avoided
    *   Variables with really, really long names make code harder to read
    *   Variables that override or "shadow" other identifiers
        *   Builtin Python functions such as `input`, `len`, `list`, `max`, `min` and `sum` are especially susceptible to this
    *   Variable names should strike a good balance between brevity and descriptiveness





3. Comments that share **too much information**
    *   When almost every line of code is has an explanatory comment, it is likely true that variable and function names were poorly chosen
    *   Write code that speaks for itself





4. Comments that **lie**
    * An out-of-date remark that longer accurately describes the code
    * Bad advice left by a developer without a clue





5. Too many arguments
    *   Seen when more than a handful of parameters are passed to a function/method
    *   Parameters that are passed in but left unused
    *   Instead, accumulate parameters into a collection such as a dict




6. Function/Method that is too long
    *   Too many lines of code typically happens because the function/method has too many different responsibilities
    *   Generally, a method longer than a dozen lines should make you ask yourself "can I split this into smaller, more focused pieces?"




7. Complex decision trees
    *   Too long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Are all of the branches possible to reach?
    *   Has every branch been tested?




8. Spaghetti code
    *   Heaps of meandering code without a clear goal
    *   Functions/objects used in inconsistent ways
    *   Many variables are used to keep track of 
    *   Conditional statements with long, confusing Boolean expressions
    *   Boolean expressions expressing double negatives; ex. `if not undone: ...`
    *   Code that makes you say "It would be easier to rewrite this than to understand it"




9. Redundant code
    *   A repeated statement which doesn't have an effect the second time
    *   ```
        i = 7
        print(i)
        i = 7
        ```
    *   Ask yourself whether it makes any difference to be run more than once.




10. Dead code
    *   A piece of code that is not used (usually because it is obsolete)
    *   Blocks of commented-out code that serve no purpose and clutter up the file




If you see something that is not covered on this list, please add it to this report.




### Template

0.  Smell at `file` [lines xx-yy or general location]
    *   [Brief description of smell]
    *   [Code Snippet between triple-backquotes `` ``` ``]
    *   [How to resolve]


### Example

0.  Redundant Code at `src/main.py` [lines 32, 34]
    *   The import statement `import mbrot_fractal` occurs twice.  A second occurrence doesn't do it better than the first.
    *   ```python
        import mbrot_fractal  	    	       
        import phoenix_fractal as phoenix  	    	       
        import mbrot_fractal  	    	       
        ```
    *   This is easily resolved by deleting the second `import` statement.
    

## Code Smells



---
**This is the format I will be writing my smell documentation.** 

Smell found at; **File**:*smallest line*-*biggest line*

Code Smell:
```python
#CODE SMELL
```
Fix:
```python
#FIXED SMELL
```


---

0. **Magic** numbers
    * Numeric literals in critical places without any context or meaning
    * "Does `256` over here have anything to do with the `256` over there?"
 
Smell found at; `src/mbrot_fractal.py`:*226*-*245*

Code Smell:
```python
    canvas = Canvas(window, width=512, height=512, bg='#000000')  	    	       
    canvas.pack()  	    	       
    canvas.create_image((256, 256), image=img, state="normal")  	    	       

    # At this scale, how much length and height on the imaginary plane does one  	    	       
    # pixel take?  	    	       
    pixelsize = abs(maxx - minx) / 512  	    	       

    portion = 0  	    	       
    total_pixels = 512 * 512  # 262144  	    	       
    for row in range(512, 0, -1):  	    	       
        cc = []  	    	       
        for col in range(512):  	    	       
            x = minx + col * pixelsize  	    	       
            y = miny + row * pixelsize  	    	       
            color = colorOfThePixel(complex(x, y), palette)  	    	       
            cc.append(color)  	    	       
        img.put('{' + ' '.join(cc) + '}', to=(0, 512-row))  	    	       
        window.update()  # display a row of pixels  	    	       
        portion = 512 - row / 512
```
Fix:
```python
    PIXELWIDTH = 512 
    PIXELHEIGHT = 512
    canvas = Canvas(window, width=PIXELWIDTH, height=PIXELHEIGHT, bg='#000000')  	    	       
    canvas.pack()  	    	       
    canvas.create_image((PIXELWIDTH/2, PIXELHEIGHT/2), image=img, state="normal")  	    	       

    # At this scale, how much length and height on the imaginary plane does one  	    	       
    # pixel take?  	    	       
    pixelsize = abs(maxx - minx) / PIXELWIDTH 	    	       

    portion = 0  	    	       
    total_pixels = PIXELWIDTH * PIXELHEIGHT  # 262144  	    	       
    for row in range(PIXELHEIGHT, 0, -1):  	    	       
        cc = []  	    	       
        for col in range(PIXELWIDTH):  	    	       
            x = minx + col * pixelsize  	    	       
            y = miny + row * pixelsize  	    	       
            color = colorOfThePixel(complex(x, y), palette)  	    	       
            cc.append(color)  	    	       
        img.put('{' + ' '.join(cc) + '}', to=(0, 512-row))  	    	       
        window.update()  # display a row of pixels  	    	       
        portion = PIXELWIDTH - row / PIXELHEIGHT
```
---
1. **Global** variables
    *   Used to avoid passing a parameter into a function
    *   Used to return an extra value from a function
    *   There are better ways to meet both of these needs!

Smell found at; `src/phoenix_fractal.py`:*308*-*323*

Code Smell:
```python
global tkPhotoImage  	    	       
    global win  	    	       

    # Note the time of when we started so we can measure performance improvements  	    	       
    b4 = time()  	    	       
    # Set up the GUI so that we can display the fractal image on the screen  	    	       
    win = Tk()  	    	       

    print("Rendering %s fractal" % i, file=sys.stderr)  	    	       
    # the size of the image we will create is 512x512 pixels  	    	       
    s = 512  	    	       
    # construct a new TK PhotoImage object that is 512 pixels square...  	    	       
    tkPhotoImage = PhotoImage(width=512, height=512)  	    	       
    # ... and use it to make a picture of a fractal  	    	       
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?  	    	       
    makePictureOfFractal(f[i], i, ".png", win, grad, tkPhotoImage, GREY0, 512)  	    	       

```
Fix:
```python
  	    	       

    # Note the time of when we started so we can measure performance improvements  	    	       
    b4 = time()  	    	       
    # Set up the GUI so that we can display the fractal image on the screen  	    	       
    win = Tk()  	    	       

    print("Rendering %s fractal" % i, file=sys.stderr)  	    	       
    # the size of the image we will create is 512x512 pixels  	    	       
    s = 512  	    	       
    # construct a new TK PhotoImage object that is 512 pixels square...  	    	       
    tkPhotoImage = PhotoImage(width=512, height=512)  	    	       
    # ... and use it to make a picture of a fractal  	    	       
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?  	    	       
    makePictureOfFractal(f[i], i, ".png", win, grad, tkPhotoImage, GREY0, 512)  	    	       

```
---
2. **Poorly-named** variables

Smell found at; `scr/main.py`:*45*-*48*

Code Smell:
```python
from phoenix_fractal import f as phoenix_fractals  	    	       
PHOENX =[]  	    	       
for p in  phoenix_fractals . keys():  	    	       
    PHOENX=PHOENX+[p]  	    	       
```
Fix:
```python
from phoenix_fractal import phoenixDictionary  	    	       
validPKeys =[]  	    	       
for key in  phoenix_fractals . keys():  	    	       
    validPKeys=validPKeys+[key]  	    	       
```

---
3. Comments that share **too much information**
    *   When almost every line of code is has an explanatory comment, it is likely true that variable and function names were poorly chosen
    *   Write code that speaks for itself

Smell found at; `src/main`:*51*-*54*

Code Smell:
```python
MBROTS.extend( #extend the list with a tuple - I think this  	    	       
               # casts the last half of this list as read-only  	    	       
        ('spiral0','spiral1','starfish')  # its a good thing  	    	       
              ) # that I don't change this list afterward!  
```
Fix:
```python
#extend the list with a tuple
MBROTS.extend('spiral0','spiral1','starfish')  
```


4. Comments that **lie**
    * An out-of-date remark that longer accurately describes the code
    * Bad advice left by a developer without a clue

Smell found at; `src/phoenix_fractal.py`:*91*-*94*

Code Smell:
```python
# Use 101 here because that's the number of colors in the palette  	    	       
    # Except range() wants its number to be one more than the number  	    	       
    # that YOU want.  	    	       
    for i in range(102):# <--not cool, PYTHON WHY CAN'T YOU BE BEAUTIFUL LIKE MATH?  	    	       

```
Fix:
```python
    numColors = 101  	    	        	    	       
    for i in range(numColors + 1): # plus one because range is not inclusive. 	    	       

```

---

5. Too many arguments
    *   Seen when more than a handful of parameters are passed to a function/method
    *   Parameters that are passed in but left unused
    *   Instead, accumulate parameters into a collection such as a dict

Smell found at; `src/phoenix_fractal.py`:*128*

Code Smell:
```python
def makePictureOfFractal(f, i, e, w, g, p, W, s):
```
Fix:
```python
def makePictureOfFractal(f, w, p, W, s):
```

---
6. Function/Method that is too long
    *   Too many lines of code typically happens because the function/method has too many different responsibilities
    *   Generally, a method longer than a dozen lines should make you ask yourself "can I split this into smaller, more focused pieces?"

Smell found at; **File**:*smallest line*-*biggest line*

Code Smell:
```python
def paint(fractals, imagename, window):  	    	       
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	    	       
    This code creates an image which is 640x640 pixels in size."""  	    	       

    global palette  	    	       
    global img  	    	       

    fractal = fractals[imagename]  	    	       

    # Figure out how the boundaries of the PhotoImage relate to coordinates on  	    	       
    # the imaginary plane.  	    	       
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)  	    	       
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)  	    	       
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)  	    	       
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)  	    	       

    # Display the image on the screen  	    	       
    canvas = Canvas(window, width=512, height=512, bg='#000000')  	    	       
    canvas.pack()  	    	       
    canvas.create_image((256, 256), image=img, state="normal")  	    	       

    # At this scale, how much length and height on the imaginary plane does one  	    	       
    # pixel take?  	    	       
    pixelsize = abs(maxx - minx) / 512  	    	       

    portion = 0  	    	       
    total_pixels = 512 * 512  # 262144  	    	       
    for row in range(512, 0, -1):  	    	       
        cc = []  	    	       
        for col in range(512):  	    	       
            x = minx + col * pixelsize  	    	       
            y = miny + row * pixelsize  	    	       
            color = colorOfThePixel(complex(x, y), palette)  	    	       
            cc.append(color)  	    	       
        img.put('{' + ' '.join(cc) + '}', to=(0, 512-row))  	    	       
        window.update()  # display a row of pixels  	    	       
        portion = 512 - row / 512  	    	       
        # pixelsWrittenSoFar(portion, )  # This way isn't working let me try somthing eles...  	    	       
        #total_pixles = pixelsWrittenSoFar(row, col)  # will equal 262144 when the program is finished  	    	       
        print(pixelsWrittenSoFar(row, col), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column  	    	       

```
Fix:
```python
def createImage(fractals, imagename, window):  	    	       
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	    	       
    This code creates an image which is 640x640 pixels in size."""  	    	       
 	    	       
    fractal = fractals[imagename]  	    	       

    # Figure out how the boundaries of the PhotoImage relate to coordinates on  	    	       
    # the imaginary plane.  	    	       
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)  	    	       
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)  	    	       
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)  	    	       
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)  	    	       

    # Display the image on the screen  	    	       
    canvas = Canvas(window, width=512, height=512, bg='#000000')  	    	       
    canvas.pack()  	    	       
    canvas.create_image((256, 256), image=img, state="normal")  	    	       

    # At this scale, how much length and height on the imaginary plane does one  	    	       
    # pixel take? 
    
def colorPixels(pixelsize,maxx,miny):
    pixelsize = abs(maxx - minx) / 512  
    for row in range(512, 0, -1):  	    	       
        cc = []  	    	       
        for col in range(512):  	    	       
            x = minx + col * pixelsize  	    	       
            y = miny + row * pixelsize  	    	       
            color = colorOfThePixel(complex(x, y), palette)  	    	       
            cc.append(color)  	    	       
        img.put('{' + ' '.join(cc) + '}', to=(0, 512-row))  	    	       
        window.update()  # display a row of pixels  	    	       
        portion = 512 - row / 512  	    	       
        # pixelsWrittenSoFar(portion, )  # This way isn't working let me try somthing eles...  	    	       
        #total_pixles = pixelsWrittenSoFar(row, col)  # will equal 262144 when the program is finished  	    	       
        print(pixelsWrittenSoFar(row, col), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column  	    	       

```

---
7. Complex decision trees
    *   Too long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Are all of the branches possible to reach?
    *   Has every branch been tested?

Smell found at; `src/mbrot_fractal.py`:*154*-*190*

Code Smell:
```python
def colorOfThePixel(c, palette):  	    	       
    """Return the color of the current pixel within the Mandelbrot set"""  	    	       
    global z  	    	       
    z = complex(0, 0)  # z0  	    	       

    global MAX_ITERATIONS  	    	       
    global iter  	    	       

    len = MAX_ITERATIONS  	    	       
    for iter in range(len):  	    	       
        z = z * z + c  # Get z1, z2, ...  	    	       
        global TWO  	    	       
        if abs(z) > TWO:  	    	       
            z = float(TWO)  	    	       
            # XXX: the program used to crash with the error  	    	       
            #   TypeError: 'int' object is not callable  	    	       
            #  	    	       
            # maybe it had something to do with 'len' being an integer variable  	    	       
            # instead of a function variable.  	    	       
            # Somebody from StackOverflow suggested I do it this way  	    	       
            # IDK why, but it stopped crashing, and taht's all that matters!  	    	       
            import builtins  	    	       
            len = builtins.len  	    	       
            if iter >= len(palette):  	    	       
                iter = len(palette) - 1  	    	       
            return palette[iter]  	    	       
        elif abs(z) < TWO:  	    	       
            continue  	    	       
        elif abs(z) > seven:  	    	       
            print("You should never see this message in production", file=sys.stderr)  	    	       
            continue  	    	       
            break  	    	       
        elif abs(z) < 0:  	    	       
            print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)  	    	       
            sys.exit(1)  	    	       
        else:  	    	       
            pass  	    	       

```
Fix:
```python
def colorOfThePixel(c, palette):  	    	       
    """Return the color of the current pixel within the Mandelbrot set"""  	    	       
      	    	       
    z = complex(0, 0)  # z0  	    	         	    	       

    for i in range(len(palette)):  	    	       
        z = z * z + c  # Get z1, z2, ...  	    	       
          	    	       
        if abs(z) > 2:  	    	       
            z = float(2)  	    	         	    	         	    	       
            if i >= len(palette):  	    	       
                i = len(palette) - 1  	    	       
            return palette[i]  	    	       
        else:
            continue
              	    	       
              	    	       

```

---
8. Spaghetti code
    *   Heaps of meandering code without a clear goal
    *   Functions/objects used in inconsistent ways
    *   Many variables are used to keep track of 
    *   Conditional statements with long, confusing Boolean expressions
    *   Boolean expressions expressing double negatives; ex. `if not undone: ...`
    *   Code that makes you say "It would be easier to rewrite this than to understand it"

Smell found at; `src/main.py`:*88*-*99*

Code Smell:
```python
    quit = False                                           #######  	    	       
    next = ''                                              #######  	    	       
    iter = 0                                                #####  	    	       
    while not quit:                             #     ## ########### ###  	    	       
        next = PHOENX[iter]                      ### #################### ## #  	    	       
        print("\t%s" % next)                      ###########################  	    	       
                                              # ############################  	    	       
        if PHOENX[iter] == 'shrimp-cocktail': ################################  	    	       
            break                            ####################################  	    	       
                            #    ## #       ###################################  	    	       
        else:               ##########     ######################################  	    	       
            iter += 1     ##############   ####################################  	    	       

```
Fix:
```python
      	    	       
          
    for i in range(len(PHOENX)):                	                             
        print("\t%s" % PHOENX[i])                  	       
                                                 

```

---
9. Redundant code
    *   A repeated statement which doesn't have an effect the second time
    *   ```
        i = 7
        print(i)
        i = 7
        ```
    *   Ask yourself whether it makes any difference to be run more than once.

Smell found at; `src/main.py`:*104*-*105*

Code Smell: 
```python
    i = 0                 ##############   #####################################  	    	       
    i = 0                   ##########     ####################################  	    	       

```
Fix:
```python
    i = 0       	    	       
      	    	       

```
---

10. Dead code
    *   A piece of code that is not used (usually because it is obsolete)
    *   Blocks of commented-out code that serve no purpose and clutter up the file

Smell found at; `src/brot_fractal.py`:*smallest line*-*biggest line*

Code Smell:
```python
    portion = 0  	    	       
    total_pixels = 512 * 512  # 262144  
```
Fix:
```python
  
```

---
If you see something that is not covered on this list, please add it to this report.

---
**BAD ART**

Smell found at; `src/main.py`:*86*-*116*

Code Smell:
```python
    print("ERROR:", sys.argv[1], "is not a valid fractal")    #  	    	       
    print("Please choose one of the following:")             ###  	    	       
    quit = False                                           #######  	    	       
    next = ''                                              #######  	    	       
    iter = 0                                                #####  	    	       
    while not quit:                             #     ## ########### ###  	    	       
        next = PHOENX[iter]                      ### #################### ## #  	    	       
        print("\t%s" % next)                      ###########################  	    	       
                                              # ############################  	    	       
        if PHOENX[iter] == 'shrimp-cocktail': ################################  	    	       
            break                            ####################################  	    	       
                            #    ## #       ###################################  	    	       
        else:               ##########     ######################################  	    	       
            iter += 1     ##############   ####################################  	    	       
                     ########################################################  	    	       
              ######################################## CODE IS ART #########  	    	       
                     ########################################################  	    	       
    exit = None          ############################## (c) 2022 #############  	    	       
    i = 0                 ##############   #####################################  	    	       
    i = 0                   ##########     ####################################  	    	       
    fractal = ''            #    ## #       ####################################  	    	       
                                             #################################  	    	       
    while not exit:                          ################################  	    	       
        print("\t" + MBROTS[i])               #  ############################  	    	       
        if PHOENX[iter] =='shrimp-cocktail':    ######################### ####  	    	       
            if MBROTS[i]  == 'starfish':       ### #  ## ##############   #  	    	       
                                              #             #####  	    	       
                i = i + 1                                  #######  	    	       
                exit = PHOENX[iter] =='shrimp-cocktail'    #######  	    	       
                i -= 1 #need to back off, else index error   ###  	    	       
                exit = exit and MBROTS[i]  == 'starfish'      # 
```
Fix:
```python
    print("ERROR:", sys.argv[1], "is not a valid fractal")      	    	       
    print("Please choose one of the following:")   	       
    quit = False                                  	    	       
    next = ''                                  	    	       
    iter = 0                                 	    	       
    while not quit:                           	    	       
        next = PHOENX[iter]                   	    	       
        print("\t%s" % next)                 	    	       
                                         	    	       
        if PHOENX[iter] == 'shrimp-cocktail': 	    	       
            break                              	    	       
                              	       
        else:             
            iter += 1      	    	       
              	       
    exit = None               
    i = 0                	    	       
    i = 0                	    	       
    fractal = ''        	    	       
                                         	    	       
    while not exit:                       	    	       
        print("\t" + MBROTS[i])           	    	       
        if PHOENX[iter] =='shrimp-cocktail':  	    	       
            if MBROTS[i]  == 'starfish':     	    	       
                                              	       
                i = i + 1                               	    	       
                exit = PHOENX[iter] =='shrimp-cocktail' 	    	       
                i -= 1 #need to back off, else index error    	    	       
                exit = exit and MBROTS[i]  == 'starfish'    
```
