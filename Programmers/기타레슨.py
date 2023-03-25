#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 11:53:31 2023

@author: kimsubin
"""

n,m = map(int,input().split())
lectures = list(map(int,input().split()))

start = max(lectures)
end = sum(lectures)
result = 0

while start <= end:
    mid = (start+end)//2
    count = 0 #블루레이개수
    sum_lecture = 0
    
    for i in range(n):
        if lectures[i]+sum_lecture > mid :
            count+=1
            sum_lecture=0 #블루레이 개수추가할수록 다시 합 초기화
        
        sum_lecture+=lectures[i]
        
    if sum_lecture:
        count+=1
    if count > m :
        start = mid+1
    else:
        end = mid-1
        result = mid
print(result)
