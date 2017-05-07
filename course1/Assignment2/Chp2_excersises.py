# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:58:05 2016

@author: prade
"""

# Excersie Program1
# Program to get user input
name=input("Enter your Name: ") # in PY2.0 we use raw_input() to get user values
print("Hellow",name)

# Excersie Program2
hours=input("Enter Hours: ")
rate=input("Enter Rate: ")
pay= float(hours)*float(rate)
print("Pay: ",pay)
print("Rounded Payment: ",round(pay))


# Excersice Program3
width=17
height=12.0
width/2 # Result in PY3.0 is 8.5; Result in Py2.0 it will be 8
width/2.0 # Result is 8.5 for both PY3.0 and OY 2.5
height/3 # Result is 8.5 for both PY3.0 and OY 4.0
1+2*5 # ans is 11 as per BODMAS priority

# Excersice Program4
celcius=input("Enter the Temperature in Celcius: ")
degree_celcius=float(celcius)
degree_farenhiet=(degree_celcius*(9/5)) + 32
print("Faranhiet equalent for",degree_celcius,"is: ",degree_farenhiet)

