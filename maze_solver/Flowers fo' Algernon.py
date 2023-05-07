import time
import sys

SLEEPTIME = 0.1
FILENAME = "maze.txt"
VERBOSE = False



# TODO: write all your code below this line
#K. Brady Christianson A02347230 CS1400

def solve(maze,row,col):


 #len(maze) returns num of rows, len(maze[row]) returns num of columns




    #falure conditions
    if row < 0: return False
    if col < 0: return False
    if row >= len(maze): return False
    if col >= len(maze[0]): return False

    #success condition (completion of maze)
    if maze[row][col] in ('X', '.'):
        return False
    if  row != 1 and  col != 0:
        if row in (len(maze)-1,0):
            return True
        if col in (len(maze[row])-1,0):
            return True

    #Rat movements


    maze[row][col] = '.'
    printMaze(maze)


    if solve(maze, row + 1, col): return True
    if solve(maze, row, col + 1): return True
    if solve(maze, row, col - 1): return True
    if solve(maze, row - 1, col): return True

    maze[row][col]=' '
    printMaze(maze)
    return False


# put the line "if VERBOSE: printMaze(maze)"
# every time you drop/retrieve a marker
#
# TODO: write all your code above this line
def readMaze(maze):
    mazefile = open(FILENAME, "r")
    for line in mazefile.read().splitlines():
        maze.append([])
        for c in line:
            maze[-1].append(c)
    mazefile.close()


def printMaze(maze):
    print("\n\n\n\n\n\n\n\n\n")
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            print(maze[i][j], end="")
        print()
    time.sleep(SLEEPTIME)
    print()


def main():
    maze = []
    readMaze(maze)
    if not solve(maze, 1, 0):
         print("no solution is possible.")
    else:
        printMaze(maze)


main()