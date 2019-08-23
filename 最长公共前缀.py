#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :最长公共前缀.py
# Author: PengLei
# Date  : 2019/8/22


def maxlong(a):
    if not a:
        return ""
    a1 = min(a)
    a2 = max(a)
    # print(a1,a2)
    for i,x in enumerate(a1):
        if x != a2[i]:
            return a2[:i]
    return a1

n = int(input())
s = []
for i in range(n):
    s.append(str(input()))

li = list(map(int, input().split(' ')))
print(len(maxlong([s[li[0]-1], s[li[1]-1]])))
















# def longestCommonPrefix(strs):
#     if not strs: return ""
#     ss = list(map(set, zip(*strs)))
#     res = ""
#     for i, x in enumerate(ss):
#         x = list(x)
#         if len(x) > 1:
#             break
#         res = res + x[0]
#     return res
#
# print(longestCommonPrefix(['abcdefg','acdef']))
#
#
# def longestCommonPrefix1(strs):
#     if not strs: return ""
#     s1 = min(strs)
#     s2 = max(strs)
#     for i, x in enumerate(s1):
#         if x != s2[i]:
#             return s2[:i]
#     return s1
#
# print(longestCommonPrefix1(['abcdefg','acdef']))
