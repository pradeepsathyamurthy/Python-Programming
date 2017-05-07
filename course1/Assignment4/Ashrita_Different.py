# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:50:11 2016

@author: pradeep sathyamurthy
"""

# Creating the different function
# I have placed print statements for you to understand the work flow
# Once you understand it remove the unnecessary print statements
def different(t):
    maxi=0
    try:
        for i in t:
            print("Value of i>>>>>>",i)
            for j in i:
                print("value of j>>>>>>",j)
                j=int(j)
                if(j>maxi):
                    maxi=j
        print("Maximum Value is >>>>>>>>",maxi)
    except:
        print("Eter a valid list value")
    print("Program Ends!!!")


# Calling the function
# Looks like they have asked you to get the inout from user, so see you handle it Ashrita
# Or if this is what expected you are good to go with this program
t=[[1,0,1],[0,1,0]] 
different(t)

