# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:37:59 2017

@author: prade
"""

import urllib.request as url
from bs4 import BeautifulSoup as bs
# Test Link
#url_link = "http://python-data.dr-chuck.net/comments_42.html"
# Actual Link
url_link = "http://python-data.dr-chuck.net/comments_285995.html"
url_conn = url.urlopen(url_link)
url_data = url_conn.read()
url_soup_obj = bs(url_data,'html.parser')
span_element=url_soup_obj("span")
sum = 0
for item in span_element:
    data = item.text
    sum = sum + int(data)
    #print('class>>>',item.get('class',None)) # this is used to print the attributes inside a html tag
    #print('Contents>>>',item.content[1])
    #print('Attrs>>>>',item.attrs) # Provised attribute value in a dictionary format
print(sum)



