#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :最长连续公共子数组.py
# Author: PengLei
# Date  : 2019/8/22
'''链接：https://www.nowcoder.com/questionTerminal/b1112516673e463c9ed8943ae96e53f6
来源：牛客网

给出两个字符串（可能包含空格）,找出其中最长的公共连续子串,输出其长度。

输入描述:
输入为两行字符串（可能包含空格），长度均小于等于50.


输出描述:
输出为一个整数，表示最长公共连续子串的长度。
示例1
输入
abcde
abgde
输出
2'''


def max_arrays(nums1, nums2):
    dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
    # print(dp)
    res = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            res = max(res, dp[i+1][j+1])
    return res

nums1 = str(input())
nums2 = str(input())

print(max_arrays(nums1,nums2))



s1 = input()
s2 = input()
dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
print(dp)
maxl = 0
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        maxl = max(maxl, dp[i+1][j+1])
print(maxl)