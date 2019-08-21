#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 11:14
# @Site    : 
# @File    : insertion_sort.py
# @Software: PyCharm

'''插入排序，平均时间复杂度O(n^2)'''
def insertion_sort(nums):
    for i in range(1, len(nums)):
        current_value = nums[i]
        position = i
        while position > 0 and nums[position-1] > current_value:
            nums[position] = nums[position-1]
            position -= 1
        nums[position] = current_value
    return nums

print(insertion_sort([54,26,93,15,77,3,44,55,20]))
