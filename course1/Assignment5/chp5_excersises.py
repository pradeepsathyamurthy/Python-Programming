# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 22:22:54 2016

@author: pradeep Sathyamurthy
"""
       
# Count the number of items in the list

lst=[12,23,23,12,12,43,56,67,43,34]        
counter=0
for lists in lst:
    counter=counter+1 # This is called counter
print("Number of items in the list is: ",counter)

# Total of a set of number

lst=[12,23,23,12,12,43,56,67,43,34,1]        
sum=0
for lists in lst:
    sum=sum+lists # This is called accumilator
print("Sum of the items in the list: ",sum)


# Finding the largest value in the list
lst=[12,23,23,12,12,43,56,67,43,34,1,-68]        
largest=0
for lists in lst:
    if(lists > largest):
        largest=lists
print("Largest number in the list is: ",largest)

# Finding the smallest number in the list
lst=[12,23,23,12,12,43,-82,56,67,43,34,1,-68]        
smallest=None
print("def smallest: ",smallest)
for lists in lst:
    if(smallest is None or lists < smallest):
            smallest=lists
print("Smallest Number is: ",smallest)
    
    
# Alternate
lst=[12,23,23,12,12,43,-82,56,67,43,34,1,-68]        
smallest=min(lst)
print("Smallest Number is: ",smallest)

# Excercise 5.1
counter=0
total=0
avg=0
while True:
    num=input("Enter a Number: ")
    if (num=='Done' or num=='done'):
        break
    else:
        try:
            num=int(num)
            total=total+num
            counter=counter+1
            continue
        except:
            print("Invalid Input")
            continue
avg=total/counter
print(total, counter, avg)



# Excercise 5.2
maxi=0
mini=None
num=0
while True:
    num=input("Enter a Number: ")
    if (num=='Done' or num=='done'):
        break
    else:
        try:
            num=int(num)
            if(num==max or num > maxi):
                maxi=num
            if(mini is None or num < mini):
                mini=num
        except:
            print("Invalid Input")
            continue

print("Maximum Number:::::: ",maxi)
print("Minimum Number:::::: ",mini)
print("Program Ends!")




