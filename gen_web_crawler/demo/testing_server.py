#!/usr/bin/env python3  	    	       

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

from http.server import HTTPServer, BaseHTTPRequestHandler  	    	       
from random import randint  	    	       
import sys  	    	       
import threading  	    	       
import time  	    	       


VERSION = "1.1"  	    	       
def usage():  	    	       
    print(f"""CS 1440 Recursive Web Crawler Testing Server v{VERSION}  	    	       

Usage:  	    	       
  python test_server.py [-host localhost] [-port 8000]  	    	       
  python test_server.py -help  	    	       

Example: Listen on http://localhost:8000  	    	       
  python test_server.py  	    	       

Example: Listen on http://localhost:4444  	    	       
  python test_server.py -port 4444  	    	       

Example: Listen on http://0.0.0.0:8888  	    	       
  python test_server.py -host 0.0.0.0 -port 8888  	    	       

`-host 0.0.0.0` makes the server accessible from OUTSIDE your computer,  	    	       
  provided that you know your computer's IP address and your firewall allows  	    	       
  it.  Do this ONLY if you understand what this entails and accept the risk!  	    	       

Most options are set from the first URL the server responds to.  	    	       
Point your browser to the running server for full instructions.  	    	       
""")  	    	       
    exit(0)  	    	       


def plural(n, singular='', plural='s'):  	    	       
    return singular if n == 1 else plural  	    	       

def red(s):  	    	       
    return "\x1b[1;31m" + str(s) + "\x1b[0m"  	    	       

def green(s):  	    	       
    return "\x1b[1;32m" + str(s) + "\x1b[0m"  	    	       

def blue(s):  	    	       
    return "\x1b[1;34m" + str(s) + "\x1b[0m"  	    	       

def cyan(s):  	    	       
    return "\x1b[1;36m" + str(s) + "\x1b[0m"  	    	       

def yellow(s):  	    	       
    return "\x1b[1;33m" + str(s) + "\x1b[0m"  	    	       


class TrackingServer(HTTPServer):  	    	       
    """  	    	       
    An HTTPServer that keeps track of paths which were visited by GET requests  	    	       
    Can display a report summarizing visits  	    	       
    Out of necessity this class stores some information that seems more  	    	       
    appropriate to track in the RequestHandlerClass object.  This is because  	    	       
    a fresh RequestHandlerClass object is instantiated for each request, and the  	    	       
    information would be lost after the request concludes.  	    	       
    """  	    	       
    PAGES = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  	    	       
    RESTART = True  	    	       
    TIMER = 3  	    	       
    DEPTH = 4  	    	       
    BREADTH = 3  	    	       
    FRAGMENTS = True  	    	       
    LANDMINES = False  	    	       
    RESET = 0  	    	       
    DEADEND = True  	    	       
    VERBOSE = False  	    	       


    def __init__(self, server_address, RequestHandlerClass):  	    	       
        super().__init__(server_address, RequestHandlerClass)  	    	       
        self.pages = None  	    	       
        self.non_existant = None  	    	       

        # The server restarts itself automatically when its timeout is reached  	    	       
        # Set this to False to get your command line back after this run is over.  	    	       
        # You can also press Ctrl-C or visit the path '/shutdown' to prevent the  	    	       
        # server from restarting.  	    	       
        self.restart = TrackingServer.RESTART  	    	       

        # Number of seconds to wait before automatically shutting down  	    	       
        # This is to prevent a runaway crawler from going forever  	    	       
        # Setting to 0 disables auto shutdown  	    	       
        # /timer=[0-n]  	    	       
        self.timer = TrackingServer.TIMER  	    	       
        self.countdown_active = False  	    	       

        # Maximum depth of links in website  	    	       
        # /depth=[0-N]  	    	       
        self.depth = TrackingServer.DEPTH  	    	       

        # How many branches to create at each juncture  	    	       
        # [1-62]  	    	       
        self.breadth = TrackingServer.BREADTH  	    	       

        # Control the presence of fragments in generated URLs  	    	       
        self.fragments = TrackingServer.FRAGMENTS  	    	       

        # Immediately quit if a page is visited more than once  	    	       
        self.landmines = TrackingServer.LANDMINES  	    	       

        # % probability that a page will be generated with a "reset" link  	    	       
        # which, when visited, results in a connection reset exception  	    	       
        self.reset = TrackingServer.RESET  	    	       

        # Generate a link to /deadend on every page; this page has no outbound links,  	    	       
        # and should be visited at most once  	    	       
        self.deadend = TrackingServer.DEADEND  	    	       

        # Produce a verbose report of pages visited after the server quits  	    	       
        self.verbose = TrackingServer.VERBOSE  	    	       

        print(yellow(f"Serving from http://{server_address[0]}:{server_address[1]}/\nPress Ctrl-C or visit http://{server_address[0]}:{server_address[1]}/shutdown/ to quit\n"))  	    	       


    def shutdown_timer(self):  	    	       
        """  	    	       
        Shut server down a few seconds after the first page is visited.  	    	       
        This prevents a runaway crawler from going forever.  	    	       
        """  	    	       
        self.countdown_active = True  	    	       
        while self.timer > 0:  	    	       
            print(cyan(f"Server will shutdown in {self.timer} second{plural(self.timer)}..."))  	    	       
            time.sleep(1)  	    	       
            self.timer -= 1  	    	       
        self.shutdown()  	    	       


    def report(self):  	    	       
        if self.pages is None:  	    	       
            return  	    	       

        zero = []  	    	       
        once = []  	    	       
        many = []  	    	       
        for page in self.pages:  	    	       
            if self.pages[page] == 0:  	    	       
                zero.append(page)  	    	       
            elif self.pages[page] == 1:  	    	       
                once.append(page)  	    	       
            elif page == '/' and self.pages['/'] == 2:  	    	       
                # the initial page is often visited twice, and this is not an error  	    	       
                continue  	    	       
            else:  	    	       
                many.append(page)  	    	       

        l = len(once)  	    	       
        if l > 0:  	    	       
            print(green(f"{l} page{plural(l, ' was', 's were')} visited exactly once"))  	    	       
            if self.verbose:  	    	       
                for page in once:  	    	       
                    print(f"\t{page}")  	    	       

        l = len(zero)  	    	       
        if l > 0:  	    	       
            print(green(f"\n{l} page{plural(l, ' was', 's were')} not visited at all"))  	    	       
            if self.verbose:  	    	       
                for page in zero:  	    	       
                    print(f"\t{page}")  	    	       

        l = len(many)  	    	       
        if l > 0:  	    	       
            print(red(f"\n{l} page{plural(l, ' was', 's were')} visited many times"))  	    	       
            for page in many:  	    	       
                print(f"\t{page}: {self.pages[page]}")  	    	       

        l = len(self.non_existant)  	    	       
        if l > 0:  	    	       
            print(red(f"\n{l} page{plural(l, ' was', 's were')} visited before they were created:"))  	    	       
            for page in self.non_existant:  	    	       
                print(f"\t{page}")  	    	       


class TrackingHandler(BaseHTTPRequestHandler):  	    	       
    """  	    	       
    A fresh TrackingHandler object is instantiated for each request.  	    	       
    Information that must persist beyond a request must be stored in  	    	       
    the Server instance.  	    	       
    """  	    	       

    def listOfAnchors(self, urls):  	    	       
        """  	    	       
        Form an HTML list of anchor tags (links) pointing to input urls  	    	       
        """  	    	       
        if self.server.deadend:  	    	       
            s = '<li><a href="/deadend">A dead end</a></li>\n'  	    	       
        else:  	    	       
            s = ""  	    	       

        return s + "\n".join([ f'<li>Visit <a href="{link}">{link}</a></li>' for link in urls.keys() ])  	    	       


    def listOfAnchorsWithFragments(self, urls):  	    	       
        """  	    	       
        Form an HTML list of anchor tags (links) pointing to input urls which contain fragments  	    	       
        """  	    	       
        if not self.server.fragments:  	    	       
            return ''  	    	       

        if self.server.deadend:  	    	       
            s = '<li><a href="/deadend#fragment">A dead end with a #fragment</a></li>\n'  	    	       
        else:  	    	       
            s = ""  	    	       

        return s + "\n".join([ f'<li>Visit <a href="{link}#fragment">{link}#fragment</a></li>' for link in urls.keys() ])  	    	       


    def serverInformation(self):  	    	       
        """  	    	       
        Return a list of the server's current settings  	    	       
        """  	    	       
        if self.server.countdown_active:  	    	       
            if self.server.restart:  	    	       
                restart = f"The server will <strong>automatically restart</strong> in <strong>{self.server.timer}</strong> second{plural(self.server.timer)}"  	    	       
            else:  	    	       
                restart = f"The server will <strong>shut itself down</strong> in <strong>{self.server.timer}</strong> second{plural(self.server.timer)}"  	    	       
        else:  	    	       
            restart = "The server will continue to run <strong>until stopped by the user</strong>"  	    	       

        depth = f"Links are created to a maximum depth of <strong>{self.server.depth}</strong>"  	    	       
        breadth = f"<strong>{self.server.breadth}</strong> new link{plural(self.server.breadth)} will be created on each page"  	    	       
        if self.server.fragments:  	    	       
            fragments = "Links are created <strong>with and without</strong> fragments"  	    	       
        else:  	    	       
            fragments = "Links are created <strong>without</strong> fragments"  	    	       

        if self.server.landmines:  	    	       
            landmines = "The server will <strong>immediately shut down</strong> if a link is followed more than once"  	    	       
        else:  	    	       
            landmines = "The server will <strong>keep going</strong> even if a link is followed more than once"  	    	       

        reset = f"<strong>{self.server.reset}%</strong> of generated pages contain a <code>reset</code> link that cause a <code>ConnectionError</code> in the crawler"  	    	       

        if self.server.deadend:  	    	       
            deadend = "The server <strong>will</strong> genereate a link to <code>/deadend</code>"  	    	       
        else:  	    	       
            deadend = "The server <strong>will not</strong> genereate a link to <code>/deadend</code>"  	    	       

        if self.server.verbose:  	    	       
            verbose = "A <strong>detailed</strong> report will be printed to the console at the end"  	    	       
        else:  	    	       
            verbose = "A <strong>brief</strong> report will be printed to the console at the end"  	    	       

        return f"""<h2>Server information</h2>  	    	       
    <div>  	    	       
        <ul>  	    	       
            <li>{restart}</li>  	    	       
            <li>{depth}</li>  	    	       
            <li>{breadth}</li>  	    	       
            <li>{fragments}</li>  	    	       
            <li>{landmines}</li>  	    	       
            <li>{reset}</li>  	    	       
            <li>{deadend}</li>  	    	       
            <li>{verbose}</li>  	    	       
        </ul>  	    	       
    </div>\n"""  	    	       


    def instructions(self):  	    	       
        addr = f"http://{self.server.server_address[0]}/{self.server.server_address[1]}"  	    	       
        return f"""<h2>Instructions</h2>  	    	       
    <div>  	    	       
        <p>Visit <code>/restart</code> to restart the server immediately; new options may be given once the server comes back up.</p>  	    	       
        <p>Visit <code>/shutdown</code> to stop the server and return to the shell.</p>  	    	       
        <p>Server options are set from <em>directives</em> encoded in the path of the first URL visited.</p>  	    	       

        <p>  	    	       
        Directives are specified as <code>name=value</code>, separated by slashes (<code>/</code>).  	    	       

        The order in which directives are specified does not matter.  	    	       

        If the same directive is specified multiple times, the last value seen is used.  	    	       
        </p>  	    	       

        <ul>  	    	       
            <li><code>/restart=[true|false]</code> controls whether the server automatically restarts itself after the timer expires (Default is {TrackingServer.RESTART})</li>  	    	       
            <li><code>/timer=[0..N]</code> how long before the server restarts itself (Default is {TrackingServer.TIMER} seconds)<ul><li>Specify <code>/timer=0</code> to disable the auto-restart timer; this lets you explore the server from the comfort of your web browser</li></ul></li>  	    	       
            <li><code>/depth=[0..N]</code> how deep links generated by the server go before they wrap back around to the beginning (Default is {TrackingServer.DEPTH} levels)</li>  	    	       
            <li><code>/breadth=[1..{len(TrackingServer.PAGES)}]</code> how many new branches to create from each page (Default is {TrackingServer.BREADTH})</li>  	    	       
            <li><code>/fragments=[true|false]</code> whether to create links with URL #fragments (Default is {TrackingServer.FRAGMENTS})</li>  	    	       
            <li><code>/landmines=[true|false]</code> when enabled, visiting a link for the second time causes the server to immediately restart (Default is {TrackingServer.LANDMINES})</li>  	    	       
            <li><code>/reset=[0..100]</code> a percentage of pages containing a "reset" link which triggers a <code>ConnectionError</code> in the crawler (Default is {TrackingServer.RESET}%)</li>  	    	       
            <li><code>/deadend=[true|false]</code> controls whether a "dead-end" link is included on each page (Default is {TrackingServer.DEADEND})</li>  	    	       
            <li><code>/verbose=[true|false]</code> when set, makes the server produce a longer report at the end (Default is {TrackingServer.VERBOSE})</li>  	    	       
        </ul>  	    	       

        <h3>Examples</h3>  	    	       
        <ol start="0">  	    	       
            <li>  	    	       
                Disable the timer and produce a detailed report at the end (the report is shown by visiting <code>{addr}/restart)</code>  	    	       
                <ul><li><code>{addr}/timer=0/verbose=true/</code></li></ul>  	    	       
            </li>  	    	       

            <li>  	    	       
                Set the timer to 60 seconds, disable land mines, the dead end page, and set the maximum depth to 30  	    	       
                <ul><li><code>{addr}/timer=60/landmines=false/deadend=false/depth=30</code></li></ul>  	    	       
            </li>  	    	       
            <li>  	    	       
                Set the breadth to 1 and maximum depth to 20  	    	       
                <ul><li><code>{addr}/breadth=1/depth=20</code></li></ul>  	    	       
            </li>  	    	       
            <li>  	    	       
                The same as above, but disable fragments in links  	    	       
                <ul><li><code>{addr}/breadth=1/depth=20/fragments=false</code></li></ul>  	    	       
            </li>  	    	       
            <li>  	    	       
                Place a "reset" link on 50% of generated pages to test that the crawler handles `ConnectionError` without crashing
                <ul><li><code>{addr}/reset=50/</code></li></ul>  	    	       
            </li>
        </ol>  	    	       
    </div>  	    	       
    """  	    	       

    def respond(self):  	    	       
        """  	    	       
        Called when a valid page is requested to form an HTTP response.  	    	       
        """  	    	       
        self.server.pages[self.path] += 1  	    	       

        # Did the crawler just step on a landmine?  	    	       
        if self.server.landmines and self.server.pages[self.path] > 1:  	    	       
            # special case - the root document '/' is often crawled exactly  	    	       
            # twice - trip the landmine only when this page is visited 3x  	    	       
            if self.path == '/' and self.server.pages['/'] == 2:  	    	       
                pass  	    	       
            else:  	    	       
                print(red("A landmine was tripped! Shutting down immediately..."))  	    	       
                self.server.timer = 0  	    	       
                threading.Thread(target=self.server.shutdown).start()  	    	       
                self.do_503()  	    	       
                return  	    	       

        # The dead end page has no links  	    	       
        elif self.path == "/deadend":  	    	       
            self.send_response(200)  	    	       
            self.send_header('Connection', 'close')  	    	       
            self.end_headers()  	    	       
            self.wfile.write(  	    	       
                    bytes(f"""<!DOCTYPE html>  	    	       
<html lang="en">  	    	       
    <head>  	    	       
        <meta charset="utf-8">  	    	       
        <title>This page is a dead-end</title>  	    	       
    </head>  	    	       
    <body>  	    	       
        <h1>This page is a dead-end</h1>  	    	       
    </body>  	    	       
</html>""", encoding="utf_8"))  	    	       
            return  	    	       

        elif self.path.endswith('/reset'):  	    	       
            # return without sending data back to the browser  	    	       
            # this results in a ConnectionError on the client  	    	       
            self.log_request()  	    	       
            print(f"{red('Resetting the connection')}")  	    	       
            return  	    	       

        else:  	    	       
            new_pages = {}  	    	       

            # There is a random chance that a reset link is included on this page  	    	       
            make_reset_link = randint(0, 100) < self.server.reset  	    	       

            if len(self.path[1:]) == self.server.depth:  	    	       
                # if we've reached the max depth, start over by linking back to the level 1 pages  	    	       
                for name in TrackingServer.PAGES[:self.server.breadth]:  	    	       
                    new_pages['/' + name] = 0  	    	       

                if make_reset_link:  	    	       
                    new_pages['/reset'] = 0  	    	       
            else:  	    	       
                for name in TrackingServer.PAGES[:self.server.breadth]:  	    	       
                    new_pages[self.path + name] = 0  	    	       

                if make_reset_link:  	    	       
                    if self.path != '/':  	    	       
                        new_pages[self.path + '/reset'] = 0  	    	       
                    else:  	    	       
                        new_pages['/reset'] = 0  	    	       

            # dict.update() would overwrite an existing page's visit count with 0  	    	       
            # when that page's URL is re-generated  	    	       
            for path in new_pages:  	    	       
                if path not in self.server.pages:  	    	       
                    self.server.pages[path] = new_pages[path]  	    	       

            self.send_response(200)  	    	       
            self.send_header('Connection', 'close')  	    	       
            self.end_headers()  	    	       
            self.wfile.write(  	    	       
                    bytes(f"""<!DOCTYPE html>  	    	       
<html lang="en">  	    	       
    <head>  	    	       
        <meta charset="utf-8">  	    	       
        <title>CS 1440 Recursive Web Crawler Testing Server v{VERSION}</title>  	    	       
    </head>  	    	       
    <body>  	    	       
        <h1>CS 1440 Recursive Web Crawler Testing Server v{VERSION}</h1>  	    	       
        {self.instructions()}  	    	       
        <h2>From here you can visit</h2>  	    	       
        <ul>  	    	       
            <li><a href="/">Return home</a></li>  	    	       
            {self.listOfAnchorsWithFragments(new_pages)}  	    	       
            {self.listOfAnchors(new_pages)}  	    	       
        </ul>  	    	       
        {self.serverInformation()}  	    	       
    </body>  	    	       
</html>""", encoding="utf_8"))  	    	       
            return  	    	       


    def do_503(self):  	    	       
        if self.server.restart:  	    	       
            message = "Try again in a moment"  	    	       
        else:  	    	       
            message = "It needs to be manually restarted"  	    	       

        self.send_response(503)  	    	       
        self.send_header('Connection', 'close')  	    	       
        self.end_headers()  	    	       
        self.wfile.write(  	    	       
                bytes(f"""<!DOCTYPE html>  	    	       
<html lang="en">  	    	       
    <head>  	    	       
        <meta charset="utf-8">  	    	       
        <title>503 Service Unavailable</title>  	    	       
    </head>  	    	       
    <body>  	    	       
        <h1>503 Service Unavailable</h1>  	    	       
        <p>The server is down now. {message}.</p>  	    	       
    </body>  	    	       
</html>""", encoding="utf_8"))  	    	       


    def do_404(self):  	    	       
        """  	    	       
        Called when a non-existant page is requested.  	    	       

        Browsers will ask for a favicon automatically; ignore such requests  	    	       
        """  	    	       
        if self.path != '/favicon.ico':  	    	       
            # Visiting a page before it exists implicitly  	    	       
            # adds it to the table of visited pages  	    	       
            self.server.pages[self.path] = 1  	    	       

            # This special event is also reported separately  	    	       
            self.server.non_existant[self.path] = 1  	    	       

        self.send_response(404)  	    	       
        self.send_header('Connection', 'close')  	    	       
        self.end_headers()  	    	       
        self.wfile.write(bytes(f"""<!DOCTYPE html>  	    	       
<html lang="en">  	    	       
    <head>  	    	       
        <meta charset="utf-8">  	    	       
        <title>404, Dude!</title>  	    	       
    </head>  	    	       
    <body>  	    	       
        <h1>Error 404!</h1>  	    	       
        <h2>Sorry dude, wrong file!</h2>  	    	       
        <p>You tried to visit <code>{self.path}</code>, but that's not a place I can take you</p>  	    	       
    </body>  	    	       
</html>""", encoding="utf_8"))  	    	       


    def initialize(self):  	    	       
        options = self.path[1:].split('/')  	    	       
        for option in options:  	    	       
            if option == '':  	    	       
                continue  	    	       
            kv = option.split('=', maxsplit=1)  	    	       
            if len(kv) != 2:  	    	       
                print(red(f"Server: ignoring invalid option '{option}'"))  	    	       
                continue  	    	       

            # /restart=boolean/  	    	       
            if kv[0].lower() == 'restart':  	    	       
                restart = kv[1].lower()  	    	       
                if restart == 'true':  	    	       
                    self.server.restart = True  	    	       
                    print(green(f"Server: Setting restart to {self.server.restart}"))  	    	       
                elif restart == 'false':  	    	       
                    self.server.restart = False  	    	       
                    print(green(f"Server: Setting restart to {self.server.restart}"))  	    	       
                else:  	    	       
                    print(red(f"Server: ignoring invalid restart value '{kv[1]}' (can be True or False)"))  	    	       

            # /timer=int<0-N>/  	    	       
            elif kv[0].lower() == 'timer':  	    	       
                if kv[1].isdigit():  	    	       
                    self.server.timer = int(kv[1])  	    	       
                    if self.server.timer == 0:  	    	       
                        print(green(f"Server: Disabling auto-shutdown timer"))  	    	       
                    else:  	    	       
                        print(green(f"Server: Setting timer to {self.server.timer} seconds"))  	    	       
                else:  	    	       
                    print(red(f"Server: ignoring invalid timer value '{kv[1]}' (range is [0..infinity])"))  	    	       

            # /depth=int<0-N>/  	    	       
            elif kv[0].lower() == 'depth':  	    	       
                if kv[1].isdigit():  	    	       
                    self.server.depth = int(kv[1])  	    	       
                    print(green(f"Server: Setting depth to {self.server.depth}"))  	    	       
                else:  	    	       
                    print(red(f"Server: ignoring invalid depth value '{kv[1]}' (range is [1..infinity])"))  	    	       

            # /breadth=int<1-len(TrackingServer.PAGES)>/  	    	       
            elif kv[0].lower() == 'breadth':  	    	       
                if kv[1].isdigit() and 1 <= int(kv[1]) <= len(TrackingServer.PAGES):  	    	       
                    self.server.breadth = int(kv[1])  	    	       
                    print(green(f"Server: Setting breadth to {self.server.breadth}"))  	    	       
                else:  	    	       
                    print(red(f"Server: ignoring invalid breadth value '{kv[1]}' (range is [1..{len(TrackingServer.PAGES)}])"))  	    	       

            # /fragments=boolean/  	    	       
            elif kv[0].lower() == 'fragments':  	    	       
                fragments = kv[1].lower()  	    	       
                if fragments == 'true':  	    	       
                    self.server.fragments = True  	    	       
                    print(green(f"Server: Setting fragments to {self.server.fragments}"))  	    	       
                elif fragments == 'false':  	    	       
                    self.server.fragments = False  	    	       
                    print(green(f"Server: Setting fragments to {self.server.fragments}"))  	    	       
                else:  	    	       
                    print(red(f"Server: ignoring invalid fragments value '{kv[1]}' (can be True or False)"))  	    	       

            # /verbose=boolean/  	    	       
            elif kv[0].lower() == 'verbose':  	    	       
                verbose = kv[1].lower()  	    	       
                if verbose == 'true':  	    	       
                    self.server.verbose = True  	    	       
                    print(green(f"Server: Setting verbose to {self.server.verbose}"))  	    	       
                elif verbose == 'false':  	    	       
                    self.server.verbose = False  	    	       
                    print(green(f"Server: Setting verbose to {self.server.verbose}"))  	    	       
                else:  	    	       
                    print(red(f"Server: ignoring invalid verbose value '{kv[1]}' (can be True or False)"))  	    	       

            # /landmines=boolean/  	    	       
            elif kv[0].lower() == 'landmines':  	    	       
                landmines = kv[1].lower()  	    	       
                if landmines == 'true':  	    	       
                    self.server.landmines = True  	    	       
                    print(green(f"Server: Setting landmines to {self.server.landmines}"))  	    	       
                elif landmines == 'false':  	    	       
                    self.server.landmines = False  	    	       
                    print(green(f"Server: Setting landmines to {self.server.landmines}"))  	    	       
                else:  	    	       
                    print(red(f"Server: ignoring invalid landmines value '{kv[1]}' (can be True or False)"))  	    	       

            # /reset=int<0-100>/  	    	       
            elif kv[0].lower() == 'reset':  	    	       
                if kv[1].isdigit() and 0 <= int(kv[1]) <= 100:  	    	       
                    self.server.reset = int(kv[1])  	    	       
                    print(green(f"Server: Setting reset% to {self.server.reset}"))  	    	       
                else:  	    	       
                    print(red(f"Server: ignoring invalid reset% value '{kv[1]}' (range is [1..100])"))  	    	       

            # /deadend=boolean/  	    	       
            elif kv[0].lower() == 'deadend':  	    	       
                deadend = kv[1].lower()  	    	       
                if deadend == 'true':  	    	       
                    self.server.deadend = True  	    	       
                    print(green(f"Server: Setting deadend to {self.server.deadend}"))  	    	       
                elif deadend == 'false':  	    	       
                    self.server.deadend = False  	    	       
                    print(green(f"Server: Setting deadend to {self.server.deadend}"))  	    	       
                else:  	    	       
                    print(red(f"Server: ignoring invalid deadend value '{kv[1]}' (can be True or False)"))  	    	       

        # If the timer is set to non-zero, start a shutdown thread  	    	       
        if self.server.timer >= 1:  	    	       
            threading.Thread(target=self.server.shutdown_timer).start()  	    	       

        self.server.pages = {'/': 0}  	    	       
        if self.server.deadend:  	    	       
            self.server.pages['/deadend'] = 0  	    	       
        self.server.non_existant = {}  	    	       
        self.send_response(302)  	    	       
        self.send_header('Connection', 'close')  	    	       
        self.send_header('Location', '/')  	    	       
        self.end_headers()  	    	       


    def do_GET(self):  	    	       
        """  	    	       
        Called when the server receives an HTTP GET request  	    	       
        """  	    	       

        if self.path == '/shutdown':  	    	       
            print(cyan("Shutting down immediately..."))  	    	       
            self.server.timer = 0  	    	       
            self.server.restart = False  	    	       
            self.do_503()  	    	       
            threading.Thread(target=self.server.shutdown).start()  	    	       
        elif self.path == '/restart':  	    	       
            print(cyan("Restarting immediately..."))  	    	       
            self.server.timer = 0  	    	       
            self.server.restart = True  	    	       
            self.do_503()  	    	       
            threading.Thread(target=self.server.shutdown).start()  	    	       
        elif self.server.pages is None:  	    	       
            self.initialize()  	    	       
        elif self.path in self.server.pages:  	    	       
            self.respond()  	    	       
        else:  	    	       
            self.do_404()  	    	       


if __name__ == '__main__':  	    	       
    host, port = 'localhost', 8000  	    	       

    for arg in sys.argv[1:]:  	    	       
        if 'help' in arg or '-h' == arg:  	    	       
            usage()  	    	       

    if '-host' in sys.argv:  	    	       
        p = sys.argv.index('-host') + 1  	    	       
        if p < len(sys.argv) and sys.argv[p] != '':  	    	       
            host = sys.argv[p]  	    	       
        else:  	    	       
            usage()  	    	       

    if '-port' in sys.argv:  	    	       
        p = sys.argv.index('-port') + 1  	    	       
        if p < len(sys.argv) and sys.argv[p].isdigit():  	    	       
            port = int(sys.argv[p])  	    	       
        else:  	    	       
            usage()  	    	       

    keep_going = True  	    	       
    while keep_going:  	    	       
        server = TrackingServer((host, port), TrackingHandler)  	    	       
        try:  	    	       
            server.serve_forever()  	    	       
        except KeyboardInterrupt:  	    	       
            print('\nReceived KeyboardInterrupt')  	    	       
            server.timer = 0  	    	       
            server.shutdown()  	    	       
            keep_going = False  	    	       
        finally:  	    	       
            server.report()  	    	       
            server.server_close()  	    	       
            keep_going = keep_going and server.restart  	    	       

        if keep_going:  	    	       
            print(cyan("\nRestarting...\n\n"))  	    	       
            time.sleep(1)  	    	       
