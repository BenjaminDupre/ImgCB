#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:17:45 2020

@author: calypso
"""
# Defining working directory (this need to be set up to where you downloaded 
# the files from github)
# Loading libraries
from PIL import Image, ImageDraw
import numpy as np
import os

# opening the function definition. 
def checkmask(image_name,revealed):
    
    """
    Reveals a picture covered by 9 pieces of black in a particular. 
    It uses as input the 'image_name' of the 'image.jpg' and the 
    number between 1-9 of pieaces to 'reveal'.
    It returns a window with the number of pieces revealing the picture. 
    
    Example:
    --------    
    checkmask('blackmail.jpg',3)
    """
    
    # Opening inputed image
    pict = Image.open(image_name)
    # getting picture size 
    w, h = pict.size
    # geting relevants points to build piece (one third to get nine pieces)
    w1 = w//3
    h1 =h//3
    start=0
    # Building mask from 'https://note.nkmk.me/en/python-pillow-composite/'
    mask = Image.new('RGB',pict.size)
    draw = ImageDraw.Draw(mask)
    white = (255,255,255)
    # creating each of the nine pieces. 
    if revealed ==1:
        draw.rectangle((start,start,w1,h1), fill= white)
    
    elif revealed ==2:
        draw.rectangle((start,start,w1,h1), fill= white)
        draw.rectangle((w1,h1,w1+w1,h1+h1),fill= white)
        
    elif revealed == 3:
        draw.rectangle((start,start,w1,h1), fill= white)
        draw.rectangle((w1,h1,w1+w1,h1+h1),fill= white)
        draw.rectangle((w1+w1,h1+h1,w,h),fill= white )
        
    elif revealed == 4:
        draw.rectangle((start,start,w1,h1), fill= white)
        draw.rectangle((w1,h1,w1+w1,h1+h1),fill= white)
        draw.rectangle((w1+w1,h1+h1,w,h),fill= white)
        draw.rectangle((w1+w1,start,w, h1), fill= white)
        
    elif revealed == 5:
        draw.rectangle((start,start,w1,h1), fill= white)
        draw.rectangle((w1,h1,w1+w1,h1+h1),fill= white)
        draw.rectangle((w1+w1,h1+h1,w,h),fill= white)
        draw.rectangle((w1+w1,start,w, h1), fill= white) 
        draw.rectangle((start,h1+h1,w1, h), fill= white)
        
    elif revealed == 6:
        draw.rectangle((start,start,w1,h1), fill= white)
        draw.rectangle((w1,h1,w1+w1,h1+h1),fill= white)
        draw.rectangle((w1+w1,h1+h1,w,h),fill= white)
        draw.rectangle((w1+w1,start,w, h1), fill= white) 
        draw.rectangle((start,h1+h1,w1, h), fill= white) 
        draw.rectangle((w1,start,w1+w1, h1), fill= white)
        
    elif revealed == 7:
        draw.rectangle((start,start,w1,h1), fill= white)
        draw.rectangle((w1,h1,w1+w1,h1+h1),fill= white)
        draw.rectangle((w1+w1,h1+h1,w,h),fill= white)
        draw.rectangle((w1+w1,start,w, h1), fill= white) 
        draw.rectangle((start,h1+h1,w1, h), fill= white) 
        draw.rectangle((w1,start,w1+w1, h1), fill= white)
        draw.rectangle((start,h1,w1,h1+h1), fill= white)
        
    elif revealed == 8:
        draw.rectangle((start,start,w1,h1), fill= white)
        draw.rectangle((w1,h1,w1+w1,h1+h1),fill= white)
        draw.rectangle((w1+w1,h1+h1,w,h),fill= white)
        draw.rectangle((w1+w1,start,w, h1), fill= white) 
        draw.rectangle((start,h1+h1,w1, h), fill= white) 
        draw.rectangle((w1,start,w1+w1, h1), fill= white)
        draw.rectangle((start,h1,w1,h1+h1), fill= white)
        draw.rectangle((w1+w1,h1,w,h1+h1), fill= white)
        
    elif revealed == 9:
        draw.rectangle((start,start,w1,h1), fill= white)
        draw.rectangle((w1,h1,w1+w1,h1+h1), fill= white)
        draw.rectangle((w1+w1,h1+h1,w,h), fill= white)
        draw.rectangle((w1+w1,start,w, h1), fill= white) 
        draw.rectangle((start,h1+h1,w1, h), fill= white) 
        draw.rectangle((w1,start,w1+w1, h1), fill= white)
        draw.rectangle((start,h1,w1,h1+h1), fill= white)
        draw.rectangle((w1+w1,h1,w,h1+h1), fill= white)
        draw.rectangle((w1,h1+h1,w1+w1,h), fill= white)
    #error message if the peice input is out of range or wrong    
    else:
        raise ValueError("Error in Input: the typed number revealed must be between 1 and 9")
    # saving mask on wd to later use on picture
    mask.save(os.getcwd() + '/mask.jpg', quality=95)
    # using mask on picture
    src= np.array(pict)
    mask = np.array(mask)
    mask = mask/255
    dst = src * mask
    Image.fromarray(dst.astype(np.uint8)).save(os.getcwd() + "/numpy_image_mask.jpg")
    # Showing output
    a = Image.open('numpy_image_mask.jpg')
    return a.show() 

