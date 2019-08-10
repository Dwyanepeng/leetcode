#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : maxArea.py
# Author: PengLei
# Date  : 2019/4/2

'''给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条
垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共
同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。'''

class Solution:
    # 暴力解法
    def maxArea(height):
        maxA = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
               if (j-i)*min(height[i], height[j]) > maxA:
                   maxA = (j-i)*min(height[i], height[j])
                   # print(maxA)
        return maxA

    # 动态规划
    def maxArea1(height):
        maxA = 0
        start = 0
        end = len(height) - 1
        while start < end:
            maxA = max(maxA, min(height[start], height[end]) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxA


print(Solution.maxArea1([1,8,6,2,5,4,8,3,7]))