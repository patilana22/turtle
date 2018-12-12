#!/usr/bin/env python
#

# @author Anand Patil
# @version December 12, 2018
# @course Programming 1
# @assign.ment Turtle stuff
# @descrip.tion Stuffing of turtles


# https://docs.python.org/2/library/turtle.html?highlight=turtle#module-turtle

# Turtle motion
#  Move and draw
#   forward() | fd()
#   backward() | bk() | back()
#   right() | rt()
#   left() | lt()
#   goto() | setpos() | setposition()
#   setx()
#   sety()
#   setheading() | seth()
#   home()
#   circle()
#   dot()
#   stamp()
#   clearstamp()
#   clearstamps()
#   undo()
#   speed()
# Tell Turtle's state
#   position() | pos()
#   towards()
#   xcor()
#   ycor()
#   heading()
#   distance()
# Setting and measurement
#   degrees()
#   radians()
# Pen control
#  Drawing state
#   pendown() | pd() | down()
#   penup() | pu() | up()
#   pensize() | width()
#   pen()
#   isdown()
# Color control
#   color()
#   pencolor()
#   fillcolor()
# Filling
#   fill()
#   begin_fill()
#   end_fill()
# More drawing control
#   reset()
#   clear()
#   write()
# Turtle state
#  Visibility
#   showturtle() | st()
#   hideturtle() | ht()
#   isvisible()
#  Appearance
#   shape()
#   resizemode()
#   shapesize() | turtlesize()
#   settiltangle()
#   tiltangle()
#   tilt()
# Using events
#   onclick()
#   onrelease()
#   ondrag()
#   mainloop() | done()
# Special Turtle methods
#   begin_poly()
#   end_poly()
#   get_poly()
#   clone()
#   getturtle() | getpen()
#   getscreen()
#   setundobuffer()
#   undobufferentries()
#   tracer()
#   window_width()
#   window_height()
# 24.5.2.2. Methods of TurtleScreen/Screen
#  Window control
#   bgcolor()
#   bgpic()
#   clear() | clearscreen()
#   reset() | resetscreen()
#   screensize()
#   setworldcoordinates()
#  Animation control
#   delay()
#   tracer()
#   update()
#  Using screen events
#   listen()
#   onkey()
#   onclick() | onscreenclick()
#   ontimer()
#  Settings and special methods
#   mode()
#   colormode()
#   getcanvas()
#   getshapes()
#   register_shape() | addshape()
#   turtles()
#   window_height()
#   window_width()
#  Methods specific to Screen
#   bye()
#   exitonclick()
#   setup()
#   title()


import turtle
import time
 

turtle.setup(720,480)
leg1 = turtle.Turtle()
leg2 = turtle.Turtle()
leg3 = turtle.Turtle()
p1 = turtle.Turtle()
p2 = turtle.Turtle()
xStart = -210
yStart = 180
pxStart = 50
LOW_Y = -122.57

legF = 320
def A():
    leg1.penup()
    leg2.penup()
    leg3.penup()
    leg1.goto(xStart, yStart)
    leg2.goto(xStart, yStart)
    leg3.goto(-275, 0)
    leg1.pendown()
    leg2.pendown()
    leg3.hideturtle()
    leg1.setheading(250)
    leg2.setheading(289)
    #FILLING IN
    leg1.forward(legF)
    leg2.forward(legF)
    leg3.forward(127)
    leg1.setheading(0)
    leg1.forward(30)
    leg1.goto(-250, -20)
    leg1.setheading(0)
    leg1.forward(80)
    leg1.goto(-135, -122)
    leg1.goto(-105.82,-122.57)
    leg3.pendown()
    leg3.showturtle()
    leg3.setheading(109)
    leg3.forward(30)
    leg3.seth(180)
    leg3.forward(107)
    leg3.hideturtle()
    leg1.hideturtle()
    leg2.hideturtle()
    

def P():
    p1.penup()
    p2.penup()
    p1.goto(pxStart, yStart)
    p2.goto(pxStart, yStart)
    p1.pendown()
    p2.pendown()
    p1.goto(pxStart, LOW_Y)
    p2.speed(10)
    circle("down")

def circle(b):
    if b == "down":
        for i in range(265):
            p2.forward(1)
            p2.left(-.7)
    else:
        for i in range(265):
            p2.forward(1)
            p2.left(.7)
        
        
        
A()
P()
time.sleep(20)
