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


def cut(*files, col = [1]):
    """remove sections from each line of files"""
    for file in files:
        oFile = open(file)
        column = ''
        for line in range(len(file)):
            for i in col:
                fLine = oFile.readline()
                fLine = fLine.split(',')
                if (i > len(fLine)):
                    column += '\n'
                else:
                    column += fLine[i-1] + '\n'
        print(column)
        oFile.close()


def paste(*files):
    """merge lines of files"""
    if len(files) == 1:
        for file in files:
           oFile = open(file)

           print(oFile.read(), end = "")

           oFile.close()
    else:
        lengthCash = []
        i = 0
        oFile = [None] * len(files)
        for file in files:
            oFile[i] = open(file)
            lengthCash.append(len(oFile[i].readlines()))
            colLength = max(lengthCash)
            oFile[i].seek(0)
            i += 1

        for line in range(colLength):
            nLine = ''
            for file in range(len(files)):
                fline = oFile[file].readline()
                fline = fline.strip()
                nLine += fline
                if file != len(files)-1:
                    nLine += ','
            print(nLine)

        for file in range(len(files)):
            oFile[file].close()

if __name__ == '__main__':
    #paste("../data/names8","../data/ages8", "../data/colors8", "../data/verbs8")
    cut("../data/people.csv")