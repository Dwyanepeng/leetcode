#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :convertToBase7_504.py
# Author: PengLei
# Date  : 2019/7/13
#十进制数转成7进制
'''示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"'''

class Solution:
    def convertToBase7(self, num):
        n = 1
        s = ''
        if num > 0:
            while num != 0:
                n = num
                num = n // 7
                s += str(n - num*7)
                # print(num)
            return s[::-1]
        elif num < 0:
            num = -num
            while num != 0:
                n = num
                num = n // 7
                s += str(n - num*7)
            return '-' + s[::-1]
        else:
            return str(0)


s = Solution()
print(s.convertToBase7(7))