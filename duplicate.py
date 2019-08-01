#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 9:46
# @Site    : 
# @File    : duplicate.py
# @Software: PyCharm
'''找出列表中的重复数字
从头扫到尾，只要当前元素值与下标不同，就做一次判断,numbers[i]与 numbers[numbers[i]]，
相等就认为找到了重复元素，返回 true,否则就交换两者，继续循环。直到最后还没找到认为没找到重复元素。
'''

class Solution:
    def duplicate(self, nums):
        if not nums:
            return False
        set = []
        dup = {}
        for index, num in enumerate(nums):
            if num not in set:
                set.append(num)
            else:
                dup[index] = num
        return dup.values()

k = int(input('请输入数组长度：'))
nums = []
for i in range(k):
    print('请输入第',i+1,'个数')
    num = int(input())
    nums.append(num)
s = Solution()
print(s.duplicate(nums))


