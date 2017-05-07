# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:37:54 2016

@author: pradeep Sathyamurthy
"""
# Program for Ashrita
# Get the input from User for Days and Prints its abbrevation using a function

def week():
    while True:
        day = input("Enter the Day abbrevation (Mo/Tu/We/Th/Fr/Sa/Su) to print or Done to exit the program:::")
        if(day=='Done' or day=='done'):
            break
        else:
            try:
                day=str(day)
                if(day=='Mo'):
                    print("It is Monday")
                elif(day=='Tu'):
                    print("It is Tuesday")
                elif(day=='We'):
                    print ("It is Wednesday")
                elif(day=='Th'):
                    print ("It is Thursday")
                elif(day=='Fr'):
                    print("It is Friday")
                elif(day=='Sa'):
                    print("It is Saturday")
                elif(day=='Su'):
                    print("It is Sunday")
                else:
                    print("Valid abbrevations are Mo/Tu/We/Th/Fr/Sa/Su!!!")
                continue
            except:
                print("Print a valid value")
                continue
    print("Seems you are done!")
    print("Program Ends!!!")

# Using/calling the funtion
week()
        
