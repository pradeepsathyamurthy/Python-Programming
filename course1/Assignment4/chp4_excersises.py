# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 23:30:39 2016

@author: pradeep sathyamurthy
"""
# Chapter 4
# Functions
# Probelm 4.5 and 4.6

def fred():
    print("Zap")

def jane():
    print("ABC")

jane()
fred()
jane()


# Problem 4.6

def computepay(hours,rate):
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
        
type (computepay)
hours=input("Enter Hours: ")
rate=input("Enter Rate: ")
computepay(hours,rate)
print("Program Complete!!!")

# Program 4.7

def computegrade(score):
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

score=input("Enter Score between 0.0 and 1.0: ")
computegrade(score)
print("Program Complete!!!")