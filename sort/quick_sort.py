#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 16:19
# @Site    : 
# @File    : quick_sort.py
# @Software: PyCharm
# 平均：O(nlogn) 最坏：O(n^2) O(1) 不稳定   n比较大好
def quick_sort(nums, start, end):
    if start >= end:
        return None
    low = start
    high = end
    piv = nums[start]
    while low < high:
        while low < high and nums[high] >= piv:
            high -= 1
        nums[low] = nums[high]

        while low < high and nums[low] < piv:
            low += 1
        nums[high] = nums[low]
        nums[low] = piv
    quick_sort(nums, start, low-1)
    quick_sort(nums, low+1, end)

    return nums

def quick_sort1(nums):
    if len(nums) <= 1:
        return nums
    piv = nums[0]
    left = [x for x in nums if x < piv]
    middle = [x for x in nums if x == piv]
    right = [x for x in nums if x > piv]
    return quick_sort1(left) + middle + quick_sort1(right)


print(quick_sort([54,26,93,15,77,3,44,55,20], 0, 8))
print(quick_sort1([54,26,93,15,77,3,44,55,20]))
