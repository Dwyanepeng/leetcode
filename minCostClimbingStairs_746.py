#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 10:34
# @Site    : 
# @File    : minCostClimbingStairs_746.py
# @Software: PyCharm
'''数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
 示例 2:

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
注意：

cost 的长度将会在 [2, 1000]。
每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
'''

#到达当前台阶时判断下从前一个台阶过来省体力，还是从前一个的前一个过来省体力，一直累加到最后一个台阶完，最小值就是最省体力的。
# 用p1和p2表示前两个和前一个台阶所耗费的体力，一遍循环就可以了。
class Solution:
    def minCostClimbingStairs(self, cost):
        cost.append(0)
        dp1, dp2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp1, dp2 = dp2, cost[i] + min(dp1, dp2)
        return dp2

s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))
