# -*- coding: utf-8 -*-
'''
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
'''
#敏感词语list
path = '\path\to\filtered_words.txt'
filtered_words = []
with open(path, 'path') as file:
    for line in file.readlines():
        filtered_words.append(line.strip())  #使用strip()去除空格，取出每一行的单词。#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。语法str.strip([chars])
        
        
input = raw_input("输入单词：")

if word in input:
   print("Freedom")
else:
   print("Human Rights")
