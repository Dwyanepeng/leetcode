#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :kthSmallestTree_230.py
# Author: PengLei
# Date  : 2019/7/21
'''中序遍历二叉树'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        res = []
        self.visitNode(root, res)
        return res[k - 1]

    def visitNode(self, root, res):
        if root is None:
            return None
        self.visitNode(root.left, res)
        res.append(root.val)
        self.visitNode(root.right, res)

dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]

for featVec in dataSet:
    # index列为value的数据集【该数据集需要排除index列】
    # 判断index列的值是否为value
    print('featVec', featVec)
    print(featVec[0])
print(set([1,1,1,0,0]))

featVec = [0, 1, 'no']
print(featVec[:0])