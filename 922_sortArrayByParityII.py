#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :922_sortArrayByParityII.py
# Author: PengLei
# Date  : 2019/8/19
'''给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

 

示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
 

提示：

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        n1 = []
        n2 = []
        nums = [0]*n
        for i in range(n):
            if A[i] % 2 == 0:
                n1.append(A[i])
            else:
                n2.append(A[i])
        for j in range(n):
            if j % 2 == 0:
                nums[j] = n1.pop()
            else:
                nums[j] = n2.pop()
        return nums

s = Solution()
print(s.sortArrayByParityII([4,2,5,7]))

class Solution1:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ji = [i for i in A if i % 2]
        ou = [i for i in A if not i % 2]
        print('j', ji)
        print('o', ou)
        # >> > a = [1, 2, 3]
        # >> > b = [4, 5, 6]
        # >> > c = [4, 5, 6, 7, 8]
        # >> > zipped = zip(a, b)  # 打包为元组的列表,zip(*zipped)为解压，[(1,2,3),(4,5,6)]
        # 输出: [(1, 4), (2, 5), (3, 6)]
        for n in zip(ou, ji):
            print(n)
        return [i for n in zip(ou, ji) for i in n]

s1 = Solution1()
print(s1.sortArrayByParityII([4,2,5,7]))

class Solution2:
    def sortArrayByParityII(self, A):
        n = len(A)
        a,b = 0,1
        while a < n or b < n:
            if a < n and A[a] % 2 == 0:
                a += 2
                continue
            if A[b] % 2 == 1:
                b += 2
                continue
            else:
                A[a],A[b] = A[b],A[a]
        return A

s2 = Solution2()
print(s2.sortArrayByParityII([1,2,6,7]))

class Solution3:
    def sortArrayByParityII(self, A):
        n = len(A)
        nums = [0]*n
        ou, ji = 0, 1
        for i in range(n):
            if A[i] % 2 == 0:
                nums[ou] = A[i]
                ou += 2
            else:
                nums[ji] = A[i]
                ji += 2
        return nums

s3 = Solution3()
print(s3.sortArrayByParityII([1,2,6,7]))
