import math
x="yes"
while x in ("yes", "Yes", "YES","YES!","yup","sure","maybe","ok","k","confirmed"):
    print("Type the object's mass you wish to launch in Kg (Just the number)")
    ObjectMass=eval(input("Object mass:"))
    print("Please type the elastic constant of the sling in newtons per meter (just include the number)")
    ElasticConstant=eval(input("Elasticity Constant:"))
    print("Please type the force of the gravity acting on the object in meters per second squared (just include the number)")
    Gravity=eval(input("Force of gravity:"))
    print("Please type the distance from the target in meters (just include the number)")
    Distance=eval(input("Meters:"))
    print("Finally please type the angle of trajectory in degrees (we are assuming the apparatus is on ground level)")
    Angle=((eval(input("Degrees:")))*6.28319/360)
    Equation = math.sqrt((ObjectMass*Gravity*Distance)/(ElasticConstant*math.sin(2*Angle)))
    print("Draw length needed for launch is",round(Equation,5),"Meters")
    print()
    x=input("Do you wish to calculate again?\n")
else : print("\nGood bye then!")