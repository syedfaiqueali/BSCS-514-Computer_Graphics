# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:06:06 2020

@author: faiq
"""

import turtle



'''
--------------------------------------
        QUESTION :01
       Draw your name
--------------------------------------

class Turtle:
    # instance attribute
    def __init__(self, turtle_color, turtle_width, turtle):
        self.turtle_color = turtle_color
        self.turtle_width = turtle_width
        self.turtle = turtle
        
        turtle.color(turtle_color)
        turtle.width(turtle_width)
            
    def drawF(self):
        t.penup()
        t.goto(-250,0)  
        t.pendown()
        t.left(90)
        t.forward(150)
        t.right(90)
        t.forward(100)
        t.backward(100)
        t.right(90)
        t.forward(75)
        t.left(90)
        t.forward(75)
        
        t.penup()
        t.goto(-150,0)   
        
    def drawA(self):
        t.pendown()
        t.left(75)
        t.forward(150)
        t.right(145)
        t.forward(100)
        t.right(110)
        t.forward(60)
        t.backward(60)
        t.left(110)
        t.forward(50)
        
        t.penup()
        t.goto(-30,0)
        
    def drawI(self):
        t.pendown()
        t.left(70)
        t.forward(100)
        t.backward(50)
        t.left(90)
        t.forward(150)
        t.left(90)
        t.forward(50)
        t.back(100)
        
        t.penup()
        t.goto(120,0)
        
    def drawQ(self):
        t.pendown()
        t.left(180)
        t.forward(80)
        t.left(90)
        t.forward(150)
        t.left(90)
        t.forward(80)
        t.left(90)
        t.forward(150)
        t.left(90)
        t.forward(80)
        t.right(50)
        t.forward(20)
        

#setting up workscreen 
ws=turtle.Screen() 
  
#defining turtle instance 
t=turtle.Turtle() 

# instantiate the Turtle class
tur = Turtle("Orange",15,t)
tur.drawF()
tur.drawA()
tur.drawI()
tur.drawQ()

# For closing the window
turtle.done()
turtle.bye()
'''



  
'''
--------------------------------------
        QUESTION :02
      Sierpinski Algorithm
--------------------------------------


#setting up workscreen 
ws=turtle.Screen() 
  
#defining turtle instance 
t=turtle.Turtle() 
  
#turtle pen will be of "TEAL" color 
t.color("Teal") 

t.speed(10)

t.right(30)
t.penup()
t.hideturtle()
t.shape("triangle")

def sierpinski(size, order):
    if order == 0:
        t.stamp()
    else:
        for i in range(0,3):
            t.forward(size)
            sierpinski(size/2, order-1)
            t.backward(size)
            t.left(120)


sierpinski(100,3)

# For closing the window
turtle.done()
turtle.bye()
'''



























