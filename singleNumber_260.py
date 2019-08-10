#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :singleNumber_260.py
# Author: PengLei
# Date  : 2019/7/10
#只出现一次的数，位运算
#给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
# 如果只出现一次的数只有一个，全部异或去最后一个值即可，acc ^= num，即为acc
#输入: [1,2,1,3,2,5]
#输出: [3,5]

class Solution:
    def singleNumber(self, nums):
        acc = 0
        for num in nums:
            acc ^= num #相等为0，不等为1
            # print(acc)
        n = len(bin(acc))-3
        # print('n', n)
        a,b = 0,0
        for i in nums:
            # print('dad', i >> n&1) #n=2
            # print('n&1', n&1)
            if i>>n &1:  #001,010,001,011,010,101分别右移两位，0,0,0,0,0,1,得到第一个出现一次的数
                a ^= i
            else:#剩下的为第二个，和一组数中全部异或即最后的值
                b ^= i
        return [a,b]

s = Solution()
print(s.singleNumber([1,3,2,1,2,5]))
