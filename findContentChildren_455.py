#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :findContentChildren_455.py
# Author: PengLei
# Date  : 2019/6/29

#贪心分配饼干问题，每个孩子我都有一个贪心因子g i，这是孩子满意的cookie的最小尺寸; 每个cookie j的大小为s j。如果s j > = g i，
# 我们可以将cookie j分配给孩子i，孩子我将满足。您的目标是最大化内容子项的数量并输出最大数量。

class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        satisfied = 0
        while s and g:
            if s[-1] < g[-1]:
                g.pop()
            else:
                satisfied += 1
                s.pop()
                g.pop()
        return satisfied

s = Solution()
print(s.findContentChildren([1,2,3], [1,1]))
print(s.findContentChildren([1,2], [1,2,3]))
