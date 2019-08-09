#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 17:06
# @Site    : 
# @File    : permutation.py
# @Software: PyCharm
'''数组全排列'''

class Solution:
    def permutation(self, nums):
        if len(nums) <= 1:
            return [nums]
        s = []
        for i in range(len(nums)):
            for j in self.permutation(nums[0:i]+nums[i+1:]):
                s.append(nums[i]+j)
        return s

s = Solution()
print(s.permutation('1234'))
