#!/usr/bin/env python
#

# @author Brian Arnold
# @version November, 2018
# @course Programming 1
# @assign.ment Turtle stuff
# @descrip.tion 
# 
# This is a short reference of how to use some of the simpler turtle graphics
# functions in four example functions, as well as a list of the turtle functions 
# available in Python 2.
#



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


############# Function definitions go here ###################

#########################################
def demo1():
    turtle.setup(720,480)        # make a screen 720px wide, 480px high
    alex = turtle.Turtle()      # create a turtle named alex
    alex.forward(150)           # tell alex to move forward by 150 units
    alex.left(90)               # turn by 90 degrees
    alex.forward(75)            # move forward 75 units
    
    #turtle.done()
    


#########################################
def fnRelativeMovement():
    turtle.setup(720,480)
    t1 = turtle.Turtle()     # create a turtle, call it t1

    for i in range(4):         # create a loop that does something four times
        t1.forward(50)             # go forward 50 units
        t1.right(90)             # turn right 90 degrees

    turtle.done()



#########################################
def fnAbsoluteMovement():
    turtle.setup(720,480)
    t1 = turtle.Turtle()    # create a turtle, call it t1

    t1.setheading(0)        # point the direction to zero degrees (east)
    t1.pendown()            # put the pen down to draw
    startX = t1.xcor()        # save current X coordinate
    startY = t1.ycor()        # save current Y coordinate
    t1.goto(startX + 100, startY + 50)    # move to a new X,Y coordinate, drawing 
                                        # along the way since the pen is down
    t1.penup()                # take pen up, stop drawing


    t1.setx(startX)            # Set new X coord (no draw since pen is up)
    startY = startY + 100    # Calculate and set new Y coord
    t1.sety(startY)
    t1.pendown()            # put pen down
    t1.goto(startX + 100, startY + 50)    # go direction to new X,Y coordinate

    turtle.done()



######### Function calls go below here ###############

demo1()
#fnRelativeMovement()
#fnAbsoluteMovement()


