import sys

def fractalParser(fracFile):

    fractalDictionary = {}


    oFrac = open("data/"+fracFile)

    for line in oFrac:

       rLine = line.replace("\n", "")
       if rLine == "":
           continue
       elif rLine[0] == "#":
           continue
       else:
           aLine = rLine.split(": ")
           fractalDictionary[aLine[0]] = aLine[1]
    oFrac.close()
    return fractalDictionary

# def main():
#     x = FractalParser()
#     print(x)
#
# main()