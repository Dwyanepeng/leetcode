#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :1.py
# Author: PengLei
# Date  : 2019/8/22

'''waimai,dache,lvyou,liren,meishi,jiehun,lvyoujingdian,jiaopei,menpiao,jiudian
waimai,menpiao,meishi,lvyoujingdian,lvyou,liren,jiudian,jiehun,jiaopei,dache'''
s = str(input())
ss = s.split(',')
# print(ss)

sort = sorted(ss,reverse=True)

print(','.join(sort))

print([1,2,3,4,5][1::2])