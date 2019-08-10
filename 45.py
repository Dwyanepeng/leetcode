#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 45.py
# Author: PengLei
# Date  : 2019/4/15

class Solution:
    def jump(self, nums):
        result = reach = maxReach = 0
        for index, num in enumerate(nums):
            if index > reach:
                reach = maxReach
                result += 1
            maxReach = max(maxReach, index + num)
        print(maxReach)
        return result


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    solu = Solution()
    print(solu.jump(nums))