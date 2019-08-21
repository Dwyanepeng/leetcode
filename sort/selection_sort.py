#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 11:51
# @Site    : 
# @File    : selection_sort.py
# @Software: PyCharm
# 选择排序 O(n^2) 不稳定
def selection_sort(nums):
    for i in range(len(nums)):
        min_i = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_i]:
                min_i = j
        nums[i], nums[min_i] = nums[min_i], nums[i]
    return nums

print(selection_sort([54,26,93,15,77,3,44,55,20]))