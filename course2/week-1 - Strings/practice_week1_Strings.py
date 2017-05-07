# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:58:41 2016

@author: prade
Note: Strings are immutable. However, list types are mutable
immutable = An object whose values can unchange
"""

# Strings
fruit = 'BANANA'

# Finding the length of the string
length = len(fruit)
print(length)
fruit[0]
fruit[length-1]

# Traversing through the strings
for i in fruit:
    print(i)

# Slicing - segment of a string is called slicing
fruit[0:2] # will print first two char, indexed in 0 and 2-1 = 1
fruit[1:] # print all character from index [1]
fruit[:3] # print from first char untill [3-1]=[2] index which is N
fruit[:] # print the entire string
help("slice") # used for extended slicing, read through the usage when needed
# Python's string are immutable

# Looping and counting
# Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
def loop_count(word, letter):
    word = word
    charecter = letter
    count=0
    for i in word:
        if (i == charecter):
            count=count+1
    if(count>0):
        print("number of time letter "+ charecter + " occured in " + word +" is>>>>",count)
    else:
        print("Charecter is not present in the word!!!")


# calling the function
loop_count('BANANA','A') # Strings are case sensitive, need to tbe handled explicitly
loop_count('BANANA','Z')
loop_count('BANANA','a')

# in operator
'A' in fruit
'a' in fruit # this return false as again strings are case sensitive
'NAN' in fruit

# String comparison 
fruit == 'BANANA'
fruit < 'ZARA'
'ZARA' < fruit

# string methods
# https://docs.python.org/2/library/stdtypes.html#string-methods
print(fruit)
type(fruit) # this will list the variable type is string
dir(fruit) # this will list the methods that can be applied to a string
print(fruit.upper()) # fill convert the string letters into upper case and print, note that value of actual objects stays in tact
print(fruit.capitalize()) # first char of the string is capitalized
print(fruit.find('NA')) # prvides the index of the occurence
sample_fruit = '  Banana '
print(sample_fruit.strip()) # strip off the blank spaces throughout, there is also lstrip and rstrip
fruit.startswith('B') # Check if a string start with a particular char or string and return a boolean value (True/False)

# Format String
# Used to print a charcter in print statement dynamically through variable names
number_fruit = 3
my_name = 'Pradeep'
fruit_cost = 1.2
print('%s bought %d %s at a cost of $%g' %(my_name,number_fruit,fruit,fruit_cost))





















