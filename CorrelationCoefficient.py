# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:52:45 2017
求取相关系数

@author: xuwh
"""

from numpy import *

featuremat = mat([[38,65,79,85,67,56],[14,7,22,56,77,90]])

#计算均值
mv1 = mean(featuremat[0]) #第一列均值
mv2 = mean(featuremat[1]) #第二列均值

#计算两列的标准差
dv1 = std(featuremat[0])
dv2 = std(featuremat[1])
corref = mean(multiply(featuremat[0] - mv1,featuremat[1]-mv2))/(dv1*dv2)
print corref
#使用NumPy相关系数得到相关系数矩阵
print corrcoef(featuremat)