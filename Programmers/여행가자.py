

import sys
input=sys.stdin.readline
n=int(input())
m=int(input())

city=[]
visited=[0 for _ in range(n)]

for _ in range(n):
    city.append(list(map(int,input().split())))
graph=list(map(int,input().split()))

def dfs(start):
    visited[start]=True
    for index,i in enumerate(city[start]):
        if i==1 and visited[index]==False:
          visited[index]=True
          dfs(index)

dfs(graph[0]-1) #도시는 1부터 시작하니깐 인덱스는0부터시작임

if 0 not in visited:
  print('YES')
  sys.exit()
  
for i in graph:
  if visited[i-1]==0:
    print('NO')
    sys.exit()
print('YES')