#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4_15_1.py
# Author: PengLei
# Date  : 2019/4/15
'''数组中出现频率最高的K个数
问题描述：
给定一个n个数的数组（n <= 10,000,000），以及一个数字k，请输出：数组中出现最频繁的k个数。

例如：数组[2,3,1,5,2,1,2,4,3,2,3]， k=3出现最频繁的数分别是2和3（2出现4次，3出现3次），其次是1（出
现2次） 所以输出1,2,3这3个数即可，输出顺序随意。

问题分析：
方法基本有两个：

（1）用hash统计出现次数，然后根据次数进行排序，输出结果即可。

（2）用hash统计出现次数，然后使用堆处理，输出结果即可。'''

from collections import defaultdict
import heapq

# 1
class Solution:
    def findFrequentlyK(self, A, k):
        counts = defaultdict(int)  # 所有值被初始化为0
        for x in A:  # 计数统计
            counts[x] += 1
        print(counts)
        if len(counts) <= k:
            return list(counts.keys())

        res = sorted(counts.items(), key=lambda x:x[1], reverse=True)  # 排序输出
        print('res', res)
        return [x[0] for x in res[:k]]

# 2
class Solution1:
    def findFrequentlyK(self, A, k):
        counts = defaultdict(int)  # 所有值被初始化为0
        for x in A:  # 计数统计
            counts[x] += 1
        if len(counts) <= k:
            return list(counts.keys())

        res = heapq.nlargest(k, counts.items(), key=lambda x: x[1])  # 从堆中找出最大的K个数

        return [x[0] for x in res]

if __name__ == '__main__':
    solu = Solution()
    A, k = [2, 3, 1, 5, 2, 1, 2, 4, 3, 2, 3], 10
    A, k = [2, 3, 1, 5, 2, 1, 2, 4, 3, 2, 3], 3
    print(solu.findFrequentlyK(A, k))

    solu1 = Solution1()
    print(solu1.findFrequentlyK(A, k))
