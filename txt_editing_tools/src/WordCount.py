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


def wc(*files):
    """print newline, word, and byte counts for each file"""
    tlines = 0
    twords = 0
    tbytes = 0

    for file in files:
        newLine = 0
        words = 0
        byteCount = 0
        oFile = open(file)
        count = str(oFile.readline())

        while count != '':


            wordVector = count.split()

            newLine += 1
            words += len(wordVector)
            byteCount += len(count)
            count = str(oFile.readline())

        print(str(newLine).ljust(5, " "),end=" ")
        print(str(words).ljust(5, " "),end=" ")
        print(str(byteCount).ljust(5, " "), end=" ")
        print(str(file))

        tlines += newLine
        twords += words
        tbytes += byteCount



        oFile.close()

    if len(files) > 1:
        print(str(tlines).ljust(5, " "),end=" ")
        print(str(twords).ljust(5, " "),end=" ")
        print(str(tbytes).ljust(5, " "), end=" ")
        print("Total")
        
if __name__ == "__main__":
    wc("../data/wordcount", "../data/words5")
