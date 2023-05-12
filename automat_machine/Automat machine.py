
class Artomat: #class variables defined.
    def __init__(self,money=0,hopper=0,bin1=10,bin2=10,bin3=10,bin4=10,text1=(),text2=(),text3=(),text4=()):
        self.money = money
        self.hopper = hopper
        self.bin1 = bin1
        self.bin2 = bin2
        self.bin3 = bin3
        self.bin4 = bin4
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.text4 = text4


    def printStatus(self):   #prints the contents including number of quarters in the happer and machine.
        print("\n1: "+str(self.bin1)+" packs of "+self.text1+"."+"\n2: "+str(self.bin2)+" packs of "+self.text2+"."+"\n3: "+str(self.bin3)+" packs of "+self.text3+"."+"\n4: "+str(self.bin4)+" packs of "+self.text4+".")               #print money, hopper, and bin values
        print("There is $ "+"{:.2f}".format(self.hopper*.25)+" in the hopper.\nThere is $ "+"{:.2f}".format(self.money*.25)+" in the machine.\n")
    def dropQuarter(self): #add quarter to hopper
        print("chang")                    #print message
        self.hopper+=1                                #update hopper

    def pullKnob(self,k): #add quarters to the machine and dispense art if prerequisites are met.
        if self.hopper < 3:
            print("(nothing happens)")
        else:
            self.money += self.hopper
            self.hopper = 0

            if k == 1 and self.bin1 != 0:  #dispences art pieces in correspondence to knob pulled
                print("A pack of " + str(self.text1) + " slides into view.")
                self.bin1 -= 1
            elif k == 2 and self.bin2 != 0:
                print("A pack of " + str(self.text2) + " slides into view.")
                self.bin2 -= 1
            elif k == 3 and self.bin3 != 0:
                print("A pack of " + str(self.text3) + " slides into view.")
                self.bin3 -= 1
            elif k == 4 and self.bin4 != 0:
                print("A pack of " + str(self.text4) + " slides into view.")
                self.bin4 -= 1
            else:
                print("The machine eats your quarters.")


    def restock(self): #refills the art in the machine.
        print("A grouchy-looking attendant shows up, opens the back, fiddles around a bit, closes it, and leaves.")
        self.bin1 = 10
        self.bin2 = 10
        self.bin3 = 10
        self.bin4 = 10

def main():
    photoMachine = Artomat(text1="Adams",text2="Arbus",text3="Dali",text4="Lange")
    portraitMachine = Artomat(money=212,hopper=2,bin1=1,bin2=0,bin3=8,bin4=10,text1="Picasso",text2="Rembrandt",text3="Van Gogh",text4="Monet")

    photoMachine.printStatus()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(1)
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.printStatus()
    photoMachine.restock()
    photoMachine.printStatus()
    print("----")
    portraitMachine.printStatus()
    portraitMachine.dropQuarter()
    portraitMachine.pullKnob(1)
    portraitMachine.printStatus()


main()







##Out put should look like this!!!!vvvv

#1: 10 packs of Adams
#2: 10 packs of Arbus
#3: 10 packs of Dali
#4: 10 packs of Lange
#There is $ 0.00 in the machine.
#There is $ 0.00 in the hopper.

#ching
#ching
#ching
#A pack of Adams slides into view.
#(nothing happens)
#ching
#(nothing happens)
#ching
#ching
#ching
#A pack of Arbus slides into view.

#1: 9 packs of Adams
#2: 9 packs of Arbus
#3: 10 packs of Dali
#4: 10 packs of Lange
#There is $ 1.75 in the machine.
#There is $ 0.00 in the hopper.

#A grouchy-looking attendent shows up, opens the back, fiddles around a bit, closes it, and leaves.

#1: 10 packs of Adams
#2: 10 packs of Arbus
#3: 10 packs of Dali
#4: 10 packs of Lange
#There is $ 0.00 in the machine.
#There is $ 0.00 in the hopper.

#----

#1: 1 packs of Picasso
#2: 0 packs of Rembrandt
#3: 8 packs of Van Gogh
#4: 10 packs of Monet
#There is $ 53.00 in the machine.
#There is $ 0.50 in the hopper.

#ching
#A pack of Picasso slides into view.

#1: 0 packs of Picasso
#2: 0 packs of Rembrandt
#3: 8 packs of Van Gogh
#4: 10 packs of Monet
#There is $ 53.75 in the machine.
#There is $ 0.00 in the hopper.
