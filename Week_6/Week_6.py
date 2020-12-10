# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 20:54:26 2020

@author: Faique
"""
import cv2
import time
import numpy as rect


'''
----------------------------------------
           QUESTION :01
    (Draw Rectangle on Sprite Sheet)
----------------------------------------
'''

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
        
        #Drawing a rectangle
        coordinates = rect.array([[30,140],[30,40],[160,40],[160,140]])
        cv2.polylines(sprites, [coordinates] , True, (0,0,255),3)  
        
        while True:
            time.sleep(1/30)
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