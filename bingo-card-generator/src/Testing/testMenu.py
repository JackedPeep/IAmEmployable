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

# Tests the Menu and MenuOption Classes  	    	       

import unittest  	    	       
from Menu import Menu  	    	       
from MenuOption import MenuOption  	    	       


class TestMenu(unittest.TestCase):  	    	       
    def test_add_options(self):  	    	       
        """Ensure that options can be added to a Menu"""  	    	       
        menu = Menu("Adding Options")  	    	       
        self.assertEqual(len(menu), 0)  	    	       
        menu += MenuOption("A", "Test option A")  	    	       
        self.assertEqual(len(menu), 1)  	    	       
        menu += MenuOption("B", "Test option B")  	    	       
        self.assertEqual(len(menu), 2)  	    	       
        menu += MenuOption("C", "Test option C")  	    	       
        self.assertEqual(len(menu), 3)  	    	       
        menu += MenuOption("D", "Test option D")  	    	       
        self.assertEqual(len(menu), 4)  	    	       
        menu += MenuOption("E", "Test option E")  	    	       
        self.assertEqual(len(menu), 5)  	    	       

    def test_get_options(self):  	    	       
        """Ensure that menu options can be retrieved from Menus"""  	    	       
        menu = Menu("Getting Options")  	    	       
        menu += MenuOption("A", "Test option A")  	    	       
        menu += MenuOption("B", "Test option B")  	    	       
        menu += MenuOption("C", "Test option C")  	    	       
        menu += MenuOption("D", "Test option D")  	    	       
        menu += MenuOption("E", "Test option E")  	    	       

        opt = menu[0]  	    	       
        self.assertEqual(opt.chCommand(), "A")  	    	       
        self.assertEqual(opt.szDescription(), "Test option A")  	    	       

        opt = menu[1]  	    	       
        self.assertEqual(opt.chCommand(), "B")  	    	       
        self.assertEqual(opt.szDescription(), "Test option B")  	    	       

        opt = menu[2]  	    	       
        self.assertEqual(opt.chCommand(), "C")  	    	       
        self.assertEqual(opt.szDescription(), "Test option C")  	    	       

        opt = menu[3]  	    	       
        self.assertEqual(opt.chCommand(), "D")  	    	       
        self.assertEqual(opt.szDescription(), "Test option D")  	    	       

        opt = menu[4]  	    	       
        self.assertEqual(opt.chCommand(), "E")  	    	       
        self.assertEqual(opt.szDescription(), "Test option E")  	    	       

        self.assertRaises(IndexError, menu.__getitem__, 5)  	    	       
        self.assertRaises(IndexError, menu.__getitem__, 6)  	    	       
        self.assertRaises(IndexError, menu.__getitem__, -1)  	    	       
        self.assertRaises(IndexError, menu.__getitem__, -2)  	    	       

    def test_is_valid_command(self):  	    	       
        """Ensure Menu can distinguish bad commands from the good ones"""  	    	       
        menu = Menu("Validate Commands")  	    	       
        menu += MenuOption("A", "Test option A")  	    	       
        menu += MenuOption("B", "Test option B")  	    	       
        menu += MenuOption("C", "Test option C")  	    	       
        menu += MenuOption("D", "Test option D")  	    	       
        menu += MenuOption("E", "Test option E")  	    	       
        self.assertTrue(menu.bIsValidCommand("A"))  	    	       
        self.assertTrue(menu.bIsValidCommand("B"))  	    	       
        self.assertTrue(menu.bIsValidCommand("C"))  	    	       
        self.assertTrue(menu.bIsValidCommand("D"))  	    	       
        self.assertTrue(menu.bIsValidCommand("E"))  	    	       

        self.assertTrue(menu.bIsValidCommand("a"))  	    	       
        self.assertTrue(menu.bIsValidCommand("b"))  	    	       
        self.assertTrue(menu.bIsValidCommand("c"))  	    	       
        self.assertTrue(menu.bIsValidCommand("d"))  	    	       
        self.assertTrue(menu.bIsValidCommand("e"))  	    	       

        self.assertFalse(menu.bIsValidCommand("x"))  	    	       
        self.assertFalse(menu.bIsValidCommand("X"))  	    	       
        self.assertFalse(menu.bIsValidCommand("Y"))  	    	       
        self.assertFalse(menu.bIsValidCommand("Z"))  	    	       
        self.assertFalse(menu.bIsValidCommand("?"))  	    	       

if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
