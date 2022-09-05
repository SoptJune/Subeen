#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:36:35 2022

@author: kimsubin
"""

n,m=map(int,input().split())

rectangle=[]
count=[]
for i in range(n):
    rectangle.append(input())
    
for a in range(n-7):
    for b in range(m-7):
        white=0 
        black=0 
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2==0:#짝수
                    if rectangle[i][j]!='W':#W이면
                        white+=1 #W로 칠하는 개수
                    else:
                        black+=1 #B로 칠하는 개수
                else:
                    if rectangle[i][j]!='W':#B이면
                        black+=1#B로 칠하는 개수
                    else:
                        white+=1#W로 칠하는 개수
                        
        count.append(white) 
        count.append(black) 
        
print(min(count)) 