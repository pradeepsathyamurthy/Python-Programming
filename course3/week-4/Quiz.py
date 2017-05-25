# -*- coding: utf-8 -*-
"""
Created on Wed May 24 20:46:13 2017

@author: prade
"""
# Question-1
import urllib.request as urllib
req = urllib.Request('http://www.py4inf.com/code/romeo.txt')
res = urllib.urlopen(req)
print (res)
res.close();

# Question-2
# In this Python code, which line actually reads the data?
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print (data)
mysock.close()


# Question-3
# Which of the following regular expressions would extract the URL from this line of HTML:
# <p>Please click <a href="http://www.dr-chuck.com">here</a></p>

import re
sample_txt="<p>Please click <a href=""http://www.dr-chuck.com"">here</a></p>"
href=re.findall("<.*>",sample_txt)
print(href)

#Question-8
import urllib.request as urllib
import BeautifulSoup
html = urllib.urlopen("http://www.dr-chuck.com/page1").read()
soup = BeautifulSoup(html)
x = soup('a')

