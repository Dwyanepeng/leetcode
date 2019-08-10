#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :findKthLargest_215.py
# Author: PengLei
# Date  : 2019/6/26

'''寻找数组中第k大的数'''
def quickSort(number):
    if len(number) <= 1: #必须有
        return number
    length = len(number)
    pivot = number[int(length / 2)]
    left = [x for x in number if x < pivot]
    middle = [x for x in number if x == pivot]
    right = [x for x in number if x > pivot]
    return quickSort(left) + middle + quickSort(right)
# print(quickSort([3,2,3,1,2,4,5,5,6]))

class Solution:
    def findKthLargest(self, nums, k):
        number = quickSort(nums)
        return number[-k]

s = Solution()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6],4))