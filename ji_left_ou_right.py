#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :ji_left_ou_right.py
# Author: PengLei
# Date  : 2019/8/19
class Solution:
    def ji_ou(self, nums):
        left = 0
        now = 0
        right = len(nums)-1
        while now <= right:
            if nums[now] % 2 == 1:
                # nums[now], now[left] = nums[left], nums[now]
                # now, left = now+1, left+1
                now += 1
                continue
            elif nums[now] % 2 == 0:
                nums[now], nums[right] = nums[right], nums[now]
                right -= 1
        return nums

s = Solution()
print(s.ji_ou([1,2,3,4,5,6,7,8,9,0]))

