#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : lengthOfLIS.py
# Author: PengLei
# Date  : 2019/5/29
'''给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?'''


# DP动态规划，定义状态dp[i]为以nums[i]为结尾且必须包含nums[i]本身的最长上升子序列的长度。
# 两个嵌套的循环，状态转移方程dp[i] = max(dp[i], dp[j] + 1)即在内层循环内通过比较dp[j]来
# 不断迭代dp[i]，找到前面最大的一个dp值然后加1。最后dp数组的最大值就是问题的解
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                # print(dp)
        return max(dp)


s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))

# max = 0
# for i in range(len(nums)):
#     max_L = [nums[i]]
#     for j in range(i, len(nums)):
#         if nums[j] > max_L[-1]:
#             max_L.append(nums[j])
#         print(max_L)
#     if len(max_L) > max:
#         max = len(max_L)
# return max
