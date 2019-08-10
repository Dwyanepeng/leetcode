#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :findBottomLeftValue_513.py
# Author: PengLei
# Date  : 2019/7/20

'''给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1
 

示例 2:

输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        d = {}
        def f(root, i):
            if root:
                d[i] = root.val
                f(root.right, i+1)
                f(root.left, i+1)
        f(root, 0)
        return list(d.values())[-1]
