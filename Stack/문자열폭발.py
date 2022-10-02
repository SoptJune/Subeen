#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:45:13 2022

@author: kimsubin
"""

import sys
input = lambda: sys.stdin.readline().strip() # 양쪽 공백 제거
print = lambda x: sys.stdout.write(str(x) + "\n")

strings = input()
bomb = list(input())
length = len(bomb)

stack = []
for i in strings:
    stack += i
    
    if stack[-length:] == bomb:
        for _ in range(length):
            stack.pop()

    
print(''.join(stack)) if stack else print("FRULA")
