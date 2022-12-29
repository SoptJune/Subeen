#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solution(a):
    
    answer = 2
    
    if 0 <= len(a) <= 2:
        
        return len(a)

    left, right = a[0],a[-1]
    
    for i in range(1, len(a)-1):
        
        if left > a[i]: #left보다 ㄷㅓ 작은수라면  left의 값을 더 작은수로 갱신, answr +=1
            answer += 1
            left = a[i]
            
        if right > a[-1-i]:
            answer += 1
            right = a[-1-i]
            
    return answer if left != right else answer-1
