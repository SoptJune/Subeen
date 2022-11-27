def dfs(n,computers, start, visited):
    visited[start] = True
    for i in range(0,n):
        if (visited[i] == False and computers[start][i]==1):
            visited = dfs(n,computers,i,visited)
    return visited


def solution(n, computers):
    visited = [False]*n
    answer = 0
    
    for start in range(0,n):
        if(visited[start] == False):
            dfs(n,computers,start,visited)
            answer +=1
            
    return answer