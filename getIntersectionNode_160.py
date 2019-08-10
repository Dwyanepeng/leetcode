#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :getIntersectionNode_160.py
# Author: PengLei
# Date  : 2019/7/7

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        countA = 1
        countB = 1
        pA = headA
        pB = headB
        while pA.next != None:
            pA = pA.next
            countA += 1
        while pB.next != None:
            pB = pB.next
            countB += 1
        if pA != pB:
            return None
        if countA < countB:
            countA,countB = countB,countA
            headA, headB = headB, headA
        for _ in range(countA-countB):
            headA = headA.next
        while headA !=headB:
            headA = headA.next
            headB = headB.next
        return headA

s = Solution()
print(s.getIntersectionNode([4,1,8,4,5], [5,0,1,8,4,5]))