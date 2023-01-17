#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 22:15:21 2023

@author: kimsubin
"""


import sys
input = sys.stdin.readline
 
n = int(input())
m = int(input())

arr = []

parent = [i for i in range(n+1)]
 
 
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a) # 부모노드
    b = find(b) # 부모노드
    if a < b:  # 트리 길이가 긴 것이 부모노드 가져야함. 이때 음수면 절대값처럼 생각. -3 < -2 : a가 b보다 트리가 큼
       parent[b] = a 
    else:
       parent[a] = b
    
for _ in range(m):
     a,b,c = map(int, input().split())
     arr.append((c,a,b))
     
     
result = 0
arr.sort()


for c,a,b in arr:
    if find(a) != find(b):
       union(a,b)
       result += c
            
print(result)