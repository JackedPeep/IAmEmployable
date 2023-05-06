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

# Tests the Deck Class  	    	       

import unittest  	    	       
import Deck  	    	       


class TestDeck(unittest.TestCase):  	    	       
    def setUp(self):  	    	       
        size = 7  	    	       
        self.deck2 = Deck.Deck(card_size=size, num_cards=2, max_num=3*size*size)  	    	       

        size = 16  	    	       
        self.deck16 = Deck.Deck(card_size=size, num_cards=16, max_num=3*size*size)  	    	       
        self.deck8192 = Deck.Deck(card_size=size, num_cards=8192, max_num=3*size*size)  	    	       

    def test_len(self):  	    	       
        """Ensure that Decks contain expected number of cards"""  	    	       
        self.assertEqual(len(self.deck2), 2)  	    	       
        self.assertEqual(len(self.deck16), 16)  	    	       
        self.assertEqual(len(self.deck8192), 8192)  	    	       

    def test_card(self):  	    	       
        """Ensure that Cards can be accessed from within a Deck"""  	    	       

        # In my implementation, an attempt to get a non-existent card results in `None`  	    	       
        # Cards are indexed by their ID number  	    	       

        self.assertIsNone(self.deck2.card(0))  	    	       
        self.assertIsNotNone(self.deck2.card(1))  	    	       
        self.assertIsNotNone(self.deck2.card(2))  	    	       
        self.assertIsNone(self.deck2.card(3))  	    	       

        self.assertIsNone(self.deck16.card(0))  	    	       
        self.assertIsNotNone(self.deck16.card(8))  	    	       
        self.assertIsNotNone(self.deck16.card(16))  	    	       
        self.assertIsNone(self.deck16.card(17))  	    	       

        self.assertIsNone(self.deck8192.card(0))  	    	       
        self.assertIsNotNone(self.deck8192.card(4096))  	    	       
        self.assertIsNotNone(self.deck8192.card(8192))  	    	       
        self.assertIsNone(self.deck8192.card(8193))  	    	       


if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
