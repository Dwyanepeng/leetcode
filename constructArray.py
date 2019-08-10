#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :constructArray.py
# Author: PengLei
# Date  : 2019/7/14

'''给定两个整数 n 和 k，你需要实现一个数组，这个数组包含从 1 到 n 的 n 个不同整数，同时满足以下条件：

① 如果这个数组是 [a1, a2, a3, ... , an] ，那么数组 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数；.

② 如果存在多种答案，你只需实现并返回其中任意一种.

示例 1:

输入: n = 3, k = 1
输出: [1, 2, 3]
解释: [1, 2, 3] 包含 3 个范围在 1-3 的不同整数， 并且 [1, 1] 中有且仅有 1 个不同整数 : 1
 

示例 2:

输入: n = 3, k = 2
输出: [1, 3, 2]
解释: [1, 3, 2] 包含 3 个范围在 1-3 的不同整数， 并且 [2, 1] 中有且仅有 2 个不同整数: 1 和 2
 

提示:

 n 和 k 满足条件 1 <= k < n <= 104.'''

#确定前k+1个数的排列
#规律：下标从[0, k]中，偶数下标填充[1,2,3…]，奇数下标填充[k + 1, k, k - 1…]，后面[k + 1, n - 1]都是顺序填充
class Solution:
    def constructArray(self, n, k):
        if k == 1:
            return list(range(1, n+1))
        else:
            a1 = list(range(2, n+1))
            a = [1]
            for i in range(k-1):
                if i%2 == 0:
                    a.append(a1[-1])
                    a1.pop(-1)
                else:
                    a.append(a1[0])
                    a1.pop(0)
            if k%2 != 0:
                return a+a1
            else:
                a1.reverse()
                return a+a1

    def constructArray1(self, n, k):
        a = list(range(1,n-k+1))
        t = 1
        while k >= 1:
            a.append(a[-1] + k*t)
            k -= 1
            t = -t
        return a

    def constructArray2(self, n, k):
        if n ==2:
            return [1,2]
        if n == 3 and k == 1:
            return [1,2,3]
        if n == 3 and k == 2:
            return [1,3,2]
        if k == 1:
            return list(range(1, n+1))
        a = []
        numK = k+1
        numTemp = 1
        for i in range(0, k+1):
            if i%2 == 0:
                a.append(numTemp)
                numTemp += 1

            else:
                a.append(numK)
                numK -= 1

        for j in range(k+1, n):
            a.append(j+1)
        return a

s = Solution()
print(s.constructArray2(14,4))