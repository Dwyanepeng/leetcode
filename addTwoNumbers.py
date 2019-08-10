#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : addTwoNumbers.py
# Author: PengLei
# Date  : 2019/3/23

def addTwoNums(a, b):
    sum1 = 0
    sum2 = 0
    for i in range(len(a)):
        sum1 += a[i] * (10 ** i)
        # print(sum1)
    for j in range(len(b)):
        sum2 += b[j] * (10 ** j)
        # print(sum2)

    return sum1+sum2


# def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
#     ln1 = []
#     ln2 = []
#     while l1 or l2:
#         ln1.append(l1.val) if l1 else 0
#         ln2.append(l2.val) if l2 else 0
#         if l1:l1 = l1.next
#         if l2:l2 = l2.next
#
#     str1 = []
#     str2 = []
#
#     for v in ln1:
#         # 插入到指定位置0
#         str1.insert(0, str(v))
#     for w in ln2:
#         str2.insert(0, str(w))
#     a = ''.join(str1)
#     b = ''.join(str2)
#     c = str(int(a)+int(b))
#     res = []
#     807转成708
#     for v in c:
#         res.insert(0, int(v))
#     return res

# addTwoNums((2->4->3),(4->6->5))
print(addTwoNums([2,4,3], [5,6,4]))