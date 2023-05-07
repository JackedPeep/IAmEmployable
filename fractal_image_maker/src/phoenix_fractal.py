#!/usr/bin/env python3  	    	       
# Phoenix Fractal Visualizer - a variation of the Julia Fractal  	    	       

#                         _  	    	       
#                        (o)<  DuckieCorp Software License  	    	       
#                   .____//  	    	       
#                    \ <' )   Copyright (c) 2022 Erik Falor  	    	       
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	    	       
#  	    	       
# Permission is granted, to any person who is EITHER an employee OR  	    	       
# customer of DuckieCorp, to deal in the Software without restriction,  	    	       
# including without limitation the rights to use, copy, modify, merge,  	    	       
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	    	       
# permit persons to whom the Software is furnished to do so, subject to the  	    	       
# following conditions:  	    	       
#  	    	       
# The above copyright notice and this permission notice shall be included in  	    	       
# all copies or substantial portions of the Software.  	    	       
#  	    	       
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	    	       
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	    	       
# FITNESS FOR A PARTICULAR PURPOSE, EDUCATIONAL VALUE AND NONINFRINGEMENT. IN  	    	       
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  	    	       
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR  	    	       
# OTHERWISE, ARISING FROM INDIGNATION, INDIGESTION, INDIFFERENCE, INDECENCY,  	    	       
# INDENTATION, INDETERMINATION, INTOXICATION, INDOCTRINATION, INTOLERANCE,  	    	       
# INDULGENCE, INDELICATENESS, INDISCRETION, INEFFECTIVENESS OR IN CONNECTION  	    	       
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  	    	       


import sys  	    	       
import time
# gui imports
from tkinter import Tk, Canvas, PhotoImage, mainloop  	    	       



def getColorFromPalette(z):  	    	       
    """  	    	       
    Return the index of the color of the current pixel  	    	       
    within the Phoenix fractal in the palette array  	    	       
    """  	    	       

    # I feel bad about all of the global variables I'm using.  	    	       
    # There must be a better way...  	    	       
    global grad  	    	       
    global win  	    	       

    # c is the Julia Constant; varying this value gives rise to a variety of variated images  	    	       
    c = complex(0.5667, 0.0)  	    	       

    # phoenix is the Phonix Constant; same deal as above - adjust this to get different results  	    	       
    pheonix = complex(-0.5, 0.0)  	    	       

    # The first thing we do to the complex number Z is reflect its components,  	    	       
    # so the imaginary part becomes the real part, and vice versa  	    	       
    zFlipped = complex(z.imag, z.real)  	    	       
    ## if we don't do this, the image comes out SIDEWAYS!!!  	    	       

    # zPrevious is the PREVIOUS Z value, except the 1st time through the  	    	       
    # function, when it starts out as Complex Zero (which is actually the  	    	       
    # same thing as REAL Zero 0)  MATH IS BEAUTIFUL!  	    	       
    zPrev = 0+0j  	    	       
    z = zFlipped  	    	       

    # Use 101 here because that's the number of colors in the palette  	    	       
    # Except range() wants its number to be one more than the number  	    	       
    # that YOU want.  	    	       
    for i in range(102):# <--not cool, PYTHON WHY CAN'T YOU BE BEAUTIFUL LIKE MATH?  	    	       

        zSave = z  # save the current Z value before we overwrite it  	    	       
        # compute the new Z value from the current and previous Zs  	    	       
        z = z * z + c + (pheonix * zPrev)  	    	       
        zPrev = zSave  # Set the prevZ value for the next iteration  	    	       

        if abs(z) > 2:  	    	       
            return grad[i]  # The sequence is unbounded  	    	       
            z = z * z + c  # + zPrev * pheonix  	    	       
    # TODO: One of these returns occasionally makes the program crash sometimes  	    	       
    return grad[101]         # Else this is a bounded sequence


def getFractalKey(dictionary, name):
    """Make sure that the key name is in the dictionary and returns it.
    """  	    	       
    
    if name in dictionary:
        return name  	    	       


Save_As_Picture = True  	    	       
tkPhotoImage = None  	    	       
#def makePictureOfFractal(image, w, p, backgroundColor, dimentionOFImage):  +
def makePictureOfFractal(fractalImages, w, p, BGCOLOR, IMAGEDIMENTION):
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	    	       
    Assumes the image is 640x640 pixels."""  	    	       

    # Correlate the boundaries of the PhotoImage object to the complex  	    	       
    # coordinates of the imaginary plane  	    	       

    # Compute the minimum coordinate of the picture  	    	       
    min = ((fractalImages['centerX'] - (fractalImages['axisLength'] / 2.0)),
           (fractalImages['centerY'] - (fractalImages['axisLength'] / 2.0)))

    # Compute the maximum coordinate of the picture  	    	       
    # The program has only one axisLength because the images are square  	    	       
    # Squares are basically rectangles except the sides are equal instead of different  	    	       
    max = ((fractalImages['centerX'] + (fractalImages['axisLength'] / 2.0)),
           (fractalImages['centerY'] + (fractalImages['axisLength'] / 2.0)))
    #mbrot version.
    # minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    # maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    # miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
    # maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)
    # Display the image on the screen  	    	       
    mouseBasedInterface = Canvas(win, width=IMAGEDIMENTION, height=IMAGEDIMENTION, bg=BGCOLOR)

    # pack the canvas object into its parent widget  	    	       
    mouseBasedInterface.pack()
    # TODO: Sometimes I wonder whether some of my functions are trying to do  	    	       
    #       too many different things... this is the correct part of the  	    	       
    #       program to create a GUI window, right?  	    	       

    # Create the TK PhotoImage object that backs the Canvas Objcet  	    	       
    # This is what lets us draw individual pixels instead of drawing things like rectangles, squares, and quadrilaterals  	    	       
    mouseBasedInterface.create_image((IMAGEDIMENTION/2, IMAGEDIMENTION/2), image=p, state="normal")

    # pack the canvas object into its parent widget  	    	       
    mouseBasedInterface.pack()  # Does this even matter?
    # At this scale, how much length and height of the  	    	       
    # imaginary plane does one pixel cover?  	    	       
    size = abs(max[0] - min[0]) / IMAGEDIMENTION

    # pack the canvas object into its parent widget  	    	       
    mouseBasedInterface.pack()

    # Keep track of the fraction of pixels that have been written up to this point in the program  	    	       
    fraction_of_pixels_writtenSoFar = int(IMAGEDIMENTION // 640)

    # for r (where r means "row") in the range of the size of the square image,  	    	       
    # but count backwards (that's what the -1 as the 3rd parameter to the range() function means - it's the "step"  	    	       
    # You can actually put any number there that you want, because it defaults to "1" you usually don't have to  	    	       
    # but I have to here because we're actually going BACKWARDS, which took me  	    	       
    # a long time to figure out, so don't change it, or else the picture won't  	    	       
    # come out right  	    	       

    for row in range(len(IMAGEDIMENTION)):
        # for c (c == column) in the range of pixels in a square of size s  	    	       
        cs = []  	    	       
        for col in range(IMAGEDIMENTION):
            # calculate the X value in the complex plane (I guess that's  	    	       
            # actually the REAL number part, but we call it X because  	    	       
            # GRAPHICS... whatev)  	    	       
            x = min[0] + col * size
            y = 0  	    	       
            # get the color of the pixel at this point in the complex plain  	    	       
            cp = getColorFromPalette(complex(x, y))  	    	       
            # calculate the X value in the complex plane (but I know this is  	    	       
            # really the IMAGINARY axis that we're talking about here...)  	    	       
            y = min[1] + row * size
            # TODO: do I really need to call getColorFromPalette() twice?  	    	       
            #       It seems like this should be slow...  	    	       
            #       But, if it aint broken, don't repair it, right?  	    	       
            cp = getColorFromPalette(complex(x, y))  	    	       
            cs.append(cp)  	    	       
        pixls = '{' + ' '.join(cs) + '}'  	    	       
        p.put(pixls, (0, IMAGEDIMENTION - row))
        w.update()  # display a row of pixels  	    	       
        fraction_of_pixels_writtenSoFar = (IMAGEDIMENTION - row) / IMAGEDIMENTION # update the number of pixels output so far
        # print a statusbar on the console  	    	       
        print(f"[{fraction_of_pixels_writtenSoFar:>4.0%}"  	    	       
              + f"{'=' * int(34 * fraction_of_pixels_writtenSoFar):<33}]",
              end="\r",
              file=sys.stderr)



# This is the color palette, which defines the palette that images are drawn  	    	       
# in as well as limiting the number of iterations the escape-time algorithm uses  	    	       
#  	    	       
# TODO: It would be nice to add more or different colors to this list, but it's
#  just so much work to calculate all of the in-between shades!
grad = [  	    	       
        '#FFE4B5', '#FFE5B2', '#FFE6AF', '#FFE8AC', '#FFE9A9', '#FFEBA7',  	    	       
        '#FFEDA4', '#FFEFA1', '#FFF19E', '#FFF49B', '#FFF698', '#FFF995',  	    	       
        '#FFFC92', '#FFFF90', '#FCFF8D', '#F9FF8A', '#F5FF87', '#F1FF84',  	    	       
        '#EEFF81', '#E9FF7E', '#E5FF7B', '#E1FF78', '#DDFF76', '#D8FF73',  	    	       
        '#D3FF70', '#CEFF6D', '#C9FF6A', '#C4FF67', '#BEFF64', '#B9FF61',  	    	       
        '#B3FF5F', '#ADFF5C', '#A7FF59', '#A0FF56', '#9AFF53', '#93FF50',  	    	       
        '#8DFF4D', '#86FF4A', '#7FFF47', '#78FF45', '#70FF42', '#69FF3F',  	    	       
        '#61FF3C', '#59FF39', '#51FF36', '#49FF33', '#40FF30', '#38FF2E',  	    	       
        '#2FFF2B', '#28FF29', '#25FF2C', '#22FF30', '#1FFF33', '#1CFF37',  	    	       
        '#19FF3B', '#16FF3F', '#14FF43', '#11FF48', '#0EFF4C', '#0BFF51',  	    	       
        '#08FF56', '#05FF5B', '#02FF60', '#00FE65', '#00FC6B', '#00F971',  	    	       
        '#00F677', '#00F37C', '#00F081', '#00ED86', '#00EA8B', '#00E790',  	    	       
        '#00E595', '#00E299', '#00DF9D', '#00DCA2', '#00D9A5', '#00D6A9',  	    	       
        '#00D3AD', '#00D0B0', '#00CDB4', '#00CBB7', '#00C8BA', '#00C5BD',  	    	       
        '#00C2BF', '#00BCBF', '#00B4BC', '#00ACB9', '#00A4B6', '#009DB4',  	    	       
        '#0095B1', '#008EAE', '#0087AB', '#0080A8', '#0079A5', '#0072A2',  	    	       
        '#006C9F', '#00669C', '#005F9A', '#005997', '#005494', '#004E91',  	    	       
        '#00488E', '#00438B', '#003E88', '#003985', '#003483', '#002F80',  	    	       
        '#002B7D', '#00267A', '#002277'  	    	       
        ]  	    	       



# This dictionary contains the different views of the Phoenix set you can make  	    	       
# with this program.  	    	       
#  	    	       
# For convenience I have placed these into a dictionary so you may easily  	    	       
# switch between them by entering the name of the image you want to generate  	    	       
# into the variable 'i'.  	    	       
#  	    	       
# TODO: Maybe it would be a good idea to incorporate the complex value `c` into  	    	       
# this configuration dictionary instead of hardcoding it into this program.  	    	       
# But I don't have time for this right now, too busy.  I'll just keep doing it  	    	       
# the way I know how.  	    	       
fractalImages = {
        # The full Phoneix set  	    	       
        'phoenix': {  	    	       
            'centerX':     0.0,  	    	       
            'centerY':     0.0,  	    	       
            'axisLength':  3.25,  	    	       
            },  	    	       

        # This one looks like a peacock's tail to me  	    	       
        'peacock': {  	    	       
            'centerX':     -0.363287878200906,  	    	       
            'centerY':     0.381197981824009,  	    	       
            'axisLength':  0.0840187115019564,  	    	       
        },  	    	       

        # Two or more monkeys having a scuffle  	    	       
        'monkey-knife-fight': {  	    	       
            'centerX':    -0.945542168674699,  	    	       
            'centerY':    0.232234726688103,  	    	       
            'axisLength': 0.136626506024096,  	    	       
            },  	    	       

        # This one makes me hungry to look at  	    	       
        'shrimp-cocktail': {  	    	       
            'centerX': 0.529156626506024,  	    	       
            'centerY': -0.3516077170418,  	    	       
            'axisLength': 0.221204819277108,  	    	       
            },  	    	       
        }  	    	       


# This is how you write colors for computers  	    	       
WHITE = '#ffffff'  # white  	    	       
RED = '#ff0000'  # red  	    	       
BLUE = '#00ff00'  # blue  	    	       
GREEN = '#0000ff'  # green  	    	       
BLACK = '#000000'  # black  	    	       
ORANGE = '#ffa50'  # orange  	    	       
TOMATO = '#ff6347'  # tomato (a shade of red)  	    	       
HOT_PINK = '#ff69b4'  # hot pink (a kind of pink)  	    	       
REBECCA_PURPLE = '#663399'  # Rebecca Purple  	    	       
LIME_GREEN = '#89ff00'  # lime green (brighter than regular green)  	    	       
GREY0 = '#000000'  # gray 0 - basically the same as black  	    	       
GRAY37 = '#5e5e5e'  # gray 37 - lighter than black and gray 36  	    	       
GREY74 = '#bdbdbd'  # gray 74 - almost white  	    	       
GRAY99 = '#fcfcfc'  # gray 99 - almost white  	    	       


def phoenix_main(i):  	    	       
    """The main entry-point for the Phoenix fractal generator"""  	    	       

    # Look, I  know globals are bad, but I don't know how else to use those  	    	       
    # variables in here if I don't do it this way.  I didn't take any fancy CS  	    	       
    # classes, sue me  	    	       


    # Note the time of when we started so we can measure performance improvements  	    	       
    b4 = time.time()
    # Set up the GUI so that we can display the fractal image on the screen  	    	       
    win = Tk()  	    	       

    print("Rendering %s fractal" % i, file=sys.stderr)  	    	       
    # the size of the image we will create is 512x512 pixels  	    	       
    s = 512  	    	       
    # construct a new TK PhotoImage object that is 512 pixels square...  	    	       
    tkPhotoImage = PhotoImage(width=512, height=512)  	    	       
    # ... and use it to make a picture of a fractal  	    	       
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?  	    	       
    makePictureOfFractal(fractalImages[i], i, ".png", win, grad, tkPhotoImage, GREY0, 512)

    if Save_As_Picture:  	    	       
        # Write out the Fractal into a .gif image file  	    	       
        tkPhotoImage.write(i + ".png")  	    	       

        print(f"\nDone in {time() - b4:.3f} seconds!", file=sys.stderr)  	    	       


    # print a message telling the user how to quit or exit the program  	    	       
    print("Close the image window to exit the program", file=sys.stderr)  	    	       
    # Call tkinter.mainloop so the GUI remains open  	    	       
    mainloop()  	    	       


## This is some weird Python thing... but all of the tutorials do it, so here we go  	    	       
#if __name__ == '__main__':  	    	       
#    # Process command-line arguments, allowing the user to select their fractal  	    	       
#    if len(sys.argv) < 2:  	    	       
#        print("Please provide the name of a fractal as an argument", file=sys.stderr)  	    	       
#        for i in f:  	    	       
#            print(f"\t{i}", file=sys.stderr)  	    	       
#        sys.exit(1)  	    	       
#  	    	       
#    elif sys.argv[1] not in f:  	    	       
#        print(f"ERROR: {sys.argv[1]} is not a valid fractal", file=sys.stderr)  	    	       
#        print("Please choose one of the following:", file=sys.stderr)  	    	       
#        for i in f:  	    	       
#            print(f"\t{i}", file=sys.stderr)  	    	       
#        sys.exit(1)  	    	       
#  	    	       
#    else:  	    	       
#        fratcal_config = (f, sys.argv[1])  	    	       
#        phoenix_main(fratcal_config)  	    	       
