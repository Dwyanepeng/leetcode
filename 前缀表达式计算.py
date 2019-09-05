#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :前缀表达式计算.py
# Author: PengLei
# Date  : 2019/8/29

s = str(input())

def solu(s):
    dig = []
    for i in range(len(s)-1, -1, -1):
        if s[i].isdigit():
            dig.append(s[i])
        # print(dig)
        if not s[i].isdigit():
            a = int(dig.pop())
            b = int(dig.pop())
            # print(a,b)
            if s[i] == '+':
                # print(dig)
                res = a + b
                dig.append(res)
            elif s[i] == '-':
                # print(dig)
                res = a - b
                dig.append(res)
            elif s[i] == '*':
                # print(dig)
                res = a * b
                dig.append(res)
            else:
                # print(dig)
                res = a / b
                dig.append(res)
    return res

print(solu(s))

