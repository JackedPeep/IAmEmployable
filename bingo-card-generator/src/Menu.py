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

class Menu():  	    	       
    """  	    	       
    Present a Menu made of of MenuOptions to a user, and continue to prompt until they provide valid input  	    	       

    When the user's selection is alphabetic, it is matched without regard to case;  	    	       
    both upper- and lower-case letters are accepted  	    	       
    """  	    	       

    def __init__(self, szHeader):  	    	       
        """  	    	       
        Create an empty Menu  	    	       

        Takes a string describing the Menu as input  	    	       
        """  	    	       
        self.__m_szHeader = szHeader  	    	       
        self.__m_options = []  	    	       

    def __iadd__(self, option):  	    	       
        """  	    	       
        Append an option to the Menu  	    	       

        This method was called `operator+` in the C++ version  	    	       

        Be careful: No check is made for a duplicate MenuOption command  	    	       
        """  	    	       
        self.__m_options.append(option)  	    	       
        return self  	    	       

    def __getitem__(self, nIdx):  	    	       
        """  	    	       
        Return a MenuOption  	    	       

        This method was called `operator[]` in the C++ version  	    	       

        Retrieve an option from the menu with the indexing operator []  	    	       
        """  	    	       
        if 0 <= nIdx < len(self):  	    	       
            return self.__m_options[nIdx]  	    	       
        else:  	    	       
            raise IndexError  	    	       

    def __len__(self):  	    	       
        """  	    	       
        Return an integer: the number of MenuOptions contained in this Menu  	    	       

        This method was called `length` in the C++ version, and was meant to be explicitly called  	    	       
        """  	    	       
        return len(self.__m_options)  	    	       

    def bIsValidCommand(self, chCommand):  	    	       
        """  	    	       
        Return a Boolean: whether a command is contained in our list of MenuOptions  	    	       

        Consider upper-case options the same as lower-case  	    	       
        """  	    	       
        for i in range(len(self)):  	    	       
            if chCommand.upper() == self[i].chCommand().upper():  	    	       
                return True  	    	       
        return False  	    	       

    def prompt(self):  	    	       
        """  	    	       
        Return None: Display the menu and take a command from the user  	    	       

        The menu is repeated until the user provides a recognized command  	    	       
        """  	    	       
        while True:  	    	       
            options = []  	    	       

            print(f"\n{self.__m_szHeader} menu:")  	    	       
            for i in range(len(self)):  	    	       
                option = self[i]  	    	       
                if option is not None:  	    	       
                    print(option)  	    	       
                    options += option.chCommand()  	    	       

            print(f"\nEnter a {self.__m_szHeader} command ({', '.join(options)})")  	    	       
            command = input()  	    	       
            if self.bIsValidCommand(command):  	    	       
                return command  	    	       
            else:  	    	       
                print(f"'{command.strip()}' is not a valid option")  	    	       
