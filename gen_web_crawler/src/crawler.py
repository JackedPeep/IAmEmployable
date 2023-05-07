#!/usr/bin/python3  	    	       

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


# python -m pip install --user -r requirements.txt  	    	       
from bs4 import BeautifulSoup  	    	       
from urllib.parse import urlparse, urljoin, urldefrag  	    	       
import requests  	    	       
import sys  	    	       
import time  	    	       


def crawl(url, visited = [], depth = 0, maxdepth = 3, tab = ""):

    """
    Given an absolute URL, print each hyperlink found within the document.  	    	       
    This function will need more parameters.  	    	       

    Your task is to make this into a recursive function that follows hyperlinks  	    	       
    until one of two base cases are reached:  	    	       

    0) No new, unvisited links are found  	    	       
    1) The maximum depth of recursion is reached  	    	       
    """
    # If invalid url return
    if depth >= maxDepth:
        return

    if url in visited:
        return
#If valid url return
    else:
        visited.append(url)
        if depth != 0:
            for i in range(depth):
                tab += "\t"
        print(tab + url)


        try:
            # if an error happens anywhere in this `try` block...
            html = requests.get(url)



        except Exception as e:
            # ... this block of code will be run in response
            print(f"Failed to get {url} because {e}")

        if html.status_code == 200:
            try:
                soup = BeautifulSoup(html.text, 'html.parser')
                links = soup.find_all('a')
                if links:
                    for a in links:
                        newUrl = a.get('href')
                        parsedUrl = urlparse(newUrl)
                        if parsedUrl.scheme != "https" and parsedUrl.scheme != "http":
                            continue
                        elif parsedUrl.netloc == "":
                            newUrl = url.join(url, newUrl)

                        newUrl = urldefrag(newUrl)
                        crawl(newUrl.url, visited=visited, depth=depth + 1, maxdepth=maxDepth)

            except Exception as e:
                print(f"An exception occurred: {e}")





# If the crawler.py module is loaded as the main module, allow our `crawl` function to be used as a command line tool  	    	       
if __name__ == "__main__":  	    	       

    ## If no arguments are given...
    timeStart = time.time()
    if len(sys.argv) < 2:  	    	       
        print("Error; No URL argument, please input an absolute URL.", file=sys.stderr)
        exit(0)  	    	       
    else:
        url = urlparse(sys.argv[1])
        if url.netloc == "":
            print("Error;`url` is not absolute:", file=sys.stderr)
            sys.exit(0)

        if url.scheme != "https" and url.scheme != "http":
            print("Error;URL scheme must be http or https:", file=sys.stderr)
            sys.exit(0)
    maxDepth = 3

    if len(sys.argv) > 2:
        if sys.argv[2].isnumeric():
            if int(sys.argv[2]) > 0:
                maxDepth = int(sys.argv[2])

    plural = 's' if maxDepth != 1 else ''
    print(f"Crawling from {sys.argv[1]} to a maximum depth of {maxDepth} link{plural}")


    try:
        crawl(sys.argv[1], maxdepth=maxDepth)
    except:
        print("Exiting")


    timeFinish = time.time()

    timeTotal = timeFinish - timeStart

    print("Your run time is "+str(timeTotal)+"seconds.")



