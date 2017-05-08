# -*- coding: utf-8 -*-
"""
Created on Sat May  6 18:26:06 2017

@author: pradeep sathyamurthy
"""
"""
Regular Expression also called as regex or regexp
Itself is a programming language used to match string of text like character, words or pattern of characters
Normally written in a formal language (python here) which will be interpreted by the regex processor inside Python engine
It id defined as really clever "wild card" expression for matching and parsing strings

It is initially difficult to understand, but once learned it is fun to program

https://docs.python.org/3/library/re.html

"""
# Sample Regular expression
# Firt we need to import re package to RAM and then mostly make use of re.search() and re.findall() method
# re.search() = find() method in string operations
# re.findall() = find() + slicing method of string operation
# Generally re.search is used along with a if or any conditional statements
# However, re.findall an be used stand alone and provide list output
import re
str_1="My Name is Pradeep and my email id is pradeep_sathyamurthy@infosys.com"
if re.search('^M',str_1):
    print (str_1)

str_2="My score in the exam that i recently took was 21 and then 43 asn then i was given 34 and finally 100"
re.findall('[0-9]+',str_2) # this will list only the numbers in the particular string in a form of list
re.findall('[0-9]*',str_2) # this will list even non matching pattern and as well numbers in a form of list

# Some most used regular expressions, have this printed in office, no need to memorize and panic later that u forgot
"""
^        Matches the beginning of a line 
$        Matches the end of the line 
.        Matches any character 
\s       Matches whitespace 
\S       Matches any non-whitespace character 
*        Repeats a character zero or more times 
*?       Repeats a character zero or more times (non-greedy) 
+        Repeats a character one or more times 
+?       Repeats a character one or more times (non-greedy) 
[aeiou]  Matches a single character in the listed set 
[^XYZ]   Matches a single character not in the listed set 
[a-z0-9] The set of characters can include a range 
(        Indicates where string extraction is to start 
)        Indicates where string extraction is to end
"""

# Defining a string
str_3="My name is pradeep and my email id if pradeep_sathyamurthy@infosys.com. My score in GRE is 321 and spilt of 170 and 151 in quants and verbal respectively, oh mygod; there is a mist in the cloud where itis so good"

# testing all the regular expression above
# working of ^
# Based on line
# Look if any line starts with (^) a particulat Character or word mentioned
result1=re.search('^M',str_3) # it will not five a True/False result, it will provide a match object if matched
result2=re.search('^N',str_3) # when not matched no return object is found
result3=re.findall('^M',str_3) # this will provide a list output when matched
result4=re.findall('^N',str_3) # if not matched, it will provide an empty list
result5=re.search('^My',str_3) # we can also look for match with words too

# working of $ 
# Based on line
# look for any lines which ends with ($) a particular character or word mentioned
# be careful with its usgae, we are insiting python to check if a charcter ends with a string 'str1' 
# so we need to mention 'str1$' and not '$str1'
result1=re.search('y$',str_3) # it will not five a True/False result, it will provide a match object if matched
result2=re.search('N$',str_3) # when not matched no return object is found
result3=re.findall('y$',str_3) # this will provide a list output when matched
result4=re.findall('N$',str_3) # if not matched, it will provide an empty list
result5=re.search('respectively$',str_3) # we can also look for match with words too
print(result1, '\n',result2,'\n',result3,'\n',result4,'\n',result5)

# working of .
# this is called a wild card character
# . => matches any character
# Based on each word occurence in a string
# this is case sensitive
# Match any word which start with a character followed by a char or a empty space which ever is present in string
result1=re.search('My.',str_3) # it will not five a True/False result, it will provide a match object if matched
result2=re.findall('My.',str_3) # this will provide a list output when matched
result3=re.findall('my.',str_3) 
print(result1, '\n',result2,'\n',result3,'\n',result4,'\n',result5)

# working of \s
# it matches whitespace character
# will return any matching word starting wiht a soecific character taking whitespace also into account
# it almost work as '.' operator howwver there is a subtle difference
# \ => Either escapes special characters (permitting you to match characters like '*', '?', and so forth), or signals a special sequence; 
# Matches Unicode whitespace characters 
result1=re.search('My\s',str_3) # ths will return 'My ' wherever found, takes space followed by as OK
result2=re.findall('My\s',str_3)
result3=re.findall('my\s',str_3) 

# working of \S
# it works opposite to \s
# it does not matches whitespace character
# will return any matching word starting wiht a soecific character without taking whitespace also into account
result1=re.search('My\S',str_3) # this will not return anything as it 'My' is always followed by a space 
result2=re.findall('My\S',str_3)
result3=re.findall('my\S',str_3) # however 'mygod' is a word that starts with 'my' but not follwed by space so it get displays

# working of *
# greedy method
# repeats a character 0 or more times
result1=re.search('M*',str_3)
result2=re.findall('my*',str_3)

# working of *?
# non-greedy method
# repeats a character 0 or more times
result1=re.search('My*?',str_3)
result2=re.findall('my*?',str_3)

# working of +
# greedy method
# repeats a character 1 or more times
result1=re.search('M+',str_3)
result2=re.findall('my+',str_3)

# working of +?
# non-greedy method
# repeats a character 1 or more times
result1=re.search('M+?',str_3)
result2=re.findall('my+?',str_3)

# working of [aeiou]
# Matches a single character in the listed set
result1=re.search('[aeiou]',str_3)
result2=re.findall('[aeiou]',str_3)
result3=re.findall('[bcdfg]',str_3)

# working of [^XYZ]
# Matches a single character not in the listed set
result1=re.search('[^aeiou]',str_3)
result2=re.findall('[^aeiou]',str_3)
result3=re.findall('[^bcdfg]',str_3)

# working of [a-z0-9]
# The set of character can include a range
result1=re.search('[a-z0-9]',str_3)
result2=re.findall('[a-z0-9]',str_3)

# working of (
# Indicates where string extraction is to start
# working of )
# Indicates where string extraction has to end
result1=re.search('(is)',str_3)
result2=re.findall('(is)',str_3)

# using the re.search() method instead of find()
import re # need this import to use the regular expression in python
import os # used to set the current working directory
os.chdir('D:\Courses\Coursera\Python\course3\week-2')
file_handle=open('mbox-short.txt')
for lines in file_handle:
    lines=lines.strip()
    if re.search('From:',lines): #<- this will search for a line starting with 'From:' and print the same
        print(lines)
file_handle.close()

# using the re.search() method instead of startwith()
import re # need this import to use the regular expression in python
import os # used to set the current working directory
os.chdir('D:\Courses\Coursera\Python\course3\week-2')
file_handle=open('mbox-short.txt')
for lines in file_handle:
    lines=lines.strip()
    if re.search('^From:',lines): #<- this will search for a line starting with 'From:' and print the same
        print(lines)
file_handle.close()

# wild card characters
# . => matches any character
# * => any number of times
# using the re.search() method instead of startwith()
import re # need this import to use the regular expression in python
import os # used to set the current working directory
os.chdir('D:\Courses\Coursera\Python\course3\week-2')
file_handle=open('sample.txt')
for lines in file_handle:
    lines=lines.strip()
    if re.search('^X.*:',lines): #above line will search for a 
        #1. ^X <- line starting with 'X' 
        #2. . <- any character  
        #3. * <- zero or more (Multiple) times and print the same
        #4. : <- This once is optional for this program, having it here or not doesnt mater, that is X and : in above wild card statement has no meaning or they are just not the wild card characters
        print(lines)
file_handle.close()

# \S <- ignoring the white space
import re # need this import to use the regular expression in python
import os # used to set the current working directory
os.chdir('D:\Courses\Coursera\Python\course3\week-2')
file_handle=open('sample2.txt')
for lines in file_handle:
    lines=lines.strip()
    if re.search('^X-\S+:',lines): #above line will search for a 
        #1. ^X- <- line starting with 'X' 
        #2. \S <- no white space  
        #3. + <- One or more times
        #4. : <- This once is optional for this program, having it here or not doesnt mater, that is X- and : in above wild card statement has no meaning or they are just not the wild card characters
        print(lines)
file_handle.close()


# Matching and Extracting the data
# re.search() will retunr a true/false implicitly and hence normally get used with if statement
# re.findall() is used to find, match and extract a particular data
import re
x = 'My 2 favorite numbers are 19 and 42 And 32'
y = re.findall('[0-9]+',x) # <- This statement will
    #1. [0-9] <- look for a word that starts with number
    #2. + <- look for such word one or more times
    # Thus re wil find once that matches these, extract them and print for you
print(y)

z = re.findall('[AEIOU]+',x)
    #1. [AEIOU] <- look for a word which starts with A,E,I,O,U basically vovels
    #2. + <- look for one or more times and print the results
print(z)

# Greedy Matching
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
    #1. ^F <- Any word that starts with F
    #2. . <- Followed by any character
    #3. +  <- One or more times
    #4. : <- Only in re.search() ':' becomes optional for staring considered here. However for re.findall() we need to mentional the start and end point of our search
print(y)
# if see the o/p it doesnt stop printing 'From:' that is chr that starts with 'F' follwed by many char and end with ':'
# it will do a greedy search on whole line of text and thus try to extract if the pattern can be extended further and hence print 'From: Using the : character' as list()

# Non-Greedy Matching
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
    #1. ^F <- Any word that starts with F
    #2. . <- Followed by any character
    #3. +  <- One or more times
    #4. ? <- Non-greedy seach applied
    #4. : <- Only in re.search() ':' becomes optional for staring considered here. However for re.findall() we need to mentional the start and end point of our search
print(y)
# If you look at this o/p we will see python would do a non-greedy seach and get satisfied with first matching occurence. this is sometimes very useful

# Usage of paranthesis ()
# This helps in fine tuning the string extraction
x= "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('\S+@\S+',x)
    #1. \S <- Stop with white space
    #2. + <- Do it one or more times
    #3. @ <- this is not a wild card, we are telling ti find for @ with no space before and no space after by mentioning \S again
    #4. \S <- Stop with white space
    #5. + <- Do this one ot more time
# so what happens here is, puthon will first search for '@' and do a forward search to extract characters untill it see a space, becareful if you use \s instead of \S then u will consider white space too 
# once forward search is done, python will do backward search and stop when it faces a white space
# python now extract the data it has and print to the system
print(y)

# () are not part of actual wild cards, they just tell python as in where to start with wild card and where to stop it
# () they actaully mention where to start with the extraction
x= "From: stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('^From:.*? (\S+@\S+)',x)
    # 1. ^From: <- any line that starts with 'From:'
    # 2. . <- Follwed by a character
    # 3. * <- Follwed by a character 0 or more times
    # 4. ? <- do a Non-Greedy Search
    # 5. () <- Where to actually start the extraction
print(y)

# extracting only the domain name from email id
# this we can tradinionally do using find and split or double split command and slicing
# Instead we can implemen this as easily as possible using regex
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)
    #1. @ <- this is not a wild card, we insist python to seach for @ in a sring
    #2. ( <- mentioning the start of extraction
    #3. [^ ] <- Match non blank characters
    #4. * <- Do this multiple times
    #5. ) <- mentioning the stop of extraction
print(y)


import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',lin)
    #1. ^From <- Line which starts with From and a space
    #2. . <- Follwed by any charcter
    #3. * <- Followed by any charcter 0 or more times
    #4. @ <-Not a regex, mentioning regex to find '@' in a string
    #5. ( <- Ectration starts
    #6. [^ ] <- Match any non blank character
    #7. * <- Match any non blank character and do it 0 or more times
    #8. ) <- Extraction ends
print(y)


import re
import os # used to set the current working directory
os.chdir('D:\Courses\Coursera\Python\course3\week-2')
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    #1. ^X-DSPAM-Confidence: <- find lines that start with 'X-DSPAM-Confidence: '
    #2. ( <- Extraction starts
    #3. [0-9.] <- Any Number with a decimal point
    #4. + <- one ot more times
    print(stuff)
    print(len(stuff))
    if len(stuff) != 1 : continue # remember length of list starts from 1 and not 0
    num = float(stuff[0]) # Type casting from list to float
    numlist.append(num) # appending the list of values extracted using regex
print('Maximum:', max(numlist))

# print few regex keywords as return - use \
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
    #1. \$ <- Print $ as it is asd mentioning python not to consider this as a regex
    #2. [0-9.] <- Any decimal, that is any number followed by a decimal point .
    #3. + <- Do this one or more time
print(y)

#Quiz

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
    #1. \S <- No white space
    #2. + <- No white space 1 or more times
    #3. ? <- No greedy seach
    #4. @ <- find @
    #5. \S <- stop when white space found after @
    #6. + <- do step-5 one or more times
print(y)

# Week-2 assignment submission

# Practice Data
#Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt (There are 87 values with a sum=445822) 
import os
import re
os.chdir('D:\Courses\Coursera\Python\course3\week-2')
file_handle = open('regex_sum_42.txt')
num_list = list()
for lines in file_handle:
    #print(lines)
    lines = lines.strip()
    num = re.findall('[0-9]+',lines)
    #print(num)
    #print(len(num))
    if len(num) != 0:
        num_list.append(num)
#print(num_list)
sum_num=0
num_count=0
for i in num_list:
    for j in i:
        #print(j)
        j=int(j)
        num_count=num_count+1
        sum_num=sum_num+j
print("Num count is>>> ",num_count)
print("Sum is>>> ",sum_num)
file_handle.close()


# Actual Data
# Actual data: http://python-data.dr-chuck.net/regex_sum_285990.txt (There are 74 values and the sum ends with 297)
# I have implemented this assignment in python 3.5
# Author: Pradeep Sathyamurthy
# Date: 07-May-2017
import os
import re
os.chdir('D:\Courses\Coursera\Python\course3\week-2')
file_handle = open('regex_sum_285990.txt')
num_list = list()
for lines in file_handle:
    #print(lines)
    lines = lines.strip()
    num = re.findall('[0-9]+',lines)
    #print(num)
    #print(len(num))
    if len(num) != 0:
        num_list.append(num)
#print(num_list)
sum_num=0
num_count=0
for i in num_list:
    for j in i:
        #print(j)
        j=int(j)
        num_count=num_count+1
        sum_num=sum_num+j
print("Num count is>>> ",num_count)
print("Sum is>>> ",sum_num)
file_handle.close()


# Shorter version of it
# import re
# print(sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ))







































