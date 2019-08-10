#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :twoSum_167.py
# Author: PengLei
# Date  : 2019/6/26

'''两数之和'''
class Solution:
    def twoSum(self, numbers, target):
        hash = {}
        for i, num in enumerate(numbers):
            another = target - num
            if another in hash:
                return [hash[another]+1, i+1]
            hash[num] = i

s = Solution()
print(s.twoSum([2,7,11,15], 9))
