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

import unittest
from Mandelbrot import malbrotPalettePosition
from ImagePainter import pixelsWrittenSoFar
from Palette import malbrotPalette
# autocmd BufWritePost <buffer> !python3 runTests.py  	    	       

class TestMandelbrot(unittest.TestCase):  	    	       
    def test_malbrotPalettePosition(self):
        palLen = len(malbrotPalette)
        self.assertEqual(malbrotPalette[malbrotPalettePosition(complex(0, 0), palLen)], '#e8283f')
        self.assertEqual(malbrotPalette[malbrotPalettePosition(complex(-0.751, 1.1075), palLen)], '#baf12e')
        self.assertEqual(malbrotPalette[malbrotPalettePosition(complex(-0.2, 1.1075), palLen)], '#e0ceaf')
        self.assertEqual(malbrotPalette[malbrotPalettePosition(complex(-0.75, 0.1075), palLen)], '#f1da2e')
        self.assertEqual(malbrotPalette[malbrotPalettePosition(complex(-0.748, 0.1075), palLen)], '#deb69f')
        self.assertEqual(malbrotPalette[malbrotPalettePosition(complex(-0.7562500000000001, 0.078125), palLen)], '#e1bc7e')
        self.assertEqual(malbrotPalette[malbrotPalettePosition(complex(-0.7562500000000001, -0.234375), palLen)], '#e7ddd7')
        self.assertEqual(malbrotPalette[malbrotPalettePosition(complex(0.3374999999999999, -0.625), palLen)], '#e1d1bd')
        self.assertEqual(malbrotPalette[malbrotPalettePosition(complex(-0.6781250000000001, -0.46875), palLen)], '#eccd43')
        self.assertEqual(malbrotPalette[malbrotPalettePosition(complex(0.4937499999999999, -0.234375), palLen)], '#d9e758')
        self.assertEqual(malbrotPalette[malbrotPalettePosition(complex(0.3374999999999999, 0.546875), palLen)], '#e1cbbd')

    def test_pixelsWrittenSoFar(self):  	    	       
        self.assertEqual(pixelsWrittenSoFar(1), '[100% =================================]')
        self.assertEqual(pixelsWrittenSoFar(7), '[ 99% =================================]')
        self.assertEqual(pixelsWrittenSoFar(257), '[ 50% ================                 ]')
        self.assertEqual(pixelsWrittenSoFar(256), '[ 50% =================                ]')
        self.assertEqual(pixelsWrittenSoFar(100), '[ 80% ===========================      ]')
        self.assertEqual(pixelsWrittenSoFar(640), '[-25%                                  ]')
        self.assertEqual(pixelsWrittenSoFar(137), '[ 73% ========================         ]')
        self.assertEqual(pixelsWrittenSoFar(512), '[  0%                                  ]')

    def test_palleteLength(self):  	    	       
        self.assertEqual(111, len(malbrotPalette))


if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
