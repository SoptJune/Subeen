#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque

def bfs():
    q = deque()
    q.append((a_,b_))
    visited[a_][b_] = True
    
    while q:
        
        a,b = q.popleft()
        c = total-a-b
        
        if a==b==c: 
            print(1)
            return
        
        for x, y in (a,b),(a,c),(b,c):
            if x < y:
                y -= x
                x += x
            elif x > y:
                x -= y
                y += y
            else: 
                continue
            
            z = total-x-y
            a = min(x,y,z)
            b = max(x,y,z)
            
            if not visited[a][b]:
                q.append((a,b))
                visited[a][b] = True #방문처리
    print(0)

a_,b_,c_ = map(int, input().split())
total = a_+b_+c_
visited = [[False]*(total+1) for _ in range(total+1)] #초기화

if total%3 != 0: 
    print(0)
else:
    bfs()