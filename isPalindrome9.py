#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : isPalindrome9.py
# Author: PengLei
# Date  : 2019/4/2
class Solution:
    def isPalindrome(x):
        strX = str(x)
        # print(strX)
        reveX = strX[len(strX)-1::-1]
        # print(reveX)
        if reveX == strX:
            return True
        else:
            return False

print(Solution.isPalindrome(-121))