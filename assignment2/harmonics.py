# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
Bahadır Güray Özgödek
150150013
'''

import matplotlib.pyplot as plt
import numpy as np
import sys

def find_cn(n,w):
    cn = (np.sin(n*w*3/2) / (n*w*3/2)) * (np.sin(n*w*1/2) / (n*w*1/2))
    return 15/8*cn

def plot_x1(w,h):
    t = np.linspace(-10,10,1000)
    x = []
    for i in t:
        sum=0
        for j in range(1,2*h+1,2):
            sum += ((1/j*np.sin(j*w*i)))
        x.append(5/2 + 10/np.pi*sum)

    plt.plot(t-2,x)
    plt.show()

def plot_x2(w,h):
    t = np.linspace(-10,10,1000)
    xt = []
    for i in t:
        sum=0
        for j in range(1,h+1):
            sum += 2*find_cn(j,w)*np.cos(j*w*i)
        xt.append(c0 + sum)
    plt.plot(t,xt)
    plt.show()


c0 = 5*3/8
w = 2*np.pi*1/8

if sys.argv[1] == "x1":
    plot_x1(w, int(sys.argv[2]))
    
elif sys.argv[1] == "x2":
    plot_x2(w, int(sys.argv[2]))





