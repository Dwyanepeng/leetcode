#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : myAtoi8.py
# Author: PengLei
# Date  : 2019/4/2
'''请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，qing返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。'''
class Solution:
    def myAtoi(str: str) -> int:
        if len(str)==0:
            return 0
        i=0
        while i<len(str) and str[i]==' ':
            i+=1
        if i<len(str):
            l=[]
            if (str[i] in ['+','-']) or str[i].isnumeric():#判断第一个是否为正负号或者数字
                l.append(str[i])
                i+=1
                while i<len(str) and str[i].isnumeric():#如果是数字就一直添加到list里面
                    l.append(str[i])
                    i+=1
                if l[0] in ['+','-']:#可能list里面只有一个正负号
                    if len(l)>1:#判断一下还有数字
                        x=int(''.join(l))
                    else:
                        return 0
                else:
                    x=int(''.join(l))
                if x>2**31-1:
                    return 2**31-1
                elif x<-2**31:
                    return -2**31
                else:
                    return x
            else:
                return 0
        else:
            return 0

print(Solution.myAtoi('    -2321 3131 qeqeqw'))