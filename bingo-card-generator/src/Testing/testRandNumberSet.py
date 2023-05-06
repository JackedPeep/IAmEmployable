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

# Tests the RandNumberSet Class  	    	       

import unittest  	    	       
from RandNumberSet import RandNumberSet  	    	       


class TestRandNumberSet(unittest.TestCase):  	    	       
    def setUp(self):  	    	       
        self.ns3 = RandNumberSet(3, 19)  	    	       
        self.ns4 = RandNumberSet(4, 32)  	    	       
        self.ns8 = RandNumberSet(8, 192)  	    	       
        self.ns16 = RandNumberSet(16, 8192)  	    	       

    def test_len(self):  	    	       
        """Ensure that a RandNumberSet's length is as expected"""  	    	       
        self.assertEqual(len(self.ns3), 3)  	    	       
        self.assertEqual(len(self.ns4), 4)  	    	       
        self.assertEqual(len(self.ns8), 8)  	    	       
        self.assertEqual(len(self.ns16), 16)  	    	       

    def test_getitem(self):  	    	       
        """  	    	       
        Ensure that RandNumberSet  	    	       
        * retrieves the same data each time the same row is requested  	    	       
        * raises IndexError for requests of out-of-bounds rows  	    	       
        * shuffling the RandNumberSet does not affect the boundaries  	    	       
        """  	    	       
        for i in range(len(self.ns8)):  	    	       
            self.assertEqual(self.ns8[i], self.ns8[i])  	    	       
        self.ns8.shuffle()  	    	       
        for i in range(len(self.ns8)):  	    	       
            self.assertEqual(self.ns8[i], self.ns8[i])  	    	       

        for i in range(len(self.ns16)):  	    	       
            self.assertEqual(self.ns16[i], self.ns16[i])  	    	       
        self.ns16.shuffle()  	    	       
        for i in range(len(self.ns16)):  	    	       
            self.assertEqual(self.ns16[i], self.ns16[i])  	    	       

        for _ in range(3):  	    	       
            self.assertRaises(IndexError, self.ns4.__getitem__, -1)  	    	       
            self.assertRaises(IndexError, self.ns4.__getitem__, -10)  	    	       
            self.assertRaises(IndexError, self.ns4.__getitem__, 4)  	    	       
            self.assertRaises(IndexError, self.ns4.__getitem__, 5)  	    	       
            self.assertRaises(IndexError, self.ns4.__getitem__, 6)  	    	       
            self.assertRaises(IndexError, self.ns4.__getitem__, 3000)  	    	       
            self.ns4.shuffle()  	    	       
            self.assertRaises(IndexError, self.ns16.__getitem__, -1)  	    	       
            self.assertRaises(IndexError, self.ns16.__getitem__, -10)  	    	       
            self.assertRaises(IndexError, self.ns16.__getitem__, 17)  	    	       
            self.assertRaises(IndexError, self.ns16.__getitem__, 18)  	    	       
            self.assertRaises(IndexError, self.ns16.__getitem__, 19)  	    	       
            self.assertRaises(IndexError, self.ns16.__getitem__, 3000)  	    	       
            self.ns16.shuffle()  	    	       

    def test_next_row(self):  	    	       
        """  	    	       
        Ensure that a RandNumberSet's .next_row() method  	    	       
        * returns `None` when exhausted  	    	       
        * can be reset by `.shuffle()`  	    	       
        * retrieves different rows each time it's called  	    	       
        """  	    	       
        # In my implementation, once a RandNumberSet is exhausted, repeated invocations of `.getNext()` returns None  	    	       
        for i in range(len(self.ns16)):  	    	       
            self.assertIsNotNone(self.ns16.next_row())  	    	       
        self.assertIsNone(self.ns16.next_row())  	    	       

        self.ns16.shuffle()  	    	       

        for i in range(len(self.ns16)):  	    	       
            self.assertIsNotNone(self.ns16.next_row())  	    	       
        self.assertIsNone(self.ns16.next_row())  	    	       

        self.assertNotEqual(self.ns8.next_row(), self.ns8.next_row())  	    	       
        self.assertNotEqual(self.ns8.next_row(), self.ns8.next_row())  	    	       
        self.assertNotEqual(self.ns8.next_row(), self.ns8.next_row())  	    	       
        self.assertNotEqual(self.ns8.next_row(), self.ns8.next_row())  	    	       
        self.assertIsNone(self.ns8.next_row())  	    	       

    def test_no_duplicates(self):  	    	       
        """Ensure that a RandNumberSet contains no duplicates"""  	    	       

        # Here I use a set to quickly and easily detect duplicates:  	    	       
        # First, create a list of all the numbers yielded from a RandNumberSet  	    	       
        # Then convert that list into a set  	    	       
        # If the length of the list is not equal to that of the set, then there  	    	       
        # must have been duplicates in the list  	    	       
        seen = set()  	    	       
        for segment in self.ns3.get_segments():  	    	       
            for n in segment:  	    	       
                self.assertNotIn(n, seen)  	    	       
                seen.add(n)  	    	       

if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
