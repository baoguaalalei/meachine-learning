# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:47:52 2017

@author: xuwh
"""
from numpy import *
import operator
import numpy as np
import sys
sys.path.append(r"C:\Users\xuwh")
##给出训练数据以及对应的类别
def createDataSet():
    group = np.array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
    labels = ['A','A','B','B']
    return group,labels

##通过KNN进行分类
def classify(input,dataSet,label,k):
    dataSize = dataSet.shape[0]
    ##计算欧氏距离
    diff = tile(input,(dataSize,1)) - dataSet
    sqdiff = diff**2
    squareDist = sum(sqdiff,axis = 1) ##行向量分别相加，从而得到一个新的行向量
    dist = squareDist**0.5
    
    ##对距离进行排序
    sortedDistIndex = argsort(dist) ##argsort()根据元素的值从大到小队元素进行排序，返回下标
    classCount = {}                 #创建的字典
    
    for i in range(k):
        voteLabel = label[sortedDistIndex[i]]  
        ###对选取的K个样本所属的类别个数进行统计
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1   #当字典的键值不存在时，值返回值定为0，在此刻增加1
    ###选取出现类别次数最多的类别
    maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key
            
    return classes


if __name__=="__main__":
    dataSet,labels = createDataSet()
    input = array([1.1,0.3])
    K = 3
    output = classify(input,dataSet,labels,K)
    print("测试数据为：",input,"分类数据为：",output)