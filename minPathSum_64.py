#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :minPathSum_64.py
# Author: PengLei
# Date  : 2019/8/7
'''Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
最小路径和
对于网格中的元素 ,从最上角的元素 走到它的最短距离为： ][j] 因此，这题的思路是：首先计算出第一行从左到右的步 数。
然后从第二行开始，采用动态规划的方法。事实上，我们只需要维护一个一维dp数组即可，这个数组代表走到对应行的每个位置
的最短路径。当更新某位置dp[j] 的时候只需要上方路径信息dp[j]（可以看作从上向下一遍一遍访问矩阵，更新dp，那么此时
的dp[j]由于还未更新，所 以是上方位置的路径信息）和左侧路径信息dp[j-1]即可，所以dp数组可以不断的覆盖，而不需要维
护二维dp数组'''

class Solution:
    def minPathSum(self, grid):
        r, c = len(grid), len(grid[0])
        dp = [0]*c
        for i in range(r):
            for j in range(c):
                if j == 0:
                    dp[j] = dp[j]
                    print('111')
                elif i == 0:
                    dp[j] = dp[j-1]
                    print('222')
                else:
                    dp[j] = min(dp[j], dp[j-1])
                    print('333')
                dp[j] += grid[i][j]
                print(dp)
        return dp[c-1]

s = Solution()
print(s.minPathSum([
  [1,3,1,3],
  [1,5,1,3],
  [4,2,1,5]
]))