#!/usr/bin/env python  	    	       

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


import sys  	    	       

from Concatenate import cat, tac  	    	       
from CutPaste import cut, paste  	    	       
from Grep import grep  	    	       
from Partial import head, tail  	    	       
from Sorting import sort  	    	       
from WordCount import wc  	    	       
from Usage import usage  	    	       


if len(sys.argv) < 2:  	    	       
    usage()  	    	       
    sys.exit(1)  	    	       
else:  	    	       
    #TODO: determine which tool the user has invoked
    tool = sys.argv[1]
    if tool == 'cat':  	    	       
        if len(sys.argv) < 3:
            usage('Missing Files', 'cat')
        else:
            cat(*sys.argv[2:])
    elif tool == 'tac':
        if len(sys.argv) < 3:
            usage('Missing Files', 'tac')
        else:
            tac(*sys.argv[2:])
    elif tool == 'cut':
        if len(sys.argv) < 3:
            usage('Missing Files', 'cut')
        elif sys.argv[2] == '-f':
            if len(sys.argv) < 5:
                usage('Missing Arguments', 'cut')
            elif not sys.argv[3].isdigit():
                usage('Missing column numbers', 'cut')
            else:
                cut(*sys.argv[4:], col=int(sys.argv[3]))
        else:
            cut(*sys.argv[2:])
    elif tool == 'paste':
        if len(sys.argv) < 3:
            usage('Missing Files', 'paste')
        else:
            paste(*sys.argv[2:]) 	    	       
    elif tool == 'grep':
        if len(sys.argv) < 4:
            usage('Missing Arguments', 'grep')
        else:
            grep(sys.argv[3:], sys.argv[2])
            
    elif tool == 'head':
        if len(sys.argv) < 3:
            usage('Missing Files', 'head')
        elif sys.argv[2] == '-n':
            if len(sys.argv) < 5:
                usage('Missing Arguments', 'head')              
            elif not sys.argv[3].isdigit():
                 usage('Missing number of lines', 'head')
            else:
                head(*sys.argv[4:],nLine=int(sys.argv[3]))
        else:
            head(*sys.argv[2:])
    elif tool == 'tail':
        
        if len(sys.argv) < 3:
            usage('Missing Files', 'tail')
        elif sys.argv[2] == '-n':
            if len(sys.argv) < 5:
                usage('Missing Arguments', 'tail')
            elif not sys.argv[3].isdigit():
                usage('Missing number of lines', 'tail')
            else:
                tail(*sys.argv[4:], nLine=int(sys.argv[3]))
        else:
            tail(*sys.argv[2:]) 	    	       
    elif tool == 'sort':
        if len(sys.argv) < 3:
            usage('Missing Files', 'sort')
        else:
            sort(*sys.argv[2:])  	    	       
    elif tool == 'wc':
        if len(sys.argv) < 3:
            usage('Missing Files', 'wc')
        else:
            wc(*sys.argv[2:])
        #TODO: Check for options for given tool
        #TODO: call on that tool, forwarding any remaining arguments to it 	    	       
