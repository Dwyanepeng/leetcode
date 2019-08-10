#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 16:57
# @Site    : 
# @File    : findBottomLeftValue_513.py
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root.val
        if self.height(root.left) >= self.height(root.right):
            return self.findBottomLeftValue(root.left)
        return self.findBottomLeftValue(root.right)

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def findBottomLeftValue1(self, root):
        d = {}

        def f(root, i):
            if root:
                d[i] = root.val
                f(root.right, i + 1)
                f(root.left, i + 1)

        f(root, 0)
        return list(d.values())[-1]


