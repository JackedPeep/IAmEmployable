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

from MenuOption import MenuOption  	    	       


class TestMenuOption(unittest.TestCase):  	    	       

    def setUp(self):  	    	       
        """Create no fewer than 5 MenuOption objects to test"""  	    	       
        self.a = MenuOption("A", "Test option A")  	    	       
        self.b = MenuOption("B", "Test option B")  	    	       
        self.c = MenuOption("C", "Test option C")  	    	       
        self.d = MenuOption("D", "Test option D")  	    	       
        self.e = MenuOption("E", "Test option E")  	    	       

    def test_chCommand(self):  	    	       
        """Ensure each option's letter char is set correctly"""  	    	       
        self.assertEqual(self.a.chCommand(), "A")  	    	       
        self.assertEqual(self.b.chCommand(), "B")  	    	       
        self.assertEqual(self.c.chCommand(), "C")  	    	       
        self.assertEqual(self.d.chCommand(), "D")  	    	       
        self.assertEqual(self.e.chCommand(), "E")  	    	       

    def test_szDescription(self):  	    	       
        """Ensure each option's description is set correctly"""  	    	       
        self.assertEqual(self.a.szDescription(), "Test option A")  	    	       
        self.assertEqual(self.b.szDescription(), "Test option B")  	    	       
        self.assertEqual(self.c.szDescription(), "Test option C")  	    	       
        self.assertEqual(self.d.szDescription(), "Test option D")  	    	       
        self.assertEqual(self.e.szDescription(), "Test option E")  	    	       

    def test_str(self):  	    	       
        """Ensure the __str__ dunder works correctly"""  	    	       
        self.assertEqual(str(self.a), "A) Test option A")  	    	       
        self.assertEqual(str(self.b), "B) Test option B")  	    	       
        self.assertEqual(str(self.c), "C) Test option C")  	    	       
        self.assertEqual(str(self.d), "D) Test option D")  	    	       
        self.assertEqual(str(self.e), "E) Test option E")  	    	       


if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
