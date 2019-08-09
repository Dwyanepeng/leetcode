#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 9:16
# @Site    : 
# @File    : integerBreak_343.py
# @Software: PyCharm
'''给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
'''
# 这又是一个递归解决问题的思路，然后和前面一样，我们通过发现递归问题中具有重叠子问题，所
# 以我们使用动态规划自下而上的解决问题。
# 理解了上面分解的思路实际上问题就非常简单了，还有一点需要注意的是，有可能不一定需要分
# 解，比如3 * sums(2) 和 3 * 2 ,明显前者是3而后者是6，所以这种情况是不用继续向下分的。所以
# 考虑这个情况进去即可，在求max的时候加入即可。

class Solution:
    def integerBreak(self, n):
        sums = [0,1]
        for i in range(2, n+1):
            tmp = 0
            for j in range(1, i):
                tmp = max(tmp, j*sums[i-j], j*(i-j))
            sums.append(tmp)
            # print(sums)
        return sums[n]
    #令dp[i]表示整数i对应的最大乘积，那么dp[i]的值应是dp[j]*(i-j),j属于[1,i-1]的最大值，
    # 同时注意dp[i]对应的值是经过拆分了的，所以还应判断两个数拆分的情况，即j*(i-j)的值，取最大即可。
    def integerBreak1(self, n):
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(i-1, 0, -1):
                dp[i] = max(dp[i], dp[j]*(i-j))
                dp[i] = max(dp[i], j*(i-j))
        return dp[n]

s = Solution()
print(s.integerBreak1(4))