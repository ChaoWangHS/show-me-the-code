
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，
则变成「**是个好城市」。
#敏感词语list
path = r'C:\Users\ChaoWang\Desktop\TODO\python\code\filtered_words.txt'
filtered_words = []
with open(path, 'r') as file:
    for line in file.readlines():
        filtered_words.append(line.strip())  #使用strip()去除空格，取出每一行的单词。#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。语法str.strip([chars])
        
print filtered_words
input1 = raw_input('inputs words:')

input2 = input1.split(" ")

for i in input2:
    if i in filtered_words:
	   input1 = input1.replace(i, r'**')
print (input1)
