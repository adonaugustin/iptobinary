#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 18:51:28 2023

@author: adonaugustinn
"""


import subprocess
import re
import time

def glow_forone():
    print(1)
    time.sleep(.5)
def glow_forzero():
    print(0)
    time.sleep(.5)
def start():
    for i in range(5):
     print('*',"\n")
     time.sleep(.3)
     

result =str( subprocess.run(["ipconfig getifaddr en0"], shell=True, capture_output=True, text=True))
arrange_list=result.split(',')

ip_addr=[]
for i in arrange_list:
   if( i.__contains__('stdout')):
       ip=i.split('=')
       ip_addr=ip[1].split('\\')[0]
ip_addr_ind=ip_addr.split('.')

ox=[]
for i in range(4):
    ox.append(bin(int([int(x.group()) for x in re.finditer(r'\d+', ip_addr_ind[i])][0])))
start()
for y in ox:   
    for x in y[2:]:
      
        if (x=='1'): 
            glow_forone()
        if (x=='0'): 
            glow_forzero()
            




