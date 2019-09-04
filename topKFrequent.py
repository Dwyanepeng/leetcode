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
        # list = []
        # for i in range(k):
        #     list.append(dic[i][0])
        # print(dic)
        return [i[0] for i in dic[0:k]]
        # return list(dic[0::k][0])

s = Solution()
print(s.topKFrequent([1,2,2,2,2,3,3,4,4,4], 2))