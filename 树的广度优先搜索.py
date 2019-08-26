#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 11:38
# @Site    : 
# @File    : 树的广度优先搜索.py
# @Software: PyCharm

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return root
        queue = []
        result = []

        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result