# Disclamer lines 2-5 and lines 25-30 are copy
# and pasted from MY previous work if proof is required I
#have it.
import turtle
TheTurtle = turtle.Turtle()
TheTurtle.speed(50)
TheTurtle.shape("arrow")
#-base square for the sign is created-

#quardinets and starting color/pensize set
TheTurtle.penup()
TheTurtle.setpos(0,200)
TheTurtle.color("yellow")
TheTurtle.pensize(12)
TheTurtle.pendown()

#Loop variables defined for square loop
loopnumber=0
loopreset=0
Ymax=200
Ymin=-20
Xmax=300
Xmin=-300



while loopnumber <= 20:
    TheTurtle.setpos(loopreset,Ymax)
    TheTurtle.setpos(Xmax,Ymax)
    TheTurtle.setpos(Xmax,Ymin)
    TheTurtle.setpos(Xmin,Ymin)
    TheTurtle.setpos(Xmin,Ymax)
    TheTurtle.setpos(loopreset,Ymax)
    loopnumber=loopnumber+1
    Ymax=Ymax-10
    Ymin=Ymin+10
    Xmax=Xmax-10
    Xmin=Xmin+10

#-The border is created-
TheTurtle.penup()
TheTurtle.color("black")
TheTurtle.setpos(0,190)
TheTurtle.pensize(7)
TheTurtle.pendown()

TheTurtle.setpos(290,190)
TheTurtle.setpos(290,-10)
TheTurtle.setpos(-290,-10)
TheTurtle.setpos(-290,190)
TheTurtle.setpos(0,190)
TheTurtle.hideturtle()
#-The two way arrow is created-

#Right arrow
TheTurtle.penup()
TheTurtle.setpos(120,180)
TheTurtle.pendown()


triangleside =180


TheTurtle.begin_fill()
TheTurtle.setheading(330)
TheTurtle.forward(triangleside)
TheTurtle.setheading(210)
TheTurtle.forward(triangleside)
TheTurtle.setheading(90)
TheTurtle.forward(triangleside)
TheTurtle.end_fill()
#Left arrow
TheTurtle.penup()
TheTurtle.setpos(-120,180)
TheTurtle.pendown()

TheTurtle.begin_fill()
TheTurtle.setheading(210)
TheTurtle.forward(triangleside)
TheTurtle.setheading(330)
TheTurtle.forward(triangleside)
TheTurtle.setheading(90)
TheTurtle.forward(triangleside)
TheTurtle.end_fill()

#Conecting the arrows
TheTurtle.penup()
TheTurtle.setpos(-130,135)
TheTurtle.pendown()

TheTurtle.begin_fill()
TheTurtle.setpos(130,135)
TheTurtle.setpos(130,45)
TheTurtle.setpos(-130,45)
TheTurtle.setpos(-130,135)
TheTurtle.end_fill()



turtle.done()