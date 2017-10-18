# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:36:59 2017

@author: xuwh

"""
import sys
import os
import jieba
from numpy import *

def savefile(savepath,content): #保存至文件 
    fp = open(savepath,"wb")
    content = bytes(content,encoding = "utf8")  
    fp.write(content)
    fp.close()
    
def readfile(path):
    fp = open(path,"rb")
    content = fp.read()
    fp.close()
    return content

#corpus_path = "D:\\Python\\test\\dataset"                   #未分类语料库路径
corpus_path = "D:\\Python\\demo\\chapter02\\train_corpus_small\\"
#seg_path = "D:\\Python\\demo\\chapter02\\train_corpus_seg\\art" 
seg_path = "D:\\Python\\demo\\chapter02\\train_corpus_seg\\"                     #分词后分类语料库的路径
catelist = os.listdir(corpus_path) #获取corpus_path下的所有子目录

#获取每个目录下所有的文件
for mydir in catelist:
    class_path = corpus_path + mydir + "\\" #拼出分类子目录的路径
    seg_dir = seg_path + mydir +"\\"        #拼出分词后语料分类目录
    if not os.path.exists(seg_dir):        #是否存在目录，如果没有则创建
        os.makedirs(seg_dir)               
    file_list = os.listdir(class_path)     #获取分类目录下的所有文件
    
for file_path in file_list:                      #遍历类别目录下文件
    fullname = class_path + file_path            #拼出文件名全路径
    content = readfile(fullname).strip()         #读取文件内容
    print(type(content))
    content = content.decode()
    print(type(content))    
    content = content.replace("\r\n","").strip() #删除换行和多余空格
    content_seg = " ".join(jieba.cut(content))             #为文件内容分词
    print (content_seg) # 不知为什么没有显示
    savefile(seg_dir+file_path," ".join(content_seg))   #将处理后的文件保存到分词后语料目录 

print ("中文语料分词结束")  
    