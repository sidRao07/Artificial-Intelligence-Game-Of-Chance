#!/usr/bin/env python
"""
Created on Wed Oct 10 15:24:24 2018

@author: sidar
"""
import sys


def roll():
    if(die_1 <org_expected or die_2 <org_expected or die_3 <org_expected):
        if(die_1 <org_expected):
            print("re-roll die 1")
        if(die_2 <org_expected):
            print("re-roll die 2")
        if(die_3 <org_expected):
            print("re-roll die 3")
    else :
        print("no change")
def roll2(die,otherDie,number):
    expected=0
    for i in range(1,7):
        if(i==die):
            expected+= (25-die-die)*1/6.0
        else :
            expected+=i*1/6
    if(die< org_expected):
        x= org_expected
    else :
        x=die
 
    if(die+die +expected>x+x+otherDie):
        if(otherDie< org_expected):
            y= org_expected
        else :
            y=otherDie
        if(die+die +otherDie<x+x+y):
            roll()
        else :    
            print("re roll die ",number)
    else:
        roll()    
def die_func(die_1,die_2,die_3):    
    if(die_1==die_2==die_3):
        print("do not re -roll")

    elif(die_1==die_2 or die_1 ==die_3 or die_2==die_3):
        if(die_1==die_2):
            roll2(die_1,die_3,3)
        elif(die_1==die_3):    
            roll2(die_1,die_2,2)
        else :
            roll2(die_2,die_1,1)
        
    elif (die_1!=die_2 and die_1!=die_3 and die_2!=die_3):
        roll()

die_1=int(sys.argv[1])
die_2=int(sys.argv[2])
die_3=int(sys.argv[3])

org_expected=0
for i in range(1,7):
    org_expected+= i*1/6.0 
die_func(die_1,die_2,die_3)  
        
