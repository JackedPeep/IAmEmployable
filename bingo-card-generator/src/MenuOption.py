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

class MenuOption():  	    	       
    """  	    	       
    Represent an option in a text-based Menu  	    	       

    An option is a single letter paired with a description string  	    	       
    """  	    	       

    def __init__(self, chCommand, szDescription):  	    	       
        """  	    	       
        Create a MenuOption  	    	       
        """  	    	       
        self.__m_chCommand = chCommand  	    	       
        if self.__m_chCommand == '':  	    	       
            self.__m_chCommand = '?'  	    	       
        elif len(self.__m_chCommand) > 1:  	    	       
            self.__m_chCommand = self.__m_chCommand[0]  	    	       

        self.__m_szDescription = szDescription  	    	       
        if self.__m_szDescription == '':  	    	       
            self.__m_szDescription = '???'  	    	       

    def chCommand(self):  	    	       
        """  	    	       
        Return a string: the command letter that activates this MenuOption  	    	       
        """  	    	       
        return self.__m_chCommand  	    	       

    def szDescription(self):  	    	       
        """  	    	       
        Return a string: the human-friendly description of this MenuOption  	    	       
        """  	    	       
        return self.__m_szDescription  	    	       

    def __str__(self):  	    	       
        """  	    	       
        Return a string: the command letter combined with its description  	    	       

        This is basically equivalent to the `operator<<` method in the C++ version  	    	       
        """  	    	       
        return f"{self.__m_chCommand}) {self.__m_szDescription}"  	    	       
