#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :numSquares_279.py
# Author: PengLei
# Date  : 2019/7/30
#DP
class Solution:
    def numSquares(self, n):
        dp = [1]+[0]*n
        for i in range(int(n**0.5),0,-1):
            s = i**2
            for j in range(len(dp)):
                if dp[j] and j+s < len(dp) and not 0 < dp[j+s] < dp[j] + 1:
                    dp[j+s] = dp[j]+1
        return dp[-1]-1

s = Solution()
print(s.numSquares(12))