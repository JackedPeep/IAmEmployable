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
from Phoenix import phoenixPalettePosition
import ImagePainter
from Palette import phoenixPalette


# autocmd BufWritePost <buffer> !python3 runTests.py  	    	       

class TestPhoenix(unittest.TestCase):  	    	       
    def test_colorOfThePixel(self):  	    
        palLen = len(phoenixPalette)
        self.assertEqual(phoenixPalette[phoenixPalettePosition(complex(0, 0), palLen)], '#FFEBA7')  	    	       
        self.assertEqual(phoenixPalette[phoenixPalettePosition(complex(-0.751, 1.1075), palLen)], '#FFE4B5')
        self.assertEqual(phoenixPalette[phoenixPalettePosition(complex(-0.2, 1.1075), palLen)], '#FFE5B2')
        self.assertEqual(phoenixPalette[phoenixPalettePosition(complex(-0.750, 0.1075), palLen)], '#9AFF53')
        self.assertEqual(phoenixPalette[phoenixPalettePosition(complex(-0.748, -0.1075), palLen)], '#002277')
        self.assertEqual(phoenixPalette[phoenixPalettePosition(complex(-0.75625, 0.078125), palLen)], '#002277')
        self.assertEqual(phoenixPalette[phoenixPalettePosition(complex(-0.75625, -0.234375), palLen)], '#A7FF59')
        self.assertEqual(phoenixPalette[phoenixPalettePosition(complex(0.33749, -0.625), palLen)], '#FFE6AF')
        self.assertEqual(phoenixPalette[phoenixPalettePosition(complex(-0.678125, -0.46875), palLen)], '#002277')
        self.assertEqual(phoenixPalette[phoenixPalettePosition(complex(-0.406, -0.837), palLen)], '#FFE5B2')
        self.assertEqual(phoenixPalette[phoenixPalettePosition(complex(-0.186, -0.685), palLen)], '#FFE6AF')


    def test_paletteLength(self):
        self.assertEqual(111, len(phoenixPalette))


if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
