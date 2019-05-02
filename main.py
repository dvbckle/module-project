# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:15:41 2019

@author: dvbckle
"""
#RoboGarden Create Basic Module Mission
from list_math import *                       #import math module

sample_list = [1,2,5,7,10,45,-23,10]

# run example functions from list_math

print("my test list is: ",sample_list)
print("number of items in the list is: ",f_count(sample_list))
print("sum of the items in the list is: ",f_sum(sample_list))
print("average of the items in the list is: ",f_average(sample_list))
print("the maximum of items in the list is: ",f_max(sample_list))
print("the minimum of items in the list is: ",f_min(sample_list))
