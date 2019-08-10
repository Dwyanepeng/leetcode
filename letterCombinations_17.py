#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :letterCombinations_17.py
# Author: PengLei
# Date  : 2019/8/3
'''17. Letter Combinations of a Phone Number
Medium


2404

321

Favorite

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].'''
#回溯法电话号码问题
import itertools

class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return None
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 1:
            return list(dic[digits])
        chars = [dic.get(d) for d in digits]
        tmp = [[]]
        for pool in chars:
            tmp = [x+[y] for x in tmp for y in pool]
        result = list()
        for prod in tmp:
            result.append(''.join(prod))
        return result

    def letterCombinations1(self, digits):
        if not digits:
            return []

        l_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        chars = [l_map.get(d) for d in digits]
        return [''.join(x) for x in itertools.product(*chars)]

if __name__ == '__main__':
    digits = input()
    s = Solution()
    print(s.letterCombinations1(digits))

