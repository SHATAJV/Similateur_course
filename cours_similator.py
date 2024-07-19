#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Course Similator:
"""

import random
total_distance = 2400
min_number_horses = 12
max_number_horses =20

def start_dice():
    return  random.randint(1, 6)
 def Speed(currenct_speed, DQ):
     if DQ:
         return currenct_speed, DQ
     dice=start_dice()
     if currenct_speed ==0:
         if dice ==1 or dice==2:
             DQ= True
     elif currenct_speed ==1:
         if dice==1:
             currenct_speed +=1
     elif currenct_speed==2:
         if dice in [1,2]:
             currenct_speed +=1
     elif currenct_speed==3:
         if dice in [4,5]:
             currenct_speed +=1
         elif dice==1:
             currenct_speed -=1
     elif currenct_speed==4:
         if dice==1:
             currenct_speed -=1
     elif currenct_speed==5:
         if dice in [1,2]:
             currenct_speed -=1
     elif currenct_speed ==6:
         if dice in [1,2]:
             currenct_speed -=1
         elif dice==6:
             DQ=True

     if currenct_speed<0:
         currenct_speed

     return currenct_speed,DQ

def position_horse (position, speed, DQ):
    for i, pos in enumerate(position):
        status = "DQ" if DQ[i] else f"Position: {pos} m, Speed: {speed[i]} m/s"
    print(f"Horse {i+1} - {status}")
def winner(positions):
    for i, pos in enumerate(positions):
        if pos >= total_distance:
            return i
            return None