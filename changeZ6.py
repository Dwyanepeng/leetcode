#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : changeZ6.py
# Author: PengLei
# Date  : 2019/3/30
'''Z字形变换'''

print(16//(2*3-2)*(3-2+1)+16%(2*3-2))
print(int(16//(2*5-2)*(5-2+1)+(16-(5+5-2)*(16//(2*5-2)))/5))
# print([4*[0]]*3)
# lie = int(len(s)//(2*numRows-2)*(numRows-1)+(len(s)-(2*numRows-2)*(len(s)//(2*numRows-2)))/numRows)
class Solution:
    def changeZ(s, numRows):
        lie = int(len(s) // (2 * numRows - 2) * (numRows - 1) + (len(s) - (2 * numRows - 2) * (len(s) // (2 * numRows - 2))) / numRows)
        a = [lie*[0]]*numRows
        for i in range(len(a)):
            for j in range(len(a[0])):
                if i % 2 == 0:

        return len(a[0])

print(Solution.changeZ('LEETCODEISHIRING', 3))
