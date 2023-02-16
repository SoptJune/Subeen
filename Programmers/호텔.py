#!/usr/bin/env python3
# -*- coding: utf-8 -*-

C,N = map(int,input().split())
costs= [list(map(int,input().split())) for _ in range(N)]

INF = 1e7
dp = [INF for _ in range(C+100)] #dp 최대값으로 초기화
dp[0]=0
 
for cost, people in costs:
    for i in range(people,C+100): #최소인원 C보다 인원이 많은 경우 고려해서
        dp[i] = min(dp[i-people]+cost,dp[i]) #현재cost, i번째까지의 최소 cost
 
print(min(dp[C:]))
