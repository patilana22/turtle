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
 

turtle.setup(720,480)
wiz = turtle.Turtle()

while True:
    wiz.penup()
    wiz.goto(-250, 200)
    wiz.pendown()
    wiz.setheading(252)
    wiz.forward(20)
