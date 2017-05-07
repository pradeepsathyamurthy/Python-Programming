# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 18:55:25 2016

@author: prade
"""

# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.pythonlearn.com/code/words.txt
import os
os.chdir("D:\Courses\Coursera\Python\course2\week-2")

fname = input("Enter the file name:::")
fhandle = open(fname)
print(fhandle)
for lines in fhandle:
    up_case=lines.upper()
    up_case=up_case.rstrip()
    print(up_case)
fhandle.close()

# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: 
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce 
# an output as shown below. Do not use the sum() function or a variable named sum in your solution. 
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt 
# as the file name.

fname = input("Enter the file name: ")
fh = open(fname)
count=0
summation=0
avg=0
for lines in fh:
    lines = lines.rstrip()
    if(lines.startswith("X-DSPAM-Confidence:")):
        float_index = lines.find(":")
        float_value = lines[float_index+1:]
        float_value = float_value.strip()
        float_value = float(float_value)
        summation = summation+float_value
        count=count+1
        print(float_value)
print(summation)
print(count)
avg=summation/count
print(avg)
