# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:35:33 2017

@author: xuwh
"""
import sys  
import os
import time
from numpy import *
import cPickle as pickle
#数据文件转矩阵
# path: 数据文件路径
# delimiter: 文件分隔符
def file2matrix(path,delimiter):	
	recordlist = []
	fp = open(path,"rb") 	# 读取文件内容
	content = fp.read()
	fp.close()
	rowlist = content.splitlines() 	# 按行转换为一维表
	# 逐行遍历
	# 结果按分隔符分割为行向量	
	recordlist =[ row.split(delimiter) for row in rowlist if row.strip()]
	return mat(recordlist)	                           # 返回转换后的矩阵形式	
root = "D:\\Python\\test\\dataset"                    # 数据文件所在路径，里面包含转义字符
pathlist = os.listdir(root)                           # 获取路径下所有数据文件
recordmat = [file2matrix(root+"/"+path,"\t") for path in pathlist]  #文件到矩阵的转换

file_obj = open(root+"/recordmat.dat", "wb")
pickle.dump(recordmat[0],file_obj)                    # 将生成的矩阵对象保存到指定的位置
file_obj.close()

read_obj = open(root+"/recordmat.dat", "rb")
readmat = pickle.load(read_obj)                    # 从指定位置读取对象
print shape(readmat)

#for path in pathlist:
#   recordmat = file2matrix(root+"/"+path,"\t")
#   print shape(recordmat)