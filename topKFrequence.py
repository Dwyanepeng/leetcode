#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 11:00
# @Site    : 
# @File    : topKFrequence.py
# @Software: PyCharm

nums = list(map(int, input().split(' ')))
K = int(input())

def topKFrequence(nums, K):
    map = {}
    for num in nums:
        if num in map.keys():
            map[num] += 1
        else:
            map[num] = 1
    print(map)
    if len(map) <= K:
        return list(map.keys())
    res = sorted(map.items(),key=lambda x:x[1], reverse=True)
    print(res)
    return [x[0] for x in res[0:K]]

print(topKFrequence(nums, K))



from collections import Counter
print(sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True))