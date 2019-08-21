#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 11:29
# @Site    : 
# @File    : binary_search_sort.py
# @Software: PyCharm

# def binary_search_sort(nums):
#     for i in range(1, len(nums)):
#         low = 0
#         high = i-1
#         current_value = nums[i]
#         position = i
#         while low <= high:
#             middle = (low+high) // 2
#             if nums[middle] > current_value:
#                 high = middle - 1
#             else:
#                 low = middle + 1
#             while position > low:
#                 nums[position] = nums[position-1]
#                 position -= 1
#             nums[low] = current_value
#         return nums
#
# print(binary_search_sort([54,26,93,15,77,3,44,55,20]))

def foo(l, k):
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] > k:
            right = mid - 1
        elif l[mid] < k:
            left = mid + 1
        elif l[mid] == k:
            return mid
    return -1


if __name__ == '__main__':
    l = [54,26,93,15,77,3,44,55,20]
    print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(foo(l, 8))  # 8