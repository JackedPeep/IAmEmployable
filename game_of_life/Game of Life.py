# 20210405 K. Brady Christianson CS1400
# 22 by 22 only look at 21 by 21 grid
# 2 arrays. First is current generation. Second is next generation.
# Calculate next generation using these rules.
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
import random
import time

class Cell:
    def __init__(self):
        self.cell = 'dead'

    def killCell(self):  # sets cell to 'dead'
        self.cell = 'dead'

    def reviveCell(self):
        self.cell = 'alive'

    def isAlive(self):
        if self.cell == 'alive':
            return True
        else:
            return False

    def cellPicture(self):
        if self.cell == 'alive':
            return "X"
        else:
            return " "


class Board:
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.board = [[Cell() for lengthBros in range(self.length)] for heightBros in range(self.height)]  # Matrix example from
        self.creatBoard()

    def printBoard(self):
        print("\n\n\n\n\n\n\n\n\n         Game of life!")
        for height in self.board:
            for length in height:
                print(length.cellPicture(), end=" ")
            print()

    def creatBoard(self):
        for height in self.board:
            for width in height:
                percentChance = random.randint(0, 2)
                if percentChance == 1:
                    width.reviveCell()

    def broCheck(self, lengthCheck, heightCheck):
        bros = []
        for length in range(-1, 2):
            for height in range(-1, 2):
                broLength = lengthCheck + length
                broHeight = heightCheck + height
                trueBros = True
                if broLength == lengthCheck and broHeight == heightCheck:
                    trueBros = False
                if broLength < 0 or broLength >= self.length:
                    trueBros = False
                if broHeight < 0 or broHeight >= self.height:
                    trueBros = False
                if trueBros:
                    bros.append(self.board[broLength][broHeight])



        return bros

    def boardTime(self):
        birth = []
        exicution = []

        for height in range(len(self.board)):
            for length in range(len(self.board[height])):
                broCheck = self.broCheck(height, length)
                livingBros = []

                for broCount in broCheck:
                    if broCount.isAlive():
                        livingBros.append(broCount)
                broObject=self.board[height][length]
                mainBroStatus = broObject.isAlive()

                if mainBroStatus == True:
                    if len(livingBros)< 2 or len(livingBros)>3:
                        exicution.append(broObject)
                    if len(livingBros) == 3 or len(livingBros)==2:
                        birth.append(broObject)
                else:
                    if len(livingBros)==3:
                        birth.append(broObject)
        for broItems in birth:
            broItems.reviveCell()
        for broItems in exicution:
            broItems.killCell()



def main():
    gameOlife= Board(22,22)
    g=0
    while g < 50:
        gameOlife.printBoard()
        gameOlife.boardTime()
        time.sleep(.3)
        g+=1
        print("           Generation =",str(g))



main()





