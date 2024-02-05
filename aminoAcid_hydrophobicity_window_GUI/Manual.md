# Recursive Web Crawler User Manual

Items needed:

* Python3

run for program requirements: 
```bash
 python -m pip install --user -r requirements.txt
```


Run demo: 
```bash

USERNAME@COMPUTER:~/cs1440-christianson-brady-assn6$ python3 crawler.py [pointer URL] [Depth]

```
IMPORTANT: Int the pointer URL variable the program only takes an absolute URL. You may copy and paste this from the top of the website you wish to point at.
The Depth argument is optional and will default to 3 if not included. Just running crawler.py will show an error message describing what inputs are needed.


Web crawler should run to the depth you assigned starting at the pointer URL, and it should return the URLs visited and any errors the crawler encounters.
