
import random
import time

die = 0
potentialScore = 0
actualScore = 0
devilPotentialScore = 0
devilActualScore = 0
devilsTurn=False
role = False
Input = False

def uDie(die):

    # die - Integer valued 1-6.  The rolled die value.

    if die==1: return "\u2620"
    if die==2: return "\u2681"
    if die==3: return "\u2682"
    if die==4: return "\u2683"
    if die==5: return "\u2684"
    if die==6: return "\u2685"

def printSimpleBoard(die,myPts,devilPts,myTurn,myRndPts,devilRndPts):

    # die - Integer valued 1-6.  The rolled die value.
    # myPts - Integer valued 0-100. The current saved score of the human player.
    # devilPts - Integer valued 0-100. The current saved score of the devil.
    # myTurn - Boolean value.  True if it is the human player's turn.
    # myRndPts - Integer valued 0-100.  The human's saved score plus points gained that round.
    # devilRndPts - Integer valued 0-100.  The devil's saved score plus points gained that round.

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("my\tthis\tdevil's\tthis")
    print("score\tround\tscore\tround")
    print("  ",myPts,"\t  ",myRndPts,"\t  ",devilPts,"\t  ",devilRndPts)
    print("\t     die")
    print("\t     ",uDie(die),"\n")

def devilsDice(die,potentialScore,actualScore,devilPotentialScore,devilActualScore,Input):
    die = 0
    potentialScore = 0
    actualScore = 0
    devilPotentialScore = 0
    devilActualScore = 0
    Input = False

    while (actualScore + potentialScore) < 100 and (devilActualScore + devilPotentialScore) < 100 and Input != "q":
        Input = input("It is your turn. Roll or Pass? [r/p/q]\n")
        if Input == "r" or "p":

            while Input == "r" and (actualScore + potentialScore) < 100:

                die = random.randint(1, 6)
                if die == 1: #lose points and pass turn
                    potentialScore=0
                    actualScore = actualScore + potentialScore
                    printSimpleBoard(die, actualScore, devilActualScore, True, potentialScore, devilPotentialScore)
                    uDie(die)
                    print("Oops you rolled a " + str(die) + "...")
                    Input = "p"
                else: #gain potential points and reset the role/pass option.
                    potentialScore = potentialScore + die
                    printSimpleBoard(die, actualScore, devilActualScore, True, potentialScore, devilPotentialScore)
                    uDie(die)
                    print("You rolled a " + str(die) + "!")
                    Input = input("It is still your turn. Roll or Pass? [r/p/q]\n")

            else: #Devil goes
                if Input == "p" or (actualScore + potentialScore) >= 100:
                    actualScore = actualScore + potentialScore
                    potentialScore = 0
                    print(" ")
                    time.sleep(.75)
                    Input = "r"
                    while Input == "r" and (devilActualScore + devilPotentialScore)<100 and (actualScore + potentialScore) < 100:
                        die = random.randint(1, 6)
                        if die == 1:  # lose points and pass turn
                            time.sleep(.75)
                            devilPotentialScore = 0
                            printSimpleBoard(die,actualScore,devilActualScore,True,potentialScore,devilPotentialScore)
                            uDie(die)
                            print("HA the devil rolled a " + str(die) + "!")
                            Input = "p"
                        elif devilActualScore < actualScore:  # gain potential points and reset the role/pass option.
                            time.sleep(.75)
                            print("The devil rolled a " + str(die) + ".")
                            devilPotentialScore = devilPotentialScore + die
                            printSimpleBoard(die, actualScore, devilActualScore, True, potentialScore, devilPotentialScore)
                            uDie(die)
                            if devilPotentialScore >= 30:
                                Input = "p"
                                devilActualScore += devilPotentialScore
                                devilPotentialScore=0

                        else:
                            time.sleep(.75)
                            devilPotentialScore = devilPotentialScore + die
                            printSimpleBoard(die, actualScore, devilActualScore, True, potentialScore, devilPotentialScore)
                            uDie(die)
                            print("The devil rolled a " + str(die) + ".")
                            if devilPotentialScore >= 21:
                                Input = "p"
                                devilActualScore += devilPotentialScore
                                devilPotentialScore=0

             # Devil goes

            print(" ")
            time.sleep(1)
    else:
        if Input == "q":
            print("You decided not to play against the devil.\nSome might say that was a wise decision.")
        elif (devilActualScore+devilPotentialScore) >= 100:
            print("The Devil got 100 points, looks like your gonna have a bad day...")
        elif (actualScore + potentialScore) >= 100:
            print("You won with 100 points!")
            print("The Devil said he lost the golden fiddle he was going to give you.\nSo he decides to give you some golden dice instead.")


devilsDice(die,potentialScore,actualScore,devilPotentialScore,devilActualScore,Input)





