
def solution(begin, target, words):
    answer = 0
    tmp = [begin]
    visited = [0 for i in words]

    if target not in words:
        return 0

    while tmp:
        
        stack = tmp.pop()
        
        if stack == target:
            return answer      
        
        for i in range(len(words)):
            cnt = 0
            
            for j in range(len(words[i])):
                if words[i][j] != stack[j]:  
                    cnt += 1
                    
            if cnt == 1:        
                if visited[i] == 1:  # 방문한 경우
                    continue
                else:
                    visited[i] = 1   # 방문 안 한 경우
                tmp.append(words[i])
        answer += 1
    return answer