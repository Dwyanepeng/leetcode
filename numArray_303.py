#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 17:17
# @Site    : 
# @File    : numArray_303.py
# @Software: PyCharm
'''给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。
'''
class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
    def sumRange(self, i, j):
        return sum(self.nums[i:j+1])

nn = NumArray([-2, 0, 3, -5, 2, -1])
# nn.__init__()
print(nn.sumRange(0,2))
print(nn.sumRange(2,5))
print(nn.sumRange(0,5))

#数组区间的和
class NumArray1(object):
    def __init__(self, nums):
        self.nums = nums
        self.sums = []
        total = 0
        for n in nums:
            total += n
            self.sums.append(total)
        # print(self.sums)

    def sumRange(self, i, j):
        if i > 0:
            return self.sums[j] - self.sums[i-1]
        else:
            return self.sums[j]
nn1 = NumArray1([-2, 0, 3, -5, 2, -1])
print(nn1.sumRange(2,3))