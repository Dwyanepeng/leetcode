#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :majorityElement_169.py
# Author: PengLei
# Date  : 2019/7/13

#求数组众数
class Solution:
    def majorityElement(self, nums):
        d = {}
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = 0
                d[num] += 1
            else:
                d[num] += 1
        m = 0
        for j in d.values():
            if j > len(nums)/2:
                # return  list(d.keys())[list(d.values()).index(j)] #找到字典值对应的键
                new_d = {v:k for k,v in d.items()} #字典键值对翻转
                return new_d[j]

s = Solution()
print(s.majorityElement([3,2,3]))
