#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 9:53
# @Site    : 
# @File    : match.py
# @Software: PyCharm
'''匹配 . 和 * ,分别表示匹配任意一个字符，前一个字符出现任意次数'''

def isMatch(text, pattern) -> bool:
    if not pattern:
        return not text

    first = bool(text) and pattern[0] in {text[0], '*'}

    if len(pattern) >= 2 and pattern[1] == '.':
        return isMatch(text, pattern[2:]) or first and isMatch(text[1:], pattern)
    else:
        return first and isMatch(text[1:], pattern[1:])