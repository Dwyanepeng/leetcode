#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :maxArea_2.py
# Author: PengLei
# Date  : 2019/8/22

'''给定一组非负整数组成的数组h，代表一组柱状图的高度，其中每个柱子的宽度都为1。
在这组柱状图中找到能组成的最大矩形的面积（如图所示）。 入参h为一个整型数组，代表每个柱子的高度，返回面积的值。'''

n = int(input())
nums = list(map(int, input().split(' ')))

def maxArea(n, nums):
    maxA = 0
    for w in range(1, n+1):
        times = n - (w - 1) #窗口长度
        # print('times', times)
        for h in range(0,times):
            height = nums[h:h+w]
            # print(height)
            # print('min(height)', min(height))
            if min(height) * w > maxA:
                maxA = min(height) * w
    return maxA

print(maxArea(n, nums))
