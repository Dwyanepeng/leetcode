#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :topKFrequent.py
# Author: PengLei
# Date  : 2019/6/27

#出现频率最高的k个数
class Solution:
    def topKFrequent(self, nums, k):
        dic = {}
        length = len(nums)
        if length == 1:
            return nums
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        dic = sorted(dic.items(), key=lambda d:d[1], reverse=True)
        # list = [v for v in sorted(dic.values())]
        list = []
        for i in range(k):
            list.append(dic[i][0])
        return list

s = Solution()
print(s.topKFrequent([4,1,-1,2,-1,2,3], 2))