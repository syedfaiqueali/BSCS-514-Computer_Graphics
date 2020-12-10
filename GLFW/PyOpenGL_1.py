# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:11:31 2020

@author: Faique
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1,-1, -1),
    (1, 1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1, 1),
    (1, 1, 1),
    (-1,-1,1),
    (-1, 1,1),
)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4,),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,1,0),
    (1,1,1),
    (0,1,1), 
    )

'''
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1), 
'''
'''
    (1,0,1),
    (0,1,0),
    (1,1,0),
    (0,1,1),
    (1,0,1),
    (0,1,0),
    (1,1,0),
    (0,1,1),
    (1,0,1),
    (0,1,0),
    (1,1,0),
    (0,1,1),  
'''




def Cube():
    #For edges color
    glBegin(GL_QUADS)
    
    #glColor3fv((1,1,0))  #for static color
    x=0
    for surface in surfaces:
        #x=0
        x+=1
        for vertex in surface:
            #x+=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()
    
    #Whenever write GL code so it will come in between glBegin and glEnd
    glBegin(GL_LINES) #Paramter to tell type of graphics
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex]) #To connect the dots
    glEnd()


def main():
    pygame.init()  #Initialization for pygame
    display = (800,600) 
    
    #Set the display and notify it to use OpenGL
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) 
    
    #Field of View, Aspect Ratio, z-near, z-far(i.e: clipping planes)
    gluPerspective(45, display[0]/display[1], 0.1, 50.0)
    
    #x, y, z (moving about the obj)
    glTranslatef(0.0, 0.0, -5)
    
    #Degree, x, y, z
    glRotatef(0, 0 , 0 , 0)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        #To rotate 3D (Psuedo 3D vs Real 3D)
        #glRotatef(1, 3 , 1 , 1)
        
        #Clear the frame
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        #Call the shape defined func
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)
        
    
#Call our main function
main()

















