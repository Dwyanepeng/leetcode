#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :findLHS_594.py
# Author: PengLei
# Date  : 2019/7/16
'''和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

示例 1:

输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
说明: 输入的数组长度最大不超过20,000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-harmonious-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

from collections import Counter

class Solution:
    #超时
    def findLHS(self, nums):
        L = list(set(nums))
        double = []
        for i in range(len(L)):
            for j in range(len(L)):
                if L[i]-L[j] == 1:
                    double.append(sorted([L[i], L[j]]))
        L1 = []
        for k in range(len(double)):
            L1.append([])
            min = double[k][0]
            max = double[k][1]
            for m in range(len(nums)):
                if nums[m] >= min and nums[m] <= max:
                    L1[k].append(nums[m])
        max_L = []
        for num in L1:
            if len(num) >= len(max_L):
                max_L = num
        return len(max_L)

    def findLHS1(self, nums):
        num_counter = Counter(nums)
        res = 0
        for i in num_counter:
            if i+1 in num_counter:
                res = max(res, num_counter[i]+num_counter[i+1])
        return res



s = Solution()
print(s.findLHS1([1,3,2,2,5,2,3,7]))