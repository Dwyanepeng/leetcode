#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : findMedianSortedArrays.py
# Author: PengLei
# Date  : 2019/3/25
# print(2/2)
class Solution:
    def findMedianSortedArrays(nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        a = []
        if m == 0 and n != 0:
            if len(nums2) % 2 == 0:
                z = (nums2[int(len(nums2) / 2)-1] + nums2[int(len(nums2) / 2)]) / 2
            else:
                z = nums2[len(nums2) // 2]
        if n == 0 and m != 0:
            if len(nums1) % 2 == 0:
                z = (nums1[int(len(nums1) / 2)-1] + nums1[int(len(nums1) / 2)]) / 2
            else:
                z = nums1[len(nums1) // 2]
        else:
            while i < m and j < n:
                if nums1[i]<nums2[j]:
                    a.append(nums1[i])
                    i += 1
                else:
                    a.append(nums2[j])
                    j += 1
            if i == m:
                a.extend(nums2[j:])
                # a.append(nums2[j:])
            if j == n:
                a.extend(nums1[i:])
                # a.append(nums1[i:])
            if len(a)%2 == 0:
                z = (a[int(len(a)/2)-1]+a[int((len(a)/2))])/2
            else:
                z = a[len(a)//2]
        # return a
        return z

print(Solution.findMedianSortedArrays([0,2],[9,10]))