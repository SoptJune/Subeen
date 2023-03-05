#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    #queue = deque([(x,y)])
    visited[x][y] = 1 #시작 방문처리
    
    while queue:
        i,j = queue.popleft()
        
        for l in range(4):
            nx = i+dx[l]
            ny = j+dy[l]
            if 0<=nx<n and 0<=ny<m :
               if not visited[nx][ny] and lists[nx][ny]== 0 : 
                    queue.append([nx,ny])
                    visited[nx][ny]=1 #방문춰리
               elif lists[nx][ny]==1: #치즈면  +1
                      visited[nx][ny]+=1
n,m = map(int,input().split())
lists = [list(map(int,input().split()))for _ in range(n)]

count = 0 #bfs횟수
#방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while True:
     visited = [[0]*m for _ in range(n)] 
     bfs(0,0)
     count+=1
    
     for i in range(n):
        for j in range(m):
            if visited[i][j] >=2: #인접한 부분이 2곳이상일 때 녹아야함.
                lists[i][j] = 0 #녹았으니까 공기값"0"으로 다시 바꿔줌
 
    
     air = 0
     for i in range(n):
         for j in range(m):
             if lists[i][j] ==0: #행에서 0의 개수 , 즉 치즈가 없어야함
                 air+=1
     if air == (n*m): # 치즈 없는 경우 모두 0인것이 사각형 전체여야함
          break
 
print(count)
