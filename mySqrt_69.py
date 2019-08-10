#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :mySqrt_69.py
# Author: PengLei
# Date  : 2019/7/4

#获取平方不大于x的数，二分
class Solution:
    def mySqrt(self, x):
        if x == 0:
            return x
        if x == 1:
            return x
        if x == 2:
            return 1
        m = x
        n = 0
        s = 1
        ans = 1
        while m - n >= 1:
            s = (m+n) / 2
            # print('s', s)
            if int(s) * int(s) > x and int(s-1) * int(s-1) <=x:
                return int(s-1)
            elif int(s-1) * int(s-1) > x:
                m = s
                n = n
                # ans = n
                # print('n', n)
            elif int(s) * int(s) <= x:
                m = m
                n = s
                # print('m', m)

s = Solution()
print(s.mySqrt(8))

