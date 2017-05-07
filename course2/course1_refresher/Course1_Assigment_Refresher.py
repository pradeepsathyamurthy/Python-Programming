# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 18:45:16 2016

@author: prade
"""
# Assignment-1
print("hello world")

# Assignment-2 - Geeting the input from user and printing it 
name=input("Enter your name:::")
print("Your Name is::::",name)

# Excersie Program2 - Get the number of hours worked and pay per hour and calcualte the same
hours = input("print the number of hours worked:::")
wage = input("What is the hourly pay:::")
salary = float(hours) * float(wage)
print("Your Salary is:::",salary)

# Excersice Program3 - converting celcius to farenhiet
degree_celcius = input("Enter the temperature in celcius")
degree_celcius = float(degree_celcius)
degree_farenhiet=(degree_celcius*(9/5)) + 32
print("Converted Temperature in Farenhiet is:::",degree_farenhiet)

# Assignment-3 - Using try and except block
try:
    degree_celcius = input("Enter the temperature in celcius:::")
    degree_celcius = float(degree_celcius)
    degree_farenhiet=(degree_celcius*(9/5)) + 32
    print("Converted Temperature in Farenhiet is:::",degree_farenhiet)
except:
    print("Enter a valid number")

# Assignment-4 - Functions
def prady():
    print("My Name is Prady")
name = prady()

def names_print(name):
    print("Name inputed is:::",name)

name=input("Enter your name:::")
names_print(name)

# Assignment-5 - for list
set = [12,23,23,12,12,43,56,67,43,34,1,-68]
# Count the number of items in the list
count=0
for i in set:
    count=count+1
print("number of values in the sets are:::",count)

# Sum of items in the list
summ=0
for i in set:
    summ=summ+i
print("Sum of sets is:::",summ)

# Finding the largest value in the list
largest=0
for i in set:   
    if(largest < i):
        largest=i
print("Largest number of the set is:::",largest)

# Finding the smallest number in the list
smallest = None
for i in set:
    if (i != None):
        smallest=i
    if (i!=None and smallest > i):
        smallest=i
print("Smallest Number is:::",smallest)