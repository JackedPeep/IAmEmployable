#!/usr/bin/env python3  	    	       


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
from FractalParser import fractalParser
from FractalFactory import fractalFactory
from PaletteFactory import paletteFactory
from ImagePainter import ImagePainter


if len(sys.argv) == 1:
    print ("{}".format( 'No arguments given.\nUsing default fractal.' ))
    fractalInfo = {'type':'euphemia',
                     'pixels':'640',
                     'iterations':'64',
                     'centerx':'-.24',
                     'centery':'0',
                     'axislength':'.12'}
    palette = "default"
    image = "default"
    Fractal = fractalFactory(fractalInfo)
    Palette = paletteFactory(palette)

elif len(sys.argv) < 3:
    # if user specified fractal, but not palette
    print("{}".format('Please provide the name of a palette as a second argument of \"main.py\"'))
    sys.exit(1)

elif len(sys.argv) == 3:
    fractalInfo = fractalParser(sys.argv[1])
    userPalette = sys.argv[2]
    image = sys.argv[1]
    Fractal = fractalFactory(fractalInfo)
    Palette = paletteFactory(userPalette)


else:
    print("ERROR: To many arguments please provide a valid fractal and a valid palette:")


    sys.exit(1)
paintImage = ImagePainter(Fractal, Palette, fractalInfo, image)
paintImage.printSave()