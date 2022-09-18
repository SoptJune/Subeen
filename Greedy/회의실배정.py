#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 23:24:34 2022

@author: kimsubin
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda x: sys.stdout.write(str(x) + "\n")

n = int(input())
room = [list(map(int, input().split()))for _ in range(n)]

room.sort(key = lambda x: (x[1], x[0]))

count = 0
result = 0

for i , j in room:
    if result <= i:
        result = j
        count+=1

print(count)
        