# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:45:02 2017

@author: xuwh
#2017/10/30
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

training_set = np.array([[[3,3],1],[[4,3],1],[[1,1],-1]])
a = np.zeros(len(training_set),np.float)
b = 0.0
Gram = None
y = np.array(training_set[:,1])
x = np.empty((len(training_set),2),np.float)
for i in range(len(training_set)):
    x[i] = training_set[i][0]
history = []

def cal_gram():
    """
    calculate the Gram matrix
    :return:
    """
    g = np.empty((len(training_set),len(training_set)),np.int)
    for i in range(len(training_set)):
        for j in range(len(training_set)):
            g[i][j] = np.dot(training_set[i][0],training_set[j][0])
            
    return g

def update(i):
    """
    update paramaters using stochastic gradient descent
    :param i:
    :return:    
    """
    global a,b
    a[i] += 1
    b = b + y[i]
    history.append([np.dot(a*y,x),b])
    print(a,b) # you can uncomment this line to check the process of stochastic gradient descent
    
# calculate the judge condition
def cal(i):
    global a,b,x,y
    res = np.dot(a*y,Gram[i])
    res = (res + b)*y[i]
    return res

def check():
    global a,b,x,y
    flag = False
    for i in range(len(training_set)):
        if cal(i)<=0:
            flag = True
            update(i)
    if not flag:
        w = np.dot(a*y,x)
        print("Result: w:"+ str(w)+"b:"+str(b))
        return False
    return True

if __name__=="__main__":
    Gram = cal_gram() # initialize the Gram matrix
    for i in range(1000):
        if not check():break   
   