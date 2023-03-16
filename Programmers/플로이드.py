import sys
maxSize = sys.maxsize

n = int(sys.stdin.readline())  # 도시
m = int(sys.stdin.readline())  # 버스

#최대값으로 초기화함
graph = [[maxSize] * (n) for _ in range(n)] #범위는 0부터 하고 계산할 때 -1계산하면서 생각하기

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = min(c, graph[a-1][b-1])   

#dp풀이 / 한번에 목적지 가거나 or 중간지점 k 거쳐서 목적지 가기
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

#조건문 한개 줄여보려고 *씀
for i in graph:
    for j in range(n):
        if graph[j] == maxSize:
            graph[j] = 0
    print(*i)