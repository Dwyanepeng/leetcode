#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :longestPalindromeSubseq_516.py
# Author: PengLei
# Date  : 2019/8/15

'''给定一个字符串s，找到其中最长的回文子序列。可以假设s的最大长度为1000。

示例 1:
输入:

"bbbab"
输出:

4
一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:

"cbbd"
输出:

2
一个可能的最长回文子序列为 "bb"。
'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        lenx = len(s)
        r_x = s[::-1]
        if s == s[::-1]:
            return lenx
        # 注意生成数组方法,不能是[[0]*n]*n
        c = [[0] * int(lenx+1) for _ in range(lenx+1)]
        # i=0或j=0的行、列值为0
        for i in range(lenx):
            for j in range(lenx):
                if s[i] == r_x[j]:
                    c[i+1][j+1] = c[i][j] + 1
                else:
                    c[i+1][j+1] = max(c[i+1][j], c[i][j+1])
        print(c)
        return int(c[-1][-1])

s = Solution()
print(s.longestPalindromeSubseq('bbbab'))