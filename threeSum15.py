#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : threeSum15.py
# Author: PengLei
# Date  : 2019/4/23
'''给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]'''

class Solution:
    #超时
    def threeSum(self, nums):
        s = []
        length = len(nums)
        nums.sort()
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sort = sorted([nums[i],nums[j],nums[k]])
                        if sort not in s:
                            s.append(sort)
        return s
    #通过
    def threeSum1(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        # print(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0:
                    tmp = [nums[i], nums[left], nums[right]]
                    res.append(tmp)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res

    # O(N^2)
    def threeSum2(self, nums):
        nums, r = sorted(nums), set()
        for i in [i for i in range(len(nums) - 2) if i < 1 or nums[i] > nums[i - 1]]:
            d = {-nums[i] - n: j for j, n in enumerate(nums[i + 1:])}
            r.update([(nums[i], n, -nums[i] - n) for j, n in enumerate(nums[i + 1:]) if n in d and d[n] > j])
        return list(map(list, r))

ss = Solution()
print(ss.threeSum([-1, 0, 1, 2, -1, -4]))
