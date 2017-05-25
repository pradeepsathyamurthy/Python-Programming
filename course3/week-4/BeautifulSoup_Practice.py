# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:11:36 2017

@author: prade
"""
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib.request as u
from bs4 import BeautifulSoup
url = input('Enter - ')
html = u.urlopen(url).read()
soup = BeautifulSoup(html,"lxml")
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print (tag.get('href', None))
