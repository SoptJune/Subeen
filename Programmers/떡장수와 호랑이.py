#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:32:13 2023

@author: kimsubin
"""

import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline


def dfs(day,food,yesterday):
    global flag
    if flag:
        return
    if day == n:
        for d in food:
            print(d)
        flag = True
        return
    for i in days[day][1:]:
        if not visited[day][i-1] and i != yesterday:
            visited[day][i-1] = True
            dfs(day+1, food + [i],i)

n = int(input())
flag = False
days = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*10 for _ in range(n+1)]

dfs(0,[],0)

if flag == False:
    print(-1)

        