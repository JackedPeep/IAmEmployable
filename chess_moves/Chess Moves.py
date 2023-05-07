# K. Brady Christianson (A02347230)
# CS1400 2022 04 14
import random


# the chess piece super class
class ChessPiece:
    def __init__(self, color, x, y):
        self.__color = color
        self.__x = x
        self.__y = y

    def color(self):
        return self.__color

    def location(self):
        return (self.__x, self.__y)

    def x(self):
        return self.__x

    def y(self):
        return self.__y


# TODO: write all your code below this line

class Pawn(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def pic(self):
        if self.color() == "w":
            return "\u2659"
        else:
            return "\u265F"

    def validMove(self, x, y):
        xdiff = abs(self.x() - x)
        ydiff = self.y() - y

        if self.color()=="w":
            if ydiff == 1 and xdiff == 0:
                return True
        else:
            if ydiff ==-1 and xdiff==0:
                return True

class Rook(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def pic(self):
        if self.color() == "w":
            return "\u2656"
        else:
            return "\u265C"

    def validMove(self, x, y):
        xdiff = abs(self.x() - x)
        ydiff = abs(self.y() - y)
        if abs(xdiff) == 0 or abs(ydiff) == 0:
             if abs(xdiff) == 1 or abs(ydiff) == 1:
                 return True

class Knight(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def pic(self):
        if self.color() == "w":
            return "\u2658"
        else:
            return "\u265E"

    def validMove(self, x, y):
        xdiff = abs(self.x() - x)
        ydiff = abs(self.y() - y)
        if abs(xdiff - ydiff) == 1:
            if abs(xdiff) == 2 and abs(ydiff) == 1 or abs(ydiff) == 2 and abs(xdiff) == 1:
                return True

class Queen(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def pic(self):
        if self.color() == "w":
            return "\u2655"
        else:
            return "\u265B"

    def validMove(self, x, y):
        xdiff = abs(self.x() - x)
        ydiff = abs(self.y() - y)
        if abs(xdiff - ydiff) == 0 or abs(xdiff) ==0 or abs(ydiff) == 0:
            return True

class King(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def pic(self):
        if self.color() == "w":
            return "\u2654"
        else:
            return "\u265A"

    def validMove(self, x, y):
        xdiff = abs(self.x() - x)
        ydiff = abs(self.y() - y)
        if xdiff < 2 and ydiff < 2:
            return True

class Bishop(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color,x,y)

    def pic(self):
        if self.color()=="w":
            return "\u2657"
        else: return "\u265d"

    def validMove(self,x,y):
        xdiff=abs(self.x()-x)
        ydiff=abs(self.y()-y)
        if abs(xdiff-ydiff)==0:
            return True





# TODO: write all your code above this line
# print a nice picture of the valid moves
# white pawns only move "up" one space
# black pawns only move "down" one space
# other chess pieces move normally




def printValidMoves(cp):
    print("\t  ", cp.pic(), "at", cp.location())
    for i in range(7, -1, -1):
        print("\t" + str(i) + " ", end="")
        for j in range(0, 8):
            if cp.x() == j and cp.y() == i:
                print(cp.pic() + " ", end="")
            elif cp.validMove(j, i):
                print("* ", end="")
            else:
                print(". ", end="")
        print()
    print("\t  ", end="")
    for i in range(0, 8):
        print(str(i) + " ", end="")
    print()
    print()


# returns a random chess piece at a random location
# each of these types must inherit from ChessPiece
def randomChessPiece():
    if random.randint(0, 1) == 0:
        c = "w"
    else:
        c = "b"
    t = random.randint(1, 6)
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    if t == 1: return Pawn(c, x, y)
    if t == 2: return Queen(c, x, y)
    if t == 3: return King(c, x, y)
    if t == 4: return Rook(c, x, y)
    if t == 5:
        return Knight(c, x, y)
    else:
        return Bishop(c, x, y)


def main():
    clist = []
    # make a list of random chess pieces
    for i in range(0, 10):
        clist.append(randomChessPiece())
    # display their valid moves
    for i in range(0, len(clist)):
        # behold! polymorphism works!
        printValidMoves(clist[i])


main()