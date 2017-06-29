# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:38:08 2017

@author: prade
"""

import urllib.request as urlreq
from bs4 import BeautifulSoup
URL_address = 'http://electives.us/unilistims.html'
url_content = urlreq.urlopen(URL_address).read()
# Creating a soup object
soup  = BeautifulSoup(url_content,'html.parser') # This is a html parser
soup2  = BeautifulSoup(url_content,'lxml') # This is a lxml parser

soup.head # Will parse only the head tag
soup.body # will parse the body tag
soup.title # Will parse the title tag from the soup objectappend
soup.a # this will just parse the first <a> tag from the soup object
# To get all the <a> tags from the soup object
soup.find_all('a') # this will get all the <a> tags from the soup object

# Parsing the tags within <head> tags
head_tag = soup.head
head_tag_contents = head_tag.contents # this will create a list object by ignoring all HTML tags
len(head_tag.contents)

# there is no use of parsing data in a form of list
p_tags = soup.find_all('p') # This will again create a list object with all <p> tag and its elements
type(p_tags) # this will be a bs4 object and hence need to be type casted to list object
p_list = list(p_tags)
# To parse the tags further we need to use Regular Expressions
import re
# sample_string = '<p><span class="Greentext"><strong>Application fee:</strong></span> $100 , <span class="Greentext"><strong>Tuition fee:</strong></span> $2000/4week,<span class="Greentext"> <strong>Accomodation:</strong></span> NA ,<span class="Greentext"><strong>USMLE Step1:</strong></span> Req (will accept Step 2 CK or German Physikum as substitute), <span class="Greentext"><strong>TOEFL:</strong></span>Req (will accept alternatives) <span class="Greentext"><strong>Malpractice Insurance: </strong></span>NA <span class="Greentext"><strong>Immunization:</strong></span> TB,MMR,VZ,HBV,DPT , <span class="Greentext"><strong>Health Insurance :</strong></span>Req </p>'
# re.findall('USMLE .*?,',sample_string)
for items in p_list:
    items = str(items)
    href_data = re.findall('href=.*?>',items)
    USMLE_data = re.findall('USMLE .*?,',items)
    if len(href_data) !=0 or len(USMLE_data) !=0:
        print(href_data, USMLE_data)
