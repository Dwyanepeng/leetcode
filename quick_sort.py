#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 10:15
# @Site    : 
# @File    : quick_sort.py
# @Software: PyCharm

def quick_sort(nums, first, last):
    if first >= last:
        return []
    mid_value = nums[first]
    low = first
    high = last
    while low < high:
        while low < high and nums[high] >= mid_value:
            high -= 1
        nums[low] = nums[high]

        while low < high and nums[low] < mid_value:
            low += 1
        nums[high] = nums[low]

        nums[low] = mid_value

    quick_sort(nums, first, low-1)
    quick_sort(nums, low+1, last)
    return nums


# if __name__ == '__main__':
#     l = [1, 2, 3, 4, 5, 55, 6, 3, 4, 5, 6]
#     quick_sort(l, 0, len(l) - 1)
#     print(l)
print(quick_sort([1, 2, 3, 4, 5, 55, 6, 3, 4, 5, 6], 0, 10))