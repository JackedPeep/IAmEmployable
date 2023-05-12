 # Zee Rules:

 # 1. The generator can be engaged once the engine is
 # up to speed.

 # 2. If the generator is engaged before the engine is
 # up to speed (or, if the engine loses speed when the
 # generator is engaged) the engine dies, and the
 # generator disengages automatically.

 # 3. A successfully engaged generator generates
 # electricity.

 # 4. The breakers can be engaged once electricity is
 # being generated.

 # 5. If the breakers are engaged before the
 # generator is generating electricity (or, if the
 # generator stops producing electricity) the breakers
 # disengage automatically.

 # 6. If the breakers are engaged, the lights come on.

 # 7. If the breakers disengage, the lights go off.")

 # engine state variables
oilLevel = 0
fuelLevel = 0
fuelCutOff = True
throttleAdvance = False
engineRunning = 1     # 1=NOT RUNNING 2=IDLE 3=RUNNING AT SPEED
choke = False
lightsOn = False
printStatus = True
printMenu = True
done = False
breakerOn = False
generatorEngaged = False
# main event loop
while not done:
    if printStatus:
        # print the status
        print("\n")
        print(format("Oil Level:",">33s"),end="  ")
        print(oilLevel,end="")
        if(oilLevel==3): print(" >>FULL<<")
        elif(oilLevel==1): print(" >>LOW<<")
        elif(oilLevel==0): print(" >>EMPTY<<")
        else:print()
    
        print(format("Fuel Level:",">33s"),end="  ")
        print(fuelLevel,end="")
        if(fuelLevel==5): print(" >>FULL<<")
        elif(fuelLevel==1): print(" >>LOW<<")
        elif(fuelLevel==0): print(" >>EMPTY<<")
        else:print()
    
        print(format("Throttle:",">33s"),end="  ")
        if(throttleAdvance): print("advanced")
        else: print("not advanced")
    
        print(format("Choke:",">33s"),end="  ")
        if(choke): print("engaged")
        else: print("not engaged")
    
        print(format("Fuel Cutoff:",">33s"),end="  ")
        if(fuelCutOff): print("fuel off")
        else: print("fuel on")
    
        print(format("The engine is:",">33s"),end="  ")
        if(engineRunning == 1):print(">>Not Running<<")
        elif(engineRunning == 3): print(">>At Speed<<")
        elif (engineRunning == 2) :print(">>At Idle<<")

        print(format("The generator is:", ">33s"), end="  ")
        if (engineRunning==3 and breakerOn): print(">>Running<<")
        else: print(">>Not Running<<")

        print(format("The electricity is:", ">33s"), end="  ")
        if (breakerOn): print(">>Live<<")
        elif engineRunning == 2 or engineRunning == 1: print(">>Dead<<")

    
        printStatus = False
    
    if(printMenu):
        # print the menu
        print("")
        print(format("\ts - starter button","<34s"),end="    ")
        print(format("f - add diesel fuel","<34s"))
        print(format("\tt - advance/retard throttle","<34s"),end="    ")
        print(format("o - add oil","<34s"))
        print(format("\tc - choke on/off","<34s"),end="    ")
        print(format("w - wait","<34s"))
        print(format("\tv - fuel cutoff valve open/closed","<34s"),end="    ")
        print(format("q - quit", "<34s"))
        print(format("\tg - generator engaged/disengaged", "<34s"))
        print(format("\te - breaker switch on/off", "<34s"), end="    ")
        print("")
        print("")
        print(format("\tp - panel ","<34s"),end="    ")
        print(format("m - menu","<34s"))

        printMenu = False
     
    # get response
    print("")
    r = input("action: ")
    while(r!='s' and r!='t' and r!='f' and r!='c' and 
          r!='o' and r!='v' and r!='w' and r!='q' and
          r!='p' and r!='m' and r!='e' and r!='g'):
        print("PANIC!")
        r = input("action: ")

    if(r=='s'):
        print("You punch the starter button.")
        if(engineRunning==2 or engineRunning==3):
            print("You hear the starter grind into the running engine, then release.")
        else:
            if(oilLevel<1):
                print("You hear the pistons scraping in their cylinders.")
                print("The engine refuses to turn.")
            elif(fuelLevel==0):
                print("You hear the engine turning, but it won't fire up. \nTry looking at your fuel.")
            elif(fuelCutOff):
                print("You hear the engine turning, but it won't fire up. \nTry turning on fuel cut off.")
            elif(not choke):
                print("You hear the engine turning, but it won't fire up. \nTry turning on the choke.")
            elif(throttleAdvance):
                print("You hear the engine turning, but it won't fire up. \nTake a look at the throttle.")
            else:
                engineRunning = 2
                print("The engine sputters to life!")


    if(r=='t'):
        if(throttleAdvance):
            throttleAdvance = False
            print("You back off the throttle.")
            if(engineRunning==3):
                engineRunning=2
                print("The engine drops to idle.")
        else:
            print("You advance the throttle.")
            throttleAdvance = True
            if(choke and engineRunning==3):
                engineRunning = 1
                print("The engine sputters and dies.")
            elif(engineRunning==2):
                print("The engine revs up to operating speed.")
                engineRunning = 3
            elif(engineRunning == 3) and (breakerOn):
                print()
                print("The lights flicker but don't go out.")


    if(r=='f'):
        if(fuelLevel<5):
            fuelLevel+=1
            print("You pour in a gallon of diesel fuel.")
        else:
            print("The tank is already full.")

    if(r=='c'):
        if(choke):
            choke = False
            print("You disengage the engine choke.")
        else:
            choke = True
            print("You engage the engine choke.")
            if(engineRunning == 3 and throttleAdvance):
                engineRunning = 1
                print("The engine sputters and dies.")
            

    if(r=='o'):
        if(oilLevel<3):
            oilLevel+=1
            print("You put in a quart of oil.")
        else:
            print("The oil reservoir already is full.")


    if(r=='v'):
        if(fuelCutOff):
            fuelCutOff = False
            print("You set the Fuel Cutoff Valve to \"fuel on\".")

        else:
            fuelCutOff = True
            print("You set the Fuel Cutoff Valve to \"fuel off\".")
            if(engineRunning==3 or engineRunning== 2):
                engineRunning = 1
                print("After a few moments, the engine sputters and dies.")
    if(r=='w'):
        print("You sit in the console chair to monitor the gauges.")
        print("But it is pretty boring and you soon drift off to sleep.")
        print("Zzzz....")
        if(engineRunning==3 or engineRunning ==2):
            if(oilLevel>0):oilLevel-=1
            if(fuelLevel>0):fuelLevel-=1
            if(oilLevel==0 or fuelLevel==0):
                engineRunning = 1
                print("After an hour, you awake with a start!")

                if(oilLevel ==0): print("The engine screeches to a halt.")
                else: print("The engine sputters and dies.")

            else:
                print("You wake up after an hour.")
                print("Everything appears to be operating normally.")
        else:
            print("You wake up after an hour.")
            print("The engine has miraculously not started itself during your nap.")

    if (r=='g'):
        if (engineRunning==3):
            generatorEngaged=True
            print("You kick the generator.\nYou think you can hear a sweet humming complimenting the roar of the engine.")
        elif engineRunning == 2:
            engineRunning = 1
            print("You kick the generator.")
            print("")
            print("The engine dies.")
        else: print("You kick the generator...\n\nNothing happens.")

    if (r=='e'):
        if (breakerOn):
            breakerOn = False
            print("You use both your hands to pull the red breaker switch up. \nIt screeches up with a harsh pitch.\n\nYour world goes dark.")

        elif  (generatorEngaged) and breakerOn == False:
            breakerOn = True
            print("It takes a great deal of body weight to push the breaker bar down. \nIt finally gives, and falls with a satisfying \"CAACHUNK!\" \nThe lights flicker to life.")

        else: print("You try putting all of your body weight into pushing the breaker bar into the ON position, \nbut their seems to be some mecanical lock on the bar.")





    if(r=='q'): 
        print("quitting...")
        done = True

    if(r=='p'): printStatus = True

    if(r=='m'): printMenu = True

    



