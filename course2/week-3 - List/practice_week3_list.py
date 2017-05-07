# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 08:31:42 2016

@author: prade
Note: Most of the list methods are void functions. However, strings are not
"""

t = ['b','d','a','z','m','e']
print(t)
type(t)
dir(t)
t.sort()
print(t)
# Be careful with the usage of the assignment in the list operations
t = t.sort() # Because most of the list methods are void methods. they dont return any values. THere job is to change the list directly and return nothing
print(t)

mail_id = 'psathyam@mail.depaul.edu'
mail_split = mail_id.split('@')
print(mail_split[1])

num_list=list()
while (True):
    data_input=input("Enter the Numbers:::")    
    if (data_input=='Done'):break
    value=float(data_input)
    num_list.append(value) # this is called mutable; values of the object can be changed and modified

average=sum(num_list)/len(num_list)
print("Average::::",average)

# Assignment-1
"""
'Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
'The program should build a list of words. For each word on each line check to see if the word is already in the list and 
'if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order. 
'You can download the sample data at http://www.pythonlearn.com/code/romeo.txt'
"""
import os
os.chdir("D:\Courses\Coursera\Python\course2\week-3")
data_romeo = open("romeo.txt")
#print(data_romeo) # Prints the file handler
lines_list=list()
for lines in data_romeo:
    lines=lines.rstrip()
    #print(lines)
    lines_split=lines.split()
    #print(lines_split)
    lines_list.append(lines_split)
print(lines_list)
final_word=list()
for words in lines_list:
    for word in words:
        #print(word)
        if(word in final_word):continue
        final_word.append(word)
final_word.sort()
print(final_word)
data_romeo.close()

# Assignment-2
"""
'8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line: 
'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
'You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who 
'sent the message). Then print out a count at the end. 
'Hint: make sure not to include the lines that start with From:'.
'You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt'
"""

mbox_data=open("mbox-short.txt")
lines_lst=list()
count=0
for lines in mbox_data:
    lines=lines.rstrip()    
    if(lines.startswith("From ")):
        delimiter=' '
        lines_split=lines.split(delimiter)
        print(lines_split[1])
        count=count+1
print ("There were", count, "lines in the file with From as the first word")













