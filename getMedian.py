#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 13:40
# @Site    : 
# @File    : getMedian.py
# @Software: PyCharm

# -*- coding:utf-8 -*-
'''找出数据流的中位数

答：对于一个升序排序的数组，中位数为左半部分的最大值，右半部分的最小值，而左右两部分可以是无序的，只要保证左半部分的数均小于右半部分即可。
因此，左右两半部分分别可用最大堆、最小堆实现。
如果有奇数个数，则中位数放在左半部分；如果有偶数个数，则取左半部分的最大值、右边部分的最小值之平均值。
分两种情况讨论： 当目前有偶数个数字时，数字先插入最小堆，然后选择最小堆的最小值插入最大堆（第一个数字插入左半部分的最小堆）。
当目前有奇数个数字时，数字先插入最大堆，然后选择最大堆的最大值插入最小堆。 最大堆：根结点的键值是所有堆结点键值中最大者，且每个结点的值都比其孩子的值大。 最小堆：根结点的键值是所有堆结点键值中最小者，且每个结点的值都比其孩子的值小。'''
from heapq import *

class Solution:
    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def Insert(self, num):
        if (len(self.maxheap) + len(self.minheap)) & 0x1:  # 总数为奇数插入最大堆, & 0x1相当于判断奇偶 %2 == 1
            if len(self.minheap) > 0:
                if num > self.minheap[0]:  # 大于最小堆里的元素
                    heappush(self.minheap, num)  # 新数据插入最小堆
                    heappush(self.maxheap, -self.minheap[0])  # 最小堆中的最小插入最大堆
                    heappop(self.minheap)
                else:
                    heappush(self.maxheap, -num)
            else:
                heappush(self.maxheap, -num)
        else:  # 总数为偶数 插入最小堆
            if len(self.maxheap) > 0:  # 小于最大堆里的元素
                if num < -self.maxheap[0]:
                    heappush(self.maxheap, -num)  # 新数据插入最大堆
                    heappush(self.minheap, -self.maxheap[0])  # 最大堆中的最大元素插入最小堆
                    heappop(self.maxheap)
                else:
                    heappush(self.minheap, num)
            else:
                heappush(self.minheap, num)

    def GetMedian(self, n=None):
        if (len(self.maxheap) + len(self.minheap)) & 0x1:
            mid = self.minheap[0]
        else:
            mid = (self.minheap[0] - self.maxheap[0]) / 2.0
        return mid


if __name__ == '__main__':
    s = Solution()
    s.Insert(1)
    s.Insert(2)
    s.Insert(3)
    s.Insert(4)
    print(s.GetMedian())