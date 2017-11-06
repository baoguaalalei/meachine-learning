# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 17:12:41 2017
@author: xuwh
"""
import numpy as np
'''
创建数据集
'''
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    
    classVec = [0,1,0,1,0,1]            #1 is abusive, 0 not
    return postingList,classVec

#创建一个带有所有单词的列表
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)
    
def setOfWords2Vec(vocabList, inputSet):
    retVocabList = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            retVocabList[vocabList.index(word)] = 1
        else:
            print('word ',word ,'not in dict')
    return retVocabList

#将句子根据其中的单词转换成向量，这里用的是伯努利模型，也就是只考虑这个单词是否存在  
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

# 将句子转换成向量的另一种模型，多项式模型，考虑某个词出现的次数
def trainNB0(trainMatrix,trainCatergory):
    numTrainDoc = len(trainMatrix)                     #矩阵的整个大小
    numWords = len(trainMatrix[0])                     #单词的长度
    pAbusive = sum(trainCatergory)/float(numTrainDoc)  #垃圾邮件的平均值
    #防止多个概率的成绩当中的一个为0
    p0Num = np.ones(numWords)
    p1Num = np.ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDoc):
        if trainCatergory[i] == 1:
            p1Num +=trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num +=trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = np.log(p1Num/p1Denom)                      #处于精度的考虑，否则很可能到限归零
    p0Vect = np.log(p0Num/p0Denom)
    return p0Vect,p1Vect,pAbusive

#计算P(i)和P(w[i]C[1])和P(w[i]C[0])，这里有两个技巧，一个是开始的分子分母没有全部初始化为0.
#是为了防止其中一个概率为零导致整体为零，另一个是后面乘以对数防止因为精度问题结果为零
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + np.log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0
        
def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(np.array(trainMat),np.array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
        
def main():
    testingNB()
    
if __name__ == '__main__':
    main()