# -*- coding: utf-8 -*-
"""
Created on Fri May 26 00:52:02 2017

@author: pradeep sathyamurthy
"""

import urllib.request as url
from bs4 import BeautifulSoup as bs
#url_link = "http://python-data.dr-chuck.net/known_by_Fikret.html"
url_link = input('Enter URL:')
position = input('Enter position:')
position = int(position)
count = input('Enter count:')
count = int(count)
counter=1
while True:
    if(counter==count+2):
        break
    else:
        #print('counter>>>>',counter)
        print('Retrieving:', url_link,'\n')
        url_conn = url.urlopen(url_link)
        url_raw_data = url_conn.read()
        #print(url_raw_data)
        url_soup = bs(url_raw_data,"html.parser")
        a_link = url_soup('a')
        positions_link = a_link[position-1]
        #print(positions_link)
        final_url = positions_link.get('href',None)
        #print(final_url)
        url_link = final_url
        counter=counter+1
        continue
#print(final_url)