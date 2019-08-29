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
    
mean = sum(array) / len(array)
sd = np.std(array)

normalized_array = [(i-mean)/sd for i in array]

mean2 = sum(array2) / len(array2)
sd2 = np.std(array2)

normalized_array2 = [(i-mean2)/sd2 for i in array2]

plt.title("Normalized of x[n]")
plt.stem(normalized_array , '--')

plt.title("Normalized of y[n]")
plt.stem(normalized_array2 , '--')









