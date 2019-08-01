#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 10:04
# @Site    : 
# @File    : bubble_sort.py
# @Software: PyCharm
class Solution:
    def bubble_sort(self, nums):
        length = len(nums)
        for i in range(length-1):
            for j in range(length-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

s = Solution()
print(s.bubble_sort([757,5,4,77,3,545,2,2,1]))

