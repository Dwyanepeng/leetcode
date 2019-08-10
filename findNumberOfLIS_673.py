#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : findNumberOfLIS_673.py
# Author: PengLei
# Date  : 2019/5/29
'''给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。'''

class Solution:
    def findNumberOfLIS(self, nums):
        max_L = [nums[0]]
        len_nums = len(nums)
        i = 0
        while i < len_nums:
            if nums[i] > max_L[-1]:
                max_L.append(nums[i])
            i += 1
        return max_L

s = Solution()
print(s.findNumberOfLIS([1,3,5,4,7]))