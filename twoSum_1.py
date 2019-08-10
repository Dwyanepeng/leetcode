#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :twoSum_1.py
# Author: PengLei
# Date  : 2019/7/7

#求无序数组中两个数之和为target的位置
class Solution:
    def twoSum(self, nums, targrt):
        map = {}
        for index, num in enumerate(nums):
            other_num = targrt - num
            if other_num in map:
                return [map[other_num], index]
            map[num] = index

s = Solution()
print(s.twoSum([3,3], 6))
