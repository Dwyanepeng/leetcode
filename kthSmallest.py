#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :kthSmallest.py
# Author: PengLei
# Date  : 2019/7/10

#378 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。请注意，它是排序后的第k小元素，而不是第k个元素。

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        L = []
        for i in range(n):
            for j in range(n):
                L.append(matrix[i][j])
        L.sort()
        return L[k-1]

s = Solution()
print(s.kthSmallest([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],3))