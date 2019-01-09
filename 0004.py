# !/usr/bin/env python
# coding:utf-8
from collections import Counter


def letter_frequency(sentence):
    s_list = sentence.split()
    freq = {}
    for letter in s_list:
        frequency = freq.setdefault(letter, 0)
        freq[letter] = frequency + 1
    return freq


with open('0004.txt') as f:
    lines = f.readlines()
    dic = {}
    for line in lines:
        X, Y = Counter(dic), Counter(letter_frequency(line))
        dic = dict(X+Y)
    print(dic)
