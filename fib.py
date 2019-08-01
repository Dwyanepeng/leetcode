#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 9:17
# @Site    : 
# @File    : fib.py
# @Software: PyCharm

def fib(n):
    if n == 0:
        return 1
    if n == 1 :
        return 1
    if n == 2:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(5-1))