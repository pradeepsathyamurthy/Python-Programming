# -*- coding: utf-8 -*-
"""
Created on Fri May 26 00:52:02 2017

@author: prade
"""

import urllib.request as url
from bs4 import BeautifulSoup as bs
url_link = "http://python-data.dr-chuck.net/known_by_Fikret.html"
url_conn = url.urlopen(url_link)
url_raw_data = url_conn.read()
#print(url_raw_data)
url_soup = bs(url_raw_data,"html.parser")
a_link = url_soup('a')
#print(a_link)
for item in a_link:
    #print(item)
    name=item.text
    print(name)
