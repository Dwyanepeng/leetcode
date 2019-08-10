#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : addBigNums.py
# Author: PengLei
# Date  : 2019/3/25
print('1', 10//10)
class Solution:
    def addBigNum(a, b):
        if len(a) > len(b):
            for k in range(len(a)-len(b)):
                b.insert(0, 0)
        if len(a) < len(b):
            for k in range(len(b)-len(a)):
                a.insert(0, 0)
        res = [0] * (max(len(a), len(b))+1)
        i = len(a)-1
        j = len(b)-1
        while i >= 0 or j >= 0:
            if a[i] + b[j] >= 10:
                res[i + 1] += (a[i] + b[j]) % 10
                print(res[i+1])
                res[i] += 1
                i -= 1
                j -= 1
            else:
                res[i + 1] += (a[i] + b[j])
                i -= 1
                j -= 1
        if res[0] == 0:
            res = res[1::]
        # return ''.join(res)
        return res
        # if i < 0:
        #     res


print(Solution.addBigNum([0],[0]))
