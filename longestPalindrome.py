#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : longestPalindrome.py
# Author: PengLei
# Date  : 2019/3/26

# s = 'cbbd'
# print(s[1:6])
'''最长回文数组'''

class Solution:
    def is_Palindrome(s):
        if s == s[::-1]:
            return True
    def longestPalindrome(s):
        p = ''
        p1 = ''
        i = 0
        n = len(s)
        if len(s) == 0 or len(s) == 1:
            return s
        for i in range(n):
            start = 0
            end = n - i
            while end <= n:
                sub_string = s[start:end]
                # print('sub', sub_string)
                if Solution.is_Palindrome(sub_string) is True:
                    return sub_string
                start += 1
                end += 1
        # while i < len(s):
        #     p += s[i]
        #     if p == p[::-1]:
        #         if len(p) > len(p1):
        #             p1 = p
        #     # print('p11', p1)
        #     # print('p', p)
        #     # print('p[::-1]', p[::-1])
        #     i += 1
        # if len(p1) == 1:
        #     s = s[1:]
        #     Solution.longestPalindrome(s)
        # return p1

    def longestPalindrome1(s):
        """
        :type s: str
        :rtype: str
        """
        cur_max = 0
        res = ""
        left = 0
        right = 0
        n = len(s)
        # 以i为回文中心
        for i in range(0, n):
            # 奇数
            left = i
            right = i
            # print(left,right)
            while left > 0 and right < n - 1 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            # print(left,right)
            if right - left + 1 > cur_max:
                cur_max = right - left + 1
                res = s[left:right + 1]
                print(res)
            # 偶数
            if i + 1 < n and s[i] == s[i + 1]:
                left = i
                right = i + 1
                # print(left,right)
                while left > 0 and right < n - 1 and s[left - 1] == s[right + 1]:
                    left -= 1
                    right += 1
                # print(left,right)
                if right - left + 1 > cur_max:
                    cur_max = right - left + 1
                    res = s[left:right + 1]
                    print(res)
        return res



print(Solution.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))