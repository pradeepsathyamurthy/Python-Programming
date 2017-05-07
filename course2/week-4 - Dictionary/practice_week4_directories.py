# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:31:07 2017

@author: pradeep Sathyamurthy

Note: Here we will cover more about usage of directories in Python
"""

# creating a empty dictionary, for example consider a bag as a dictionary
eng2sp = dict() # Here we are creating an empty directory, as an anology it means bag is empty now
print(eng2sp)

# adding an item to a dictionary object
# An item is composed of a key and a value
# Key is the indises or like a pointer which points to a value

eng2sp['one']='onnu' # here we are trying to create a dictionary with just one item. key 'one' points to a value called 'uno'
print(eng2sp)

# Creating and defining a dictionary
# As per analogy we are trying to fill a bag with 3 diffrent objects like money, perfume and coins
# Money can have a value say $10 note, coin can hold a value say 10 cents, like that
eng2sp={'one':'uno', 'two':'rendu', 'three':'moonu'}
print(eng2sp) # dictionary wont maintain orders as list does. this is the main difference

# accesing the dictionary
print(eng2sp['one']) # dictionary can be accessed using the key name

# accessing a key which is not in a dictionary
print(eng2sp['four']) # this will through an exception saying keyerror, keyerror means there is no such key which exists

# functions usage
len(eng2sp) # length of the dictionary object is defined by total number of key that exists in a dictionary

# in operator 
# for list this in operator uses linear search algorithm
# for dictionary in operator uses hash table algorithm
# for more detail on hash table refer http://wikipedia.org/wiki/Hash_table
'one' in eng2sp # this will return true as this key exists in dictionary object
'four' in eng2sp # this will return false 

# to check the presence of any value instead of a key we can use values() function
vals=eng2sp.values()
print(vals)
'moonu' in vals # now this will return true value

# Dictionaries are basically used for counting purpose
# we are effectively computing a histogram here, that is the number of times each charecter has been in the word
word='brontosaurus'
d=dict() # defining the dictionary
for c in word:
    if c not in d: # checking if a character is already present as a key in dictionary
        d[c]=1 # if not we are setting the value as 1 for that particular character being the key
    else:
        d[c]=d[c]+1 # if key is already present we are tring to increment the value by 1
print(d)


# get() method
# it takes key and a defalt value
# if that key is presnt it will return the key with respective value
# if not it will return the defaul value

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
counts.get('jan',0) # this will return the value against the key jan
counts.get('feb',0) # this will return the default value 0 as key is not found in dictionary


# re-writing the progam of count using get() function
word='brontosaurus'
d=dict()
for c in word:
    d[c]=d.get(c,0)+1 # this replaces the 4 lines of if-else statement  with just 1 get function
print(d)

# dictionaries and files
# another common use of dictionary is word count in files
filename='romeo.txt'
file_handle=open(filename,'r')
words=dict()
for lines in file_handle:
    print(lines)
    word=lines.split()
    for wor in word:
        print(wor)
        words[wor]=words.get(wor,0)+1
print(words)
for key in words:
    print(key,words[key])
# Printing the key in sorted order
key_list=list()
key_list=words.keys() # this create a data type called dict_key
key_list=list(key_list) # in python 3.5 there is no sort attribute for dictionary object
type(key_list)
dir(key_list)
key_list.sort()
for key in key_list:
    print(key,words[key])
file_handle.close()

# how to use translate to remove punctuation

# this is a sample code
import string
name="hi! my name is Pradeep's sathya.murthy"
print(name)
type(name)
string.punctuation
translator = str.maketrans('', '', string.punctuation) #This is a code used to create a table like structure with key value
name.translate(translator)
# sample code ends


import os
import string
string.punctuation
#help(str.translate)
os.chdir("D:\Courses\Coursera\Python\course2\week-4")
filename='romeo-full.txt'
file_handle=open(filename,'r')
counts=dict()
for lines in file_handle:
    lines=lines.strip()
    translator = str.maketrans('', '', string.punctuation)
    lines=lines.translate(translator)
    lines=lines.lower()
    words=lines.split()
    for word in words:
        print(word)
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1
print(counts)
file_handle.close()


stuff = dict()
print(stuff['candy'])


stuff = dict()
print(stuff.get('candy',-1))

word='brontosaurus'
counts=dict()
for key in word:
    if key in counts:
        counts[key] = counts[key] + 1
    else:
        counts[key] = 1
print(counts)


word='brontosaurus'
counts=dict()
for key in word:
    if key in counts:
        counts[key] = counts[key] + 1
    else:
        counts[key] = 1
print(counts)

word='brontosaurus'
counts=dict()
for key in word:
    counts[key]=counts.get(key,0)+1
print(counts)

# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
"""
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer
"""
import os
os.chdir("D:\Courses\Coursera\Python\course2\week-4")
file_name="mbox-short.txt"
mail_dict=dict()
max_profile=0
file_handle=open(file_name)
for lines in file_handle:
    lines=lines.strip()
    lines=lines.lower()
    if lines.startswith('from '):
        #print(lines)
        lines_split=lines.split()
        #print(lines_split[1])
        mail_dict[lines_split[1]]=mail_dict.get(lines_split[1],0)+1
#print(mail_dict)
for i in mail_dict:
    #print(i,mail_dict[i])
    if mail_dict[i] > max_profile:
        max_key=i
        max_profile=mail_dict[i]
print(max_key,mail_dict[max_key])
file_handle.close()


























