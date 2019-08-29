# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
Bahadır Güray Özgödek
150150013
'''

import numpy as np
import math
import sys

def find_cn(n,w):
    cn = (np.sin(n*w*3/2) / (n*w*3/2)) * (np.sin(n*w*1/2) / (n*w*1/2))
    return 15/8*cn

def calculate_THD(list):
    err=0
    print(len(list))
    for i in range(1,15):
        err += math.pow(list[i],2)
    err = err/math.pow(list[0],2)
    return math.sqrt(err)


c0 = 5*3/8
w = 2*np.pi*1/8

if sys.argv[1] == "x1":
    t = np.linspace(-10,10,1000)
    x = []
    for i in t:
        sum=0
        for j in range(1,10,2):
            sum += ((1/j*np.sin(j*w*i)))
        x.append(5/2 + 10/np.pi*sum)
    print("THD for x1 = {}".format(calculate_THD(x)))
    
elif sys.argv[1] == "x2":
    t = np.linspace(-10,10,1000)
    xt = []
    for i in t:
        sum=0
        for j in range(1,6):
            sum += 2*find_cn(j,w)*np.cos(j*w*i)
        xt.append(c0 + sum)
    print("THD for x2 = {}".format(calculate_THD(xt)))
