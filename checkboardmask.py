#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:56:16 2020

@author: calypso
"""
# Loading libraries
# from io import BytesIO as byt (use from internet)
# import requests (use from internet)
from PIL import Image, ImageDraw
import os
import numpy as np

# Defining directory
wd = "/Users/calypso/github/ImagesCheckBoard"
os.chdir(wd)
#opening image 
#url = 'https://media.wired.com/photos/5e593510bd2cfe00085b5600/master/w_1600%2Cc_limit/photo_mauve_il-miracolo_10.jpg' (use from internet)
#response = requests.get(url) (use from internet)
#pict = Image.open(byt(response.content)) (use from internet)
pict = Image.open('blackmail.jpg')
# defining number of pieces
revealed = 8
# getting pieces size 
w, h = pict.size
# geting relevants points for piece  
w1 = w//3
h1 =h//3
start=0
# Building mask from 'https://note.nkmk.me/en/python-pillow-composite/'
mask = Image.new('RGB',pict.size)
draw = ImageDraw.Draw(mask)

if revealed ==1:
    draw.rectangle((start,start,w1,h1), fill= (255,255,255))

elif revealed ==2:
    draw.rectangle((start,start,w1,h1), fill= (255,255,255))
    draw.rectangle((w1,h1,w1+w1,h1+h1),fill= (255,255,255))
    
elif revealed == 3:
    draw.rectangle((start,start,w1,h1), fill= (255,255,255))
    draw.rectangle((w1,h1,w1+w1,h1+h1),fill= (255,255,255))
    draw.rectangle((w1+w1,h1+h1,w,h),fill= (255,255,255) )
    
elif revealed == 4:
    draw.rectangle((start,start,w1,h1), fill= (255,255,255))
    draw.rectangle((w1,h1,w1+w1,h1+h1),fill= (255,255,255))
    draw.rectangle((w1+w1,h1+h1,w,h),fill= (255,255,255))
    draw.rectangle((w1+w1,start,w, h1), fill= (255,255,255))
    
elif revealed == 5:
    draw.rectangle((start,start,w1,h1), fill= (255,255,255))
    draw.rectangle((w1,h1,w1+w1,h1+h1),fill= (255,255,255))
    draw.rectangle((w1+w1,h1+h1,w,h),fill= (255,255,255))
    draw.rectangle((w1+w1,start,w, h1), fill= (255,255,255)) 
    draw.rectangle((start,h1+h1,w1, h), fill= (255,255,255))
    
elif revealed == 6:
    draw.rectangle((start,start,w1,h1), fill= (255,255,255))
    draw.rectangle((w1,h1,w1+w1,h1+h1),fill= (255,255,255))
    draw.rectangle((w1+w1,h1+h1,w,h),fill= (255,255,255))
    draw.rectangle((w1+w1,start,w, h1), fill= (255,255,255)) 
    draw.rectangle((start,h1+h1,w1, h), fill= (255,255,255)) 
    draw.rectangle((w1,start,w1+w1, h1), fill= (255,255,255))
elif revealed == 7:
    draw.rectangle((start,start,w1,h1), fill= (255,255,255))
    draw.rectangle((w1,h1,w1+w1,h1+h1),fill= (255,255,255))
    draw.rectangle((w1+w1,h1+h1,w,h),fill= (255,255,255))
    draw.rectangle((w1+w1,start,w, h1), fill= (255,255,255)) 
    draw.rectangle((start,h1+h1,w1, h), fill= (255,255,255)) 
    draw.rectangle((w1,start,w1+w1, h1), fill= (255,255,255))
    draw.rectangle((start,h1,w1,h1+h1), fill= (255,255,255))
elif revealed == 8:
    draw.rectangle((start,start,w1,h1), fill= (255,255,255))
    draw.rectangle((w1,h1,w1+w1,h1+h1),fill= (255,255,255))
    draw.rectangle((w1+w1,h1+h1,w,h),fill= (255,255,255))
    draw.rectangle((w1+w1,start,w, h1), fill= (255,255,255)) 
    draw.rectangle((start,h1+h1,w1, h), fill= (255,255,255)) 
    draw.rectangle((w1,start,w1+w1, h1), fill= (255,255,255))
    draw.rectangle((start,h1,w1,h1+h1), fill= (255,255,255))
    draw.rectangle((w1+w1,h1,w,h1+h1), fill= (255,255,255))
elif revealed == 9:
    draw.rectangle((start,start,w1,h1), fill= (255,255,255))
    draw.rectangle((w1,h1,w1+w1,h1+h1),fill= (255,255,255))
    draw.rectangle((w1+w1,h1+h1,w,h),fill= (255,255,255))
    draw.rectangle((w1+w1,start,w, h1), fill= (255,255,255)) 
    draw.rectangle((start,h1+h1,w1, h), fill= (255,255,255)) 
    draw.rectangle((w1,start,w1+w1, h1), fill= (255,255,255))
    draw.rectangle((start,h1,w1,h1+h1), fill= (255,255,255))
    draw.rectangle((w1+w1,h1,w1,h1+h1), fill= (255,255,255))
    draw.rectangle((w1,h1+h1,w1+w1,h), fill= (255,255,255))
else:
    ValueError("Error in Input: please put a number \
               of pieces to reveal between 1 and 9")
mask.save(wd + '/mask.jpg', quality=95)
# using mask
src= np.array(pict)
mask = np.array(mask)
mask = mask/255
dst = src * mask
b = Image.fromarray(dst.astype(np.uint8)).save(wd + "/numpy_image_mask.jpg")
#output
a = Image.open('numpy_image_mask.jpg')
a.show()




