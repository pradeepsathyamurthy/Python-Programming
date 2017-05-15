# -*- coding: utf-8 -*-
"""
Created on Sun May 14 23:23:33 2017

@author: prade
"""

import urllib.request as urllib
req = urllib.Request('http://data.pr4e.org/intro-short.txt')
res = urllib.urlopen(req)
print (res.info())
res.close();