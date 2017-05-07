# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:58:05 2016

@author: pradeeep
"""

# Chapter 3
# Conditional and Exception Handling
# Probelm 3.1 and 3.2

hours=input("Enter Hours: ")
rate=input("Enter Rate: ")
try:
    hours=float(hours)
    rate=float(rate)

    if(hours>40):
        extra_hrs=hours-40
        pay= (40*rate) + (1.5*rate*extra_hrs)
        print("Pay: ",pay)
        print("Rounded Payment: ",round(pay))
    else:
        extra_hrs=0
        pay= (hours*rate)
        print("Pay: ",pay)
        print("Rounded Payment: ",round(pay))

except:
    print("Either Hour or Rate is not a number")

print("Program Complete!!!")


# Problem 3.3

score=input("Enter Score between 0.0 and 1.0: ")

try:
    score=float(score)
    if(score>0.0 and score <1.0):
        if(score>=0.9): print("A")
        elif(score>=0.8): print("B")
        elif(score>=0.7): print("C")
        elif(score>=0.6): print("D")
        else: print("F")
    else:
        print("Bad Score")

except:
    print("Bad Score")

print("Program Complete!!!")


