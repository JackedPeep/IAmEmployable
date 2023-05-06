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

from Card import Card  	    	       
from RandNumberSet import RandNumberSet  	    	       


class Deck():  	    	       
    def __init__(self, card_size, num_cards, max_num):  	    	       
        """  	    	       
        Deck constructor  	    	       
        """  	    	       
        self.card_size = card_size
        self.num_cards = num_cards
        self.max_num = max_num

        self.cardArray = []
        for i in range(num_cards):
           self.cardArray.append(Card(i,RandNumberSet(card_size,max_num)))

    def __len__(self):  	    	       
        """  	    	       
        Return an integer: the number of cards in this deck  	    	       

        This method was called `size` in the C++ version  	    	       
        """  	    	       
        return self.num_cards

    def __getitem__(self, n):  	    	       
        """  	    	       
        Return Card N from the Deck  	    	       

        This method was called `operator[]` in the C++ version  	    	       
        """  	    	       
        return self.cardArray[n]

    def __str__(self):  	    	       
        """  	    	       
        Return a string: return the entire Deck as a string  	    	       

        This is basically equivalent to the `operator<<` method in the C++ version  	    	       
        """  	    	       
        for i in range(self.num_cards):
            print(str(self.cardArray[i]))

