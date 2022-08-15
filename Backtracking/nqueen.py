#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 22:25:17 2022

@author: kimsubin
"""

import sys

input = lambda: sys.stdin.readline().rstrip()
write = lambda x: sys.stdout.write(str(x) + "\n")

# 열 , 대각선 검사
def check(row, col):
    for i in range(1, row):
        if graph[i] == col or abs(graph[i] - col) == row - i:
            return False

    return True


# queen 놓기
def nqueen(row):
    global result

    if row == n + 1:
        result += 1
        return

    for col in range(1, n + 1):
        if check(row, col):
            graph[row] = col
            nqueen(row + 1)
    return

n = int(input())
graph = [0 for _ in range(n + 1)]
result = 0
nqueen(1)
write(result)