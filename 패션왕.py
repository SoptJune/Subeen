#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 21:32:02 2022

@author: kimsubin
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda x: sys.stdout.write(str(x) + "\n")

t = int(input()) 

for i in range(t):
    n = int(input()) 
    clothes = {} # 개수, 타입 저장위해 딕셔너리로
    
    for j in range(n):
        count,types= input().split()
        #종류별로 분류
        if types not in clothes.keys():
            clothes[types] = 1
        else:
            clothes[types] += 1
    
    result = 1
    
    for i in clothes: #key값
        result *= (clothes[i]+1) #전체 경우의 수(상/하의 안입은 경우 포함)
    print(result-1) #상/하의 모두 안입었을 때