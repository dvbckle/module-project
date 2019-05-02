# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:15:41 2019

@author: dvbckle
"""
#RoboGarden Create Basic Module Mission

def f_count(itemList): #count the number of elements in the list
    count = 0
    for item in itemList:
        count+=1
    return count
    
    
def f_sum(itemList): #calculate the sume of the items in the list
    numSum = 0
    for item in itemList:
        numSum+=float(item)
    return numSum
    
    
def f_average(itemList):  #calculate the average of the list
    numAvg = f_sum(itemList)/f_count(itemList)
    return numAvg
    
    
def f_max(itemList):  #Find the maximum in the list
    numMax = float(itemList[0])
    for item in itemList:
        if float(item) > numMax:
            numMax = float(item)
    return numMax
    
    
def f_min(itemList):  #Find the minimum in the list
    numMin = float(itemList[0])
    for item in itemList:
        if float(item) < numMin:
            numMin = float(item)
    return numMin
    
# Tests run to validate functions
#I_list = [1,2,-5,6,19,10]
#
#print("my test list is: ",I_list)
#print("number of items in the list is: ",f_count(I_list))
#print("sum of the items in the list is: ",f_sum(I_list))
#print("average of the items in the list is: ",f_average(I_list))
#print("the maximum of items in the list is: ",f_max(I_list))
#print("the minimum of items in the list is: ",f_min(I_list))
