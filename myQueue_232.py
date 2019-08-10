#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :myQueue_232.py
# Author: PengLei
# Date  : 2019/7/7

#两个栈实现队列操作
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    #进队列
    def push(self, node):
        self.stack1.append(node)
    #出队列
    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return "Queue is empty!"
        # 在pop前，先将stack1中的数据清空放入stack2（保存后入的在栈底），stack1始终用于push
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop(-1))
        return self.stack2.pop(-1)

    def peek(self):
        # return self.stack1[0]
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop(-1))
        return self.stack2[-1]
    def empty(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False