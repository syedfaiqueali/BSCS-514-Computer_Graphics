# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:27:25 2020

@author: faiq
"""

import matplotlib.pyplot as plt 
import tkinter as tk
import turtle
import cv2
import time

'''
--------------------------------------
           QUESTION :01
    (Draw lines between points)
--------------------------------------

class Line:
    # instance attribute
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        
    def drawLine(self):
        x_values = [self.point1[0], self.point2[0]]
        y_values = [self.point1[1], self.point2[1]]

        plt.plot(x_values, y_values)
   
  

point1 = [5, 10]
point2 = [1, 10]
# instantiate the Line class
l = Line(point1, point2)
l.drawLine()
'''




'''
--------------------------------------
        QUESTION :02
        (Draw n-gons)
--------------------------------------
     
class Polygon:
    # instance attribute
    def __init__(self, coordinates):
        self.coordinates = coordinates
        
    def drawPolygonByMatplotlib(self):
        #repeat the first point to create a 'closed loop'
        self.coordinates.append(coordinates[0]) 
        #create lists of x and y values
        xs, ys = zip(*coordinates) 
        #print(xs)
        #print(ys)
        
        plt.figure()
        plt.plot(xs,ys) 
        plt.show()
        
    def drawPolygonByTkinter(self,points,root):
        #To draw canvas
        canvas = tk.Canvas(root, width = 400, height = 400)
        canvas.pack()
        canvas.create_polygon(points, fill ='teal')
  

root = tk.Tk()
# instantiate the Line class
p = Polygon(coordinates)

coordinates = [[3,1], [5,1], [5.5,3], [4,5], [2.5,3]]
points = [(150,10),(200,50),(175,90),(120,90),(95,50)]

p.drawPolygonByMatplotlib()
p.drawPolygonByTkinter(points, root)
root.mainloop()

''' 




'''
--------------------------------------
        QUESTION :03
       Turtle Graphics
--------------------------------------

class Turtle:
    # instance attribute
    def __init__(self, canvas_size, background_color):
        self.canvas_size = canvas_size
        self.background_color = background_color
        
    def drawPolygon(self,sides,border_color):
        size = self.canvas_size
        angle = 360/ sides
        
        wn = turtle.Screen()
        wn.bgcolor(self.background_color)
        
        tess = turtle.Turtle()
        tess.color(border_color)
        tess.pensize(4)
        
        for i in range(sides):
            tess.forward(size)
            tess.left(angle)


# instantiate the Turtle class
t1 = Turtle(100,'lightgray')
t1.drawPolygon(6,'teal')

turtle.done()
turtle.bye()
'''





'''
--------------------------------------
        QUESTION :04
        Sprite Sheet
--------------------------------------

class SpriteSheet():
    # instance attribute
    def __init__(self, sprite_sheet):
        self.sprite_sheet = sprite_sheet
    
    def animateSpriteSheet(self,rows,col):
        # Making an sprite sheet image variable
        sprites = cv2.imread(self.sprite_sheet)
        
        frame_row = rows  # No of rows of your sprite sheet
        frame_col = col  # No of col of your sprite sheet
        
        # .shape(), is a tuple, 0 -height, 1- width
        height_frame = sprites.shape[0] // frame_row  #// For ans in Int
        width_frame = sprites.shape[1] // frame_col 
        
        i = 0
        j = 0
        
        while True:
            time.sleep(1/10)
            cv2.imshow("sprites", sprites[height_frame*j:height_frame*(j+1),width_frame*i:width_frame*(i+1),:])
            if i == frame_col:
                j += 1
                j = j%frame_row
                
            i += 1
            i = i % frame_row
    
            if cv2.waitKey(1) & 0xff == ord('q'):
                cv2.destroyAllWindows()
                break

        
        
        
# instantiate the Sprite class
s = SpriteSheet('sprite3.png')
s.animateSpriteSheet(4,4)
'''




'''
--------------------------------------
        QUESTION :05
       IMAGE CALCULATOR
--------------------------------------
'''
img_1 = cv2.imread('Check1.jpg',0)
img_2 = cv2.imread('Check2.jpg',0)

# Image Addition
img_3 = img_1 + img_2

cv2.imshow('Image1', img_1)
cv2.imshow('Image2', img_2)
cv2.imshow('Added Image', img_3)

# Image Subtraction
img_4 = img_3 - img_2
cv2.imshow('Subtracted Image', img_4)

cv2.waitKey(10000)
cv2.destroyAllWindows()





