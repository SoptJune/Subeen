#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 22:25:17 2022

@author: kimsubin
"""

n = int(input())
graph = [0 for _ in range(n + 1)]
result = 0

# 열 , 대각선 검사
def check(graph, row, col):

    for i in range(1, row):
        if graph[i] == col:
            return False

    for i in range(1, row):
        if abs(graph[i] - col) == row - i:
            return False
        
    return True

#queen 놓기
def nqueen(graph, row, num):
    
    global result

    if row == num + 1:
        result += 1
        return
    
    for col in range(1, n + 1):
        if check(graph, row, col):
            graph[row] = col
            nqueen(graph, row + 1, num)
        else:
            continue

nqueen(graph, 1, n)
print(result)