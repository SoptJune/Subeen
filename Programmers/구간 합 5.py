#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import sys
#input = sys.stdin.readline

n,m = map(int,input().split()) # n은 행렬크기 , m은 입력받을 횟수
number_list = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*(n+1) for i in range(n+1)] # 0으로 세팅


# 누적합으로 , for문으로 하나씩 값 더해서 구하면 시간초과,,,,;;
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + number_list[i-1][j-1]

#입력받은 값 계산
for _ in range(m) : 
    a,b,c,d = map(int,input().split())
    answer = dp[c][d] - dp[c][b-1] -dp[a-1][d] + dp[a-1][b-1]
    print(answer)

