#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : reverseNum.py
# Author: PengLei
# Date  : 2019/4/1
'''给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321'''
# 看成字符串
class Solution:
    def reverseNum(x):
        if x == 0:
            return 0
        strX = str(x)
        xx = ''
        if strX[0] == '-':
            xx = '-'
            for i in range(len(strX)-1, 0, -1):
                xx += ''.join(strX[i])
            print('int(xx)', int(xx),type(int(xx)))
            if int(xx) < -(2 ** 31):
                return 0
            return int(xx)

        else:
            for i in range(len(strX)-1, -1, -1):
                xx += ''.join(strX[i])
            print('int(xx)', int(xx), type(xx))
            if int(xx) > (2 ** 31) -1:
                return 0
            return int(xx)
print(Solution.reverseNum(-123670))


# Python中的strip用于去除字符串的首尾字符，同理，lstrip用于去除左
# 边的字符，rstrip用于去除右边的字符。

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        str_x = str(x)
        x = ''
        if str_x[0] == '-':
            x += '-'
        x += str_x[len(str_x)-1::-1].lstrip("0").rstrip("-")
        x = int(x)
        if -2**31<x<2**31-1:
            return x
        return 0
