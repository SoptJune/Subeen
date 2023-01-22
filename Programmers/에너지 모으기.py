#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:49:54 2023

@author: kimsubin
"""

n = int(input())
arr = list(map(int, input().split()))
MAX = 0

def solution(arr,m):
    global MAX
   
    
    if(len(arr) == 2):#맨앞,뒤만 남았을 때 
        MAX = max(MAX,m)
        return
    else:
        for i in range(1,len(arr)-1):
            r =arr[i-1] * arr[i+1]
            solution(arr[:i] + arr[i+1:], m + r)

solution(arr,MAX)

print(MAX)
