# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy import *  
import time  
import matplotlib.pyplot as plt  
  
  
# calculate Euclidean distance  
def euclDistance(vector1, vector2):  
    return sqrt(sum(power(vector2 - vector1, 2)))  
  
# init centroids with random samples  
def initCentroids(dataSet, k):  
    numSamples, dim = dataSet.shape 
    #print "numSamples = %Ld,dim = %Ld\n" %(numSamples,dim)
    centroids = zeros((k, dim))  
    for i in range(k):  
        index = int(random.uniform(0, numSamples)) #random.uniform(x,y) x表示随机数的最小值，y表示随机数的最大值 
        print "index = %d" %index
        centroids[i, :] = dataSet[index, :]  #该处有疑问，为什么数据的赋值会应用到[index，：]，冒号的作用是什么
    return centroids  
  
# k-means cluster  
def kmeans(dataSet, k):  
    numSamples = dataSet.shape[0] #数据的条目数  
    # first column stores which cluster this sample belongs to, 第一行用于保存该数据属于第几簇
    # second column stores the error between this sample and its centroid  第二行用于保存距离核中心的距离
    clusterAssment = mat(zeros((numSamples, 2)))  
    #print clusterAssment
    clusterChanged = True    
    ## step 1: init centroids  
    centroids = initCentroids(dataSet, k)       
    while clusterChanged:  
        clusterChanged = False  
        ## for each sample  
        for i in xrange(numSamples):  
            minDist  = 100000.0  
            minIndex = 0  
            ## for each centroid  
            ## step 2: find the centroid who is closest 找到图心，归类
            for j in range(k):  
                distance = euclDistance(centroids[j, :], dataSet[i, :])                 
                if distance < minDist:  
                    minDist  = distance  
                    minIndex = j    
                    
            ## step 3: update its cluster 更新簇
            if clusterAssment[i, 0] != minIndex:  
                clusterChanged = True  
                clusterAssment[i, :] = minIndex, minDist**2  
        print clusterAssment
        ## step 4: update centroids  更新中心
        for j in range(k):  
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
            centroids[j, :] = mean(pointsInCluster, axis = 0)  
           #print centroids[j, :], "\n"  
    print 'Congratulations, cluster complete!'  
    return centroids, clusterAssment  
# show your cluster only available with 2-D data  
def showCluster(dataSet, k, centroids, clusterAssment):  
    numSamples, dim = dataSet.shape  
    if dim != 2:  
        print "Sorry! I can not draw because the dimension of your data is not 2!"  
        return 1  
  
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']  
    if k > len(mark):  
        print "Sorry! Your k is too large! please contact Zouxy"  
        return 1  
  
    # draw all samples  
    for i in xrange(numSamples):  
        markIndex = int(clusterAssment[i, 0])  
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])  
  
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']  
    # draw the centroids  
    for i in range(k):  
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)  
  
    plt.show()  