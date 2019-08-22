#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :背包问题canPartition_416.py
# Author: PengLei
# Date  : 2019/8/10

'''给定仅包含正整数的非空数组，查找是否可以将数组划分为两个子集，使得两个子集中的元素总和相等。

注意：

每个数组元素不会超过100。
阵列大小不会超过200。

例1：

输入：[1,5,11,5]

输出：true

说明：数组可以分区为[1,5,5]和[11]。


例2：

输入：[1,2,3,5]

输出：false

说明：无法将数组分区为相等的和子集。'''

#0-1背包
# [3,3,3,4,5]
#总容量为 22，可以把它看成一个背包总容量为11的背包问题。
# 所以我们可以初始化一个数组w，w[i]表示能不能将背包容量填充到i，比如w[5]表示是不是能够在背包中找到元素，
# 使得5被填满，显然是可以的。

class Solution:
    def canPartition(self, nums):
        c = sum(nums)
        if c & 0x1: #为奇数
            return False
        c = c // 2
        w = [False] * (c+1)
        w[0] = True #表示当元素出现的时候让w[i-num]为True,即w[i]为True
        print(w)
        for num in nums:
            for i in range(c, num-1, -1):
                w[i] = w[i] or w[i-num]
                print('i', i, w)
        return w[c]

s = Solution()
print(s.canPartition([3,3,3,4,5]))
print(s.canPartition([1,5,11,5]))




