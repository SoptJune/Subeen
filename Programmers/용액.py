#!/usr/bin/env python3
# -*- coding: utf-8 -*-



n = map(int,input().split())
liq = list(map(int,input().split()))

def sol(liq):
    
    left=0
    right=len(liq)-1
    answer = [abs(liq[left]+liq[right]),(liq[left],liq[right])]
 
    while left<right:
        mix = liq[left]+liq[right]
        if abs(mix) < answer[0]:
            answer[0] = abs(mix)
            answer[1] = (liq[left],liq[right])
        if mix > 0:
            right-=1
        else:
            left += 1
        
    return answer[1]
 
answer = sol(liq)
print(answer[0],answer[1])