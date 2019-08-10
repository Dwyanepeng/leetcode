#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : twoSum.py
# Author: PengLei
# Date  : 2019/5/13
'''求有序数组中等于target的两个数的位置'''
class Soultion:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
            print(hashmap)
        return None

    def twoSum1(self, nums, target):
        i = 0
        j = len(nums) - 1
        while i != j:
            sum = nums[i] + nums[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                return [i+1, j+1]

s = Soultion()
print(s.twoSum([3,4,5,2,6], 10))
