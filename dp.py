#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 8:58
# @Site    : 
# @File    : dp.py
# @Software: PyCharm

'''最长递增子序列'''
class Solution:
    def lengthofLIS(self, nums):
        length = len(nums)
        dp = [1] * length
        i = 0
        while i < length:
            j = 0
            while j < i:
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                j += 1
            i += 1
        return max(dp)

s = Solution()
print(s.lengthofLIS([10,9,2,5,3,7,101,18]))
print(s.lengthofLIS([1,4,3,4,2]))
