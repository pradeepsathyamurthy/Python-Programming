# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 09:57:04 2017

@author: prade
"""

lst1 = list()
key = None
count_val = None
a = [31,100]
b = [32,100]
c = [32,100]
d = [33,300]
e = [33,500]
f = [34,400]
lst1.append(a)
lst1.append(b)
lst1.append(c)
lst1.append(d)
lst1.append(e)
lst1.append(f)
print(lst1)
for lst_ele in lst1:
    #print(lst_ele)
    key1=lst_ele[0]
    val1=lst_ele[1]
    if key == key1:
        count_val += val1
    else:
        if key:
            print(key,count_val)
        key = key1
        count_val = val1
print(key,count_val)
