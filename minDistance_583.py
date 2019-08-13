#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 16:37
# @Site    : 
# @File    : minDistance_583.py
# @Software: PyCharm
'''给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例 1:

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
说明:

给定单词的长度不超过500。
给定单词中的字符只含有小写字母。'''
#LCS 最长公共子序列
#构建dp数组，
# 行列相交元素相等，dp[i][j]=dp[i-1][j-1]+1
# 不相等,dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# 获得LCS需要反推
class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return m + n - 2 * dp[m][n]

