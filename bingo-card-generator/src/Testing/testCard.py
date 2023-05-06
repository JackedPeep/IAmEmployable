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

from Card import Card  	    	       
from RandNumberSet import RandNumberSet  	    	       


class TestCard(unittest.TestCase):  	    	       

    def setUp(self):  	    	       
        """  	    	       
        Create no fewer than 5 Card objects to test  	    	       

        Create a mixture of odd and even-sized cards  	    	       
        """


        self.card3 = Card(3)
        self.card4 = Card(4)
        self.card5 = Card(5)
        self.card6 = Card(6)
        self.card7 = Card(7)
        self.card8 = Card(8)
        self.card9 = Card(9)
        self.cardX = Card(10)




    def test_len(self):  	    	       
        """Assert that each card's size is as expected"""

        self.assertEqual(self.card3.len, 3, "error; not equal")
        self.assertEqual(self.card4.len, 4, "error; not equal")
        self.assertEqual(self.card5.len, 5, "error; not equal")
        self.assertEqual(self.card6.len, 6, "error; not equal")
        self.assertEqual(self.card7.len, 7, "error; not equal")
        self.assertEqual(self.card8.len, 8, "error; not equal")
        self.assertEqual(self.card9.len, 9, "error; not equal")
        self.assertEqual(self.cardX.len, 10, "error; not equal")


    def test_id(self):  	    	       
        """Assert that each card's ID number is as expected"""

        self.assertEqual(self.card3.id, 3, "error; not equal")
        self.assertEqual(self.card4.id, 4, "error; not equal")
        self.assertEqual(self.card5.id, 5, "error; not equal")
        self.assertEqual(self.card6.id, 6, "error; not equal")
        self.assertEqual(self.card7.id, 7, "error; not equal")
        self.assertEqual(self.card8.id, 8, "error; not equal")
        self.assertEqual(self.card9.id, 9, "error; not equal")
        self.assertEqual(self.cardX.id, 10, "error; not equal")



    def test_freeSquares(self):  	    	       
        """  	    	       
        Ensure that odd-sized cards have 1 "Free!" square in the center  	    	       
        Also test that even-sized cards do not have a "Free!" square by examining the 2x2 region about their centers  	    	       
        """
        # (row + 1)/2 =center

        self.assertEqual(self.card3.number_at(2,2), "Free!")
        self.assertEqual(self.card5.number_at(3,3), "Free!")
        self.assertEqual(self.card7.number_at(4,4), "Free!")
        self.assertEqual(self.card9.number_at(5,5), "Free!")

        self.assertNotEqual(self.card4.number_at(2, 2), "Free!")
        self.assertNotEqual(self.card4.number_at(2, 3), "Free!")
        self.assertNotEqual(self.card4.number_at(3, 3), "Free!")
        self.assertNotEqual(self.card4.number_at(3, 2), "Free!")
        self.assertNotEqual(self.card6.number_at(3, 3), "Free!")
        self.assertNotEqual(self.card6.number_at(3, 4), "Free!")
        self.assertNotEqual(self.card6.number_at(4, 4), "Free!")
        self.assertNotEqual(self.card6.number_at(4, 3), "Free!")
        self.assertNotEqual(self.card8.number_at(4, 4), "Free!")
        self.assertNotEqual(self.card8.number_at(4, 5), "Free!")
        self.assertNotEqual(self.card8.number_at(5, 5), "Free!")
        self.assertNotEqual(self.card8.number_at(5, 4), "Free!")
        self.assertNotEqual(self.cardX.number_at(5, 5), "Free!")
        self.assertNotEqual(self.cardX.number_at(5, 6), "Free!")
        self.assertNotEqual(self.cardX.number_at(6, 6), "Free!")
        self.assertNotEqual(self.cardX.number_at(6, 5), "Free!")



    def test_no_duplicates(self):  	    	       
        """Ensure that Cards do not contain duplicate numbers"""
        seen = set()
        for row in range(self.card3.len()):
            for col in range(self.card3.len()):
                self.assertNotIn(self.card3.number_at(row,col), seen)
                seen.add(self.card3.number_at(row,col))
        seen = set()
        for row in range(self.card4.len()):
            for col in range(self.card4.len()):
                self.assertNotIn(self.card4.number_at(row, col), seen)
                seen.add(self.card4.number_at(row, col))
        seen = set()
        for row in range(self.card5.len()):
            for col in range(self.card5.len()):
                self.assertNotIn(self.card5.number_at(row, col), seen)
                seen.add(self.card5.number_at(row, col))
        seen = set()
        for row in range(self.card6.len()):
            for col in range(self.card6.len()):
                self.assertNotIn(self.card6.number_at(row, col), seen)
                seen.add(self.card6.number_at(row, col))
        seen = set()
        for row in range(self.card7.len()):
            for col in range(self.card7.len()):
                self.assertNotIn(self.card7.number_at(row, col), seen)
                seen.add(self.card7.number_at(row, col))
        seen = set()
        for row in range(self.card8.len()):
            for col in range(self.card8.len()):
                self.assertNotIn(self.card8.number_at(row, col), seen)
                seen.add(self.card8.number_at(row, col))
        seen = set()
        for row in range(self.card9.len()):
            for col in range(self.card9.len()):
                self.assertNotIn(self.card9.number_at(row, col), seen)
                seen.add(self.card9.number_at(row, col))
        seen = set()
        for row in range(self.cardX.len()):
            for col in range(self.cardX.len()):
                self.assertNotIn(self.cardX.number_at(row, col), seen)
                seen.add(self.cardX.number_at(row, col))

if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
