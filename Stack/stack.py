#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 23:37:04 2022

@author: kimsubin
"""
import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda x: sys.stdout.write(str(x) + "\n")

n = int(input())
stack = [] 
ans = []
flag = 0
count = 1

for i in range(n):
    num = int(input())
    
    while count <= num:       # 오름차순으로 push
        stack.append(count)
        ans.append("+")
        count += 1
    
    if stack[-1] == num: # stack의 맨 위부 num입력숫자와 같으면 pop하
        stack.pop()        
        ans.append("-")
    else:                   
        print("NO")         
        flag = 1            
        break               

if flag == 0:
    for i in ans:
        print(i)