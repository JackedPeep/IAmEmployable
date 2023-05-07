#!/usr/bin/env python3  	    	       
# Mandelbrot Set Visualizer  	    	       

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

GRAPEFRUIT_PINK = '#e8283f'  	    	       
LEMON = '#fdff00'  	    	       
LIME_GREEN = '#89ff00'  	    	       
KUMQUAT = '#fac309'  	    	       
MAX_ITERATIONS = -1  	    	       
POMELLO = '#2fff00'  	    	       
TANGERINE = '#f7b604'  	    	       
# XXX: for some reason this line of code crashes the program...  	    	       
# window = Tk()  	    	       
WHITE = '#ffffff'  	    	       
#palette = [LIME_GREEN, '#a8f71b', '#c0ef34', '#d2ea4c', '#dfe563', '#e2db78',  	    	       
#        '#e0d28d', '#dfce9f', '#e0ceb1', '#e2d2c1', '#e5d9d0', '#eae1de',  	    	       
#        '#efebea', '#f7f5f5', WHITE, '#f7f5f5', '#efebea', '#eae0de',  	    	       
#        '#e5d6d0', '#e2cdc1', '#e0c5b1', '#dfbf9f', '#e0bc8d', '#e2bd78',  	    	       
#        '#e5c163', '#eac94c', '#efd634', '#f7e81b', LEMON, '#f7e81b',  	    	       
#        '#efd634', '#eac94c', '#e5c163', '#e2bd78', '#e0bc8d', '#dfbf9f',  	    	       
#        '#e0c5b1', '#e2cdc1', '#e5d6d0', '#eae0de', '#efebea', '#f7f5f5',  	    	       
#        WHITE, '#f6f5f5', '#efeaea', '#e9dfdd', '#e4d4d0', '#e1c9c1',  	    	       
#        '#dfbfb0', '#deb69f', '#deae8c', '#e0a978', '#e2a563', '#e7a54c',  	    	       
#        '#eca834', '#f3ae1b', TANGERINE, '#f3ae1b', '#eca834', '#e7a54c',  	    	       
#        '#e2a563', '#e0a978', '#deae8c', '#deb69f', '#dfbfb0', '#e1c9c1',  	    	       
#        '#e4d4d0', '#e9dfdd', '#efeaea', '#f6f5f5', WHITE, '#f6f6f5',  	    	       
#        '#efefea', '#e5e9de', '#d5e3d1', '#c3dfca', '#b4ddd1', '#a3d2db',  	    	       
#        '#91adda', '#857fdb', '#a66bdc', '#dc56df', '#e33f9d', WHITE,  	    	       
#        '#f6f5f4', '#eeeee8', '#e2e7db', '#cedead', '#beefcc', '#abdbd9',  	    	       
#        '#99beda', '#858cda', '#9c70dc', '#d159de', '#e341a4',  	    	       
#        GRAPEFRUIT_PINK, ]  	    	       

# This color palette contains 100 color steps.  	    	       
palette = [  	    	       
    '#89ff00', '#a4f817', '#baf12e',  	    	       
    '#ccec43', '#d9e758', '#e3e46b',  	    	       
    '#e1d97e', '#e0d18f', '#dfce9f',  	    	       
    '#e0ceaf', '#e1d1bd', '#e4d6cb',  	    	       
    '#e7ddd7', '#ece5e3', '#f1eeed',  	    	       
    '#f8f7f7', '#ffffff', '#f8f7f7',
    '#f1eeed', '#ece4e3', '#e7dbd7',  	    	       
    '#e4d3cb', '#e1cbbd', '#e0c4af',  	    	       
    '#dfbf9f', '#e0bd8f', '#e1bc7e',  	    	       
    '#e4bf6b', '#e7c458', '#eccd43',  	    	       
    '#f1da2e', '#f8eb17', '#fdff00',
    '#f8eb17', '#f1da2e', '#eccd43',  	    	       
    '#e7c458', '#e4bf6b', '#e1bc7e',  	    	       
    '#e0bd8f', '#dfbf9f', '#e0c4af',  	    	       
    '#e1cbbd', '#e4d3cb', '#e7dbd7',  	    	       
    '#ece4e3', '#f1eeed', '#f8f7f7',  	    	       
    '#ffffff', '#f7f6f6', '#f1eded',
    '#ebe4e2', '#e6dad7', '#e3d0ca',  	    	       
    '#e0c6bd', '#debeae', '#deb69f',  	    	       
    '#deaf8e', '#dfaa7d', '#e1a66b',  	    	       
    '#e4a557', '#e9a643', '#eea92e',  	    	       
    '#f4af17', '#f7b604', '#f4af17',
    '#eea92e', '#e9a643', '#e4a557',  	    	       
    '#e1a66b', '#dfaa7d', '#deaf8e',  	    	       
    '#deb69f', '#debeae', '#e0c6bd',  	    	       
    '#e3d0ca', '#e6dad7', '#ebe4e2',  	    	       
    '#f1eded', '#f7f6f6', '#ffffff',
    '#f8f7f7', '#f2f1ef', '#ebece5',  	    	       
    '#e2e7db', '#d3e3d0', '#c5e0ca',  	    	       
    '#b9ddce', '#abdbd9', '#9ec8da',  	    	       
    '#8fa7da', '#8480db', '#9c70dc',  	    	       
    '#c25fde', '#e04dcb', '#e43b8d',  	    	       
    '#ffffff', '#f7f6f6', '#f0efec',
    '#e8eae1', '#dae5d5', '#c8e1cb',  	    	       
    '#badecd', '#abdbd9', '#9cc4da',  	    	       
    '#8b9cda', '#8d79db', '#b066dd',  	    	       
    '#e052da', '#e33e97', '#e8283f', ]

MAX_ITERATIONS = 115  	    	       
z = 0  	    	       
seven = 7.0  	    	       
TWO = 2  	    	       

img = None  	    	       

mainWindowObject = None  	    	       

# def colorOfThePixel(c, palette):  	    	       
#     """Return the color of the current pixel within the Mandelbrot set"""  	    	       
#     global z  	    	       
#     z = complex(0, 0)  # z0  	    	       
#  	    	       
#     global MAX_ITERATIONS  	    	       
#     global iter  	    	       
#  	    	       
#     len = MAX_ITERATIONS  	    	       
#     for iter in range(len):  	    	       
#         z = z * z + c  # Get z1, z2, ...  	    	       
#         global TWO  	    	       
#         if abs(z) > TWO:  	    	       
#             z = float(TWO)  	    	       
#             if iter >= len(palette):  	    	       
#                 iter = len(palette) - 1  	    	       
#             return palette[iter]  	    	       
#         elif abs(z) < TWO:  	    	       
#             continue  	    	       
#         elif abs(z) > seven:  	    	       
#             print("You should never see this message in production", file=sys.stderr)  	    	       
#             continue  	    	       
#             break  	    	       
#         elif abs(z) < 0:  	    	       
#             print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)  	    	       
#             sys.exit(1)  	    	       
#         else:  	    	       
#             pass  	    	       
#  	    	       
#     return palette[iter]  # The sequence is unbounded  	    	       

def colorOfThePixel(c):
    """Return the color of the current pixel within the Mandelbrot set"""  	    	       
    global z  	    	       
    z = complex(0, 0)  # z0  	    	       

    global MAX_ITERATIONS  	    	       


    len = MAX_ITERATIONS  	    	       
    for count in range(len):
        z = z * z + c  # Get z1, z2, ...
        if abs(z) > 2:
            z = float(2)
            import builtins  	    	       
            len = builtins.len  	    	       
            if count >= len(palette):
                count = len(palette) - 1
            return count


    # Code borrowed from StackOverflow, comment copied from above  	    	       
    #  	    	       
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
    return palette[iter]  # The sequence is unbounded  	    	       



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


def pixelsWrittenSoFar(rows, cols):  	    	       
    portion = (512 - rows) / 512  	    	       
    pixels = (512 - rows) * 512  	    	       
    status_percent = '{:>4.0%}'.format(portion)  	    	       
    status_bar_width = 34  	    	       
    status_bar = '=' * int(status_bar_width * portion)  	    	       
    status_bar = '{:<33}'.format(status_bar)  	    	       
    # print(f"{pixels} pixels have been output so far")  	    	       
    # return pixels  	    	       
    # return '[' + status_percent + ' ' + status_bar + ']'  	    	       
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))  	    	       


# def pixelsWrittenSoFar(rows, cols):  	    	       
#     pixels = 0  	    	       
#     for r in range(rows + 1):  	    	       
#         pixels = pixels + cols  	    	       
#     print(pixels, "pixels have been output so far", file=sys.stderr)  	    	       
#     return pixels  	    	       



# These are the different views of the Mandelbrot set you can make with this  	    	       
# program.  	    	       
#  	    	       
# For convenience I have placed these into a dictionary so you may easily  	    	       
# switch between them by entering the name of the image you want to generate  	    	       
# into the variable 'image'.  	    	       
images = {  	    	       
        'mandelbrot': {  	    	       
            'centerX': -0.6,  	    	       
            'centerY': 0.0,  	    	       
            'axisLen': 2.5,  	    	       
            },  	    	       

        'mandelbrot-zoomed': {  	    	       
            'centerX': -1.0,  	    	       
            'centerY': 0.0,  	    	       
            'axisLen': 1.0,  	    	       
            },  	    	       

        'spiral0': {  	    	       
            'centerX': -0.761335372924805,  	    	       
            'centerY': 0.0835704803466797,  	    	       
            'axisLen': 0.004978179931102462,  	    	       
            },  	    	       

        'spiral1': {  	    	       
            'centerX': -0.747,  	    	       
            'centerY': 0.1075,  	    	       
            'axisLen': 0.002,  	    	       
            },  	    	       

        'seahorse': {  	    	       
            'centerX': -0.748,  	    	       
            'centerY': -0.102,  	    	       
            'axisLen': 0.008,  	    	       
            },

        'elephants': {  	    	       
            'centerX':  0.3015,  	    	       
            'centerY':  -0.0200,  	    	       
            'axisLen':  0.03,  	    	       
            },  	    	       

        'leaf': {  	    	       
            'centerX': -1.543577002,  	    	       
            'centerY': -0.000058690069,  	    	       
            'axisLen':  0.000051248888,  	    	       
            },  	    	       

        'starfish': {  	    	       
            'centerX': -0.463595023481762,  	    	       
            'centerY': 0.598380871135558,  	    	       
            'axisLen': 0.00128413675654471,  	    	       
            },  	    	       
        }  	    	       


def mbrot_main(image):  	    	       
    global img  	    	       
    # Set up the GUI so that we can paint the fractal image on the screen  	    	       
    print("Rendering {} fractal".format(image), file=sys.stderr)  	    	       
    before = time.time()  	    	       
    global window  	    	       
    window = Tk()  	    	       
    img = PhotoImage(width=512, height=512)  	    	       
    paint(images, image, window)  	    	       

    # Save the image as a PNG  	    	       
    after = time.time()  	    	       
    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)  	    	       
    img.write(f"{image}.png")  	    	       
    print(f"Wrote picture {image}.png", file=sys.stderr)  	    	       

    # Call tkinter.mainloop so the GUI remains open  	    	       
    print("Close the image window to exit the program", file=sys.stderr)  	    	       
    mainloop()  	    	       
