# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
import sys


com_list = [int(sys.argv[i]) for i in range(1,len(sys.argv))]

array = np.zeros(com_list[1]+1 , dtype=int )
array2 = np.zeros(com_list[1]+1 , dtype=int)
counter = 4

for j in range(com_list[0] , com_list[1]+1):
    array[j] = com_list[counter]
    counter += 1
    
for k in range(com_list[2] , com_list[3]+1):
    array2[k] = com_list[counter]
    counter += 1
    


plt.title("y[n]")
plt.stem(array2,'--')






