#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 18:56
# @Site    : 
# @File    : qianxu_144.py
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#前序
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        s = []
        s.append(root)
        if not root:
            return lst
        while s:
            temp = s.pop()
            lst.append(temp.val)
            if temp.right:
                s.append(temp.right)
            if temp.left:
                s.append(temp.left)
        return lst

class Solution1:
    def preorderTraversal(self, root):
        # 0 表示当前遍历到它，1 表示压入栈
        # 刚开始是 1 ，不要写成 0 了
        stack = [(1,root)]
        s = []
        while stack:
            command, node = stack.pop()
            if node is None:
                # 不能写 return ，这不是递归
                continue
            if command == 0:
                s.append(node.val)
            else:
                # 此时 command == 1 的时候，表示递归遍历到的
                # 注意：写的时候倒过来写
                #注意和后序顺序不一样，stack需要pop
                stack.append((1, node.right))
                stack.append((1, node.left))
                stack.append((0, node))
        return s
