#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:48:43 2022

@author: kimsubin
"""

def solution(n, times):
    answer = 0
   
    left = min(times)
    right = max(times)*n
    
    while left <= right:
        mid = (left+ right) // 2
        check = 0
        
        for time in times:
            check += mid // time
            if check >= n:
                break
        
        if check >= n:
            answer = mid
            right = mid - 1
      
        elif check < n:
            left = mid + 1
            
    return answer