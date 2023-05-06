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

import random  	    	       


class RandNumberSet():  	    	       

    def __init__(self, nSize, nMax):  	    	       
        """  	    	       
        Create a RandNumberSet  	    	       

        'nSize': a parameter restricted to be in the range [3..16]  	    	       
        'nMax': a parameter restricted to be no less than `nSize*nSize`  	    	       

        Numbers are kept in separate segments so that the numbers within  	    	       
        columns on the resulting Bingo! card increase from left to right.  	    	       

        Within a column numbers are unordered.  	    	       

        A newly initialized RandNumberSet may present its numbers in  	    	       
        order.  Use .shuffle() to mix it up.  	    	       
        """  	    	       
        self.__m_nSize = nSize  	    	       
        self.__m_nMax = nMax  	    	       
        self.__m_nRowPos = 0  	    	       
        self.__m_segments = []  	    	       
        segment_size = nMax // self.__m_nSize  # n.b. `//` operator means "integer division"  	    	       
        remainder = nMax % self.__m_nSize  	    	       
        low = 1  	    	       
        for segment in range(1, self.__m_nSize + 1):  	    	       
            high = low + segment_size  	    	       
            # When `len(RandNumberSet)` is not evenly divisible by `nSize`,  	    	       
            # there will be some numbers left over.  Distribute these extra  	    	       
            # numbers starting from segment #0, going up from there  	    	       
            if segment <= remainder:  	    	       
                high += 1  	    	       
            # "high + 1" is not necessary in the operator below because high = low + segment size, and low is 1.
            self.__m_segments.append(list(range(low, high)))
            low = high  	    	       

    def shuffle(self):  	    	       
        """  	    	       
        Shuffle each segment and reset the current row position so that  	    	       
        next_row() will start from the top again.  	    	       
        """  	    	       
        for seg in self.__m_segments:  	    	       
            random.shuffle(seg)  	    	       
        self.__m_nRowPos = 0  	    	       

    def next_row(self):  	    	       
        """  	    	       
        Return the next row of Bingo numbers, or None if the RandNumberSet  	    	       
        is exhausted.  	    	       

        This method automatically keeps track of which row is up next  	    	       
        """  	    	       
        if self.__m_nRowPos >= self.__m_nSize:  	    	       
            return None  	    	       
        row = []  	    	       
        for seg in self.__m_segments:  	    	       
            row.append(seg[self.__m_nRowPos])  	    	       
        self.__m_nRowPos += 1  	    	       
        return row  	    	       

    def get_segments(self):  	    	       
        """  	    	       
        Accessor to private member m_segments  	    	       
        """  	    	       
        return self.__m_segments  	    	       

    def __str__(self):  	    	       
        """  	    	       
        Return a string representing the RandNumberSet  	    	       

        This is basically equivalent to the `operator<<` method in the C++ version  	    	       
        """  	    	       
        strs = []  	    	       
        for seg in self.__m_segments:  	    	       
            strs.append(str(seg))  	    	       
        return '\n'.join(strs)  	    	       

    def __len__(self):  	    	       
        """  	    	       
        This dunder makes `len()` work on RandNumberSets  	    	       

        The length of a RandNumberSet is equal to the number of segments  	    	       
        it contains; in other words, len(RandNumberSet) == card size.  	    	       

        This method was called `size` in the C++ version, and was meant to be explicitly called  	    	       
        """  	    	       
        return self.__m_nSize  	    	       

    def __getitem__(self, n):  	    	       
        """  	    	       
        Return the specified row of Bingo numbers, raise IndexError when out-of-bounds  	    	       

        This method was called `operator[]` in the C++ version  	    	       
        """  	    	       
        if 0 <= n < self.__m_nSize:  	    	       
            row = []  	    	       
            for seg in self.__m_segments:  	    	       
                row.append(seg[n])  	    	       
            return row  	    	       
        else:  	    	       
            raise IndexError  	    	       
