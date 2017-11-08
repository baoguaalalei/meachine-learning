# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:40:16 2017

@author: xuwh
"""

from numpy import *  
import time  
import matplotlib.pyplot as plt  
import types
import k_means  
## step 1: load data  
print("step 1: load data...")  
dataSet = []  
fileIn = open(r'D:\Python\MachineLearningInAction\testSet.txt')  
for line in fileIn.readlines(): 
    lineArr = line.strip().split()   
    #print lineArr[0],lineArr[1]
    #dataSet.append([float(lineArr[0]),float(lineArr[1])])  
    dataSet.append([float(lineArr[0])])

print("step 2: clustering..." ) 
#这里使用mat将dataSet数据转换为矩阵之后才能进行线性代数操作
dataSet = mat(dataSet)  
k = 4  
centroids, clusterAssment = k_means.kmeans(dataSet, k)  
  
# step 3: show the result  
print("step 3: show the result...")  
#plt.plot()
k_means.showCluster(dataSet, k, centroids, clusterAssment)  