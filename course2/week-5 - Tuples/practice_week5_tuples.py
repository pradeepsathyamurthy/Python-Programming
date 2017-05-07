# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:38:36 2017

@author: pradeep sathyamurthy

Note: Tuples can be considered as a list which are immutable
"""

# defning a tuple
t=tuple()
type(t)
dir(t)

# initializing a tuple
t=(1,2,3,4,5,6)
type(t)
print(t)
t[1]

# initializing tuple with just 1 value
t1=('a',) # without comma it will be treated as string
type(t1)
t2=('b')
type(t2)
t3=tuple('prady')
type(t3)
print(t3)
print(t3[:3])
t = ('A',) + t[1:]
print(t)

# Comparing tuple
(0, 1, 2) < (0, 3, 4) # Tuple first look for distnct element and then compare it to provide true or false result and ignore the rest
(0, 1, 2000000) < (0, 3, 4)

# Explanation
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)
res = list()
for length, word in t:
    res.append(word)
print(res)

# Explanation
m = [ 'have', 'fun' ]
type(m)
x,y=m
print(x)
print(y)

x,y=('have','fun')
type(x)

# Explanation
a,b=1,2,3

# splitting the words
addr = 'monty@python.org'
uname, domain = addr.split('@')
print(domain)

# Dictionaries and tuple
d = {'a':10, 'b':1, 'c':22}
t = d.items()
print(t)
sorted(t)

# Multiple assignment with dictionaries
for key, val in d.items():
    print(val, key)

# finding the most common word
import os
os.chdir("D:\Courses\Coursera\Python\course2\week-5")
import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    translator = str.maketrans('', '', string.punctuation)
    line = line.translate(translator)
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
# Sort the dictionary by value
lst = list()
for key, val in counts.items():
    lst.append( (val, key) )
    lst.sort(reverse=True)

for key, val in lst[:10] :
    print(key, val)

fhand.close()

# Using tuples as a keys in dictionary
dir(lst)
dir(t1)

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()

type(x)
type(y)

x=(5,1,3)
y=(6,0,0)

x<y

tmp = list()
c=dict()
for k, v in c.items():
    tmp.append( (v, k) )
    
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])

"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of 
the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time 
using a colon. 
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""
import os
os.chdir('D:\Courses\Coursera\Python\course2\week-5')
#name = input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
name="mbox-short.txt"
counts=dict()
list_hours=list()
handle = open(name)
for lines in handle:
    lines=lines.lower()
    if lines.startswith('from ') is True:
        #print(lines)
        words=lines.split()
        #print(words)
        time_data=words[5]
        #print(time_data)
        time_split=time_data.split(":")
        #print(time_split)
        time_hour=time_split[0]
        #print(time_hour)
        counts[time_hour]=counts.get(time_hour,0)+1
#print(counts)
for k, v in counts.items():
    list_hours.append((k,v))
    list_hours.sort()
#print(list_hours)

for k,v in list_hours:
    print(k,v)




