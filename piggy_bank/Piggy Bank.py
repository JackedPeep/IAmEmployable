
class PiggyBank:
    def __init__(self,balance=0,broken=False):

        self.__balance = balance
        self.__broken = broken


    def broken(self): #return the bool of the private variable broken.
        return self.__broken

    def deposit(self,money):       # allows user to input an amount
        if self.__broken == False:  # to deposit into balance of the piggy bank.
            self.__balance += money


    def showMeTheMoney(self): #return the numeric of the private variable balance.
        return self.__balance

    def smash(self): #Breaks the bank.
        self.__broken=True
        self.__balance=0

def printStatus(x,piggyBank): #prints the status of the PiggyBank.
    if piggyBank.broken() == False:
        print(str(x),"has $%0.2f"%piggyBank.showMeTheMoney(), "and is not broken.")
    else:
        print(str(x),"has $%0.2f"%piggyBank.showMeTheMoney(), "and is broken.")

def main():
    p1 = PiggyBank()
    p2 = PiggyBank()
    p1.showMeTheMoney()
    printStatus("p1",p1)
    p1.deposit(1.25)
    printStatus("p1",p1)
    p1.deposit(6.55)
    printStatus("p1",p1)
    p1.smash()
    printStatus("p1",p1)
    p1.deposit(2.15)
    printStatus("p1",p1)
    p1.__balance=100.0
    p1.__broken=False
    printStatus("p1",p1)

main()
#p1 has $ 0.00 and is not broken.
#p1 has $ 1.25 and is not broken.
#p1 has $ 7.80 and is not broken.
#p1 has $ 0.00 and is broken.
#p1 has $ 0.00 and is broken.
#p1 has $ 0.00 and is broken.