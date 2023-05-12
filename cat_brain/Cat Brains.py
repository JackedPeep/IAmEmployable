#The cat's brain
#The food
y = "yes"
x = "yes"
def catbrain(x,y):

    while y =='yes':
        x = input("Is it food? [yes/no]\n")
        if x == 'yes':
            x = input("From a can? [yes/no]\n")
            if x == 'yes':
                print()
                print("Eat half.\n")
            elif x == 'no':
                print()
                print("Ignore it.")
        #The cat tree leads to...
        elif x == 'no':
            print()
            x = input("Is it a cat tree? [yes/no]\n")
            if x == 'yes':
                print()
                x = input("Did it come in a box? [yes/no]\n")
                if x == 'yes':
                    print()
                    print("Sit in the box.\n")
                elif x == 'no':
                    print()
                    print("Ignore it.\n")
        #The human that leads to...
            elif x == 'no':
                print()
                x = input("Is it human? [yes/no]\n")
                if x == 'yes':
                    print()
                    x = input("Does it want to pet me? [yes/no]\n")
                    if x == 'yes':
                        print()
                        print("Cough up a hair ball!\n")
                    elif x == 'no':
                        print()
                        print("Jumps in it's lap.\n")
        #The laptop that leads to...
                elif x == 'no':
                    print()
                    x = input("Is it a laptop? [yes/no]\n")
                    if x == 'yes':
                        print()
                        x = input("Is it in use? [yes/no]\n")
                        if x == 'yes':
                            print()
                            print("Lay on key board.\n")
                        elif x == 'no':
                            print()
                            print("Knock it off table.\n")
        #Bed time.
                    elif x == 'no':
                        print()
                        print("Zzzz...")

catbrain(x,y)