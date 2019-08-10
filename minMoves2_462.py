#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :minMoves2_462.py
# Author: PengLei
# Date  : 2019/7/13

'''给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。

例如:

输入:
[1,2,3]

输出:
2

说明：
只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）：

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]'''

#相遇问题， 不用考虑奇偶数了
class Solution:
    def minMoves2(self, nums):
        nums = sorted(nums)
        length = len(nums)
        times = 0
        center_num = nums[length//2]
        # print('center_num', center_num)
        for i in range(0,length//2):
            times += center_num - nums[i]
        for j in range(length//2+1,length):
            times += nums[j] - center_num
        # for i in range(le    ngth):
        #     times += abs(center_num - nums[i])
        return times
s = Solution()
print(s.minMoves2([6,5,4,3,2,1]))