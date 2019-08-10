#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :preorderTraversal_144.py
# Author: PengLei
# Date  : 2019/7/20
'''给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #递归
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        t = []
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    #迭代
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            if cur.right:
                res.append(cur.right)
            if cur.left:
                res.append(cur.left)
        return res

