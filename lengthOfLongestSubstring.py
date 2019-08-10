#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : lengthOfLongestSubstring.py
# Author: PengLei
# Date  : 2019/3/24

def lengthOfLongestSubstring(s):
    ss = []
    num = []
    max_n = 0
    for i in range(0, len(s)):
        if s[i] in ss:
            print('1', ss)
            # num.append(len(ss))
            index = ss.index(s[i])
            print('index', index)
            ss = ss[(index+1):]  #注意从当前重复的下一个字符开始
            # ss.clear()
            ss.append(s[i])
            print('ss', ss)
            if len(ss) >= max_n:
                max_n = len(ss)
            continue
        else:
            ss.append(s[i])
            # num.append(len(ss))
            if len(ss) >= max_n:
                max_n = len(ss)
            print(ss)
            # print(num)
    # print(num)1
    # return max(num)
    return max_n
print(lengthOfLongestSubstring('pwwkew'))