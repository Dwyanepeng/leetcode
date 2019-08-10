#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :longestPalindrome_409.py
# Author: PengLei
# Date  : 2019/7/9

#最长回文序列
class Solution:
    def longestPalindrome(self, s):
        res = 0
        flag = 0
        if len(set(s)) == 1:
            return s.count(s[0])
        for i in set(s):
            if s.count(i)%2 == 0:
                res += s.count(i)
            else:
                res += s.count(i) - 1
                flag = 1
        return res + flag

s =Solution()
print(s.longestPalindrome('ab'))