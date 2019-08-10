#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  :isBipartite_785.py
# Author: PengLei
# Date  : 2019/7/30
'''图'''
class Solution:
    def isBipartite(self, graph):
        a, b = set([]), set([])
        d = {True: a, False: b}
        flag = True
        visited = set([])
        for i in range(len(graph)):
            if i in visited: continue
            stack = [(i, flag)]
            while stack != []:
                k, flag = stack.pop()
                visited.add(k)
                d[flag].add(k)
                flag = not flag
                for v in graph[k]:
                    if v not in visited:
                        stack.append((v, flag))
                    if v in d[not flag]:
                        return False
        return True

    def isBipartite1(self, graph):
        # kids can be found using idx of list
        ln = len(graph)
        visited = [False] * ln
        color = [0] * ln  # 0 == not visited, 1 = red, -1 = green
        print('visited', visited)
        print('color', color)
        for idx, g in enumerate(graph):
            if visited[idx]:
                continue
            q = [idx]
            print('q', q)
            color[idx] = 1
            visited[idx] = True  # if we set this later then we are adding lot of visited childs, so better
            # to set visited first
            while len(q) > 0:
                parent = q.pop(0)
                print('parent', parent)
                kids = graph[parent]
                print('kids', kids)
                for kid in kids:
                    if color[kid] == color[parent]:
                        print(color[kid])
                        print(color[parent])
                        return False

                    if not visited[kid]:
                        color[kid] = -color[parent]
                        q.append(kid)
                        visited[kid] = True

        return True

s = Solution()
print(s.isBipartite1([[1],[0,3],[3],[1,2]]))