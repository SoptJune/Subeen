def solution(gems):
    answer = [0, len(gems) - 1]
    gems_type = len(set(gems)) # 종류
    i, j = 0, 0
    dic = {gems[0]: 1}
    while i < len(gems) and j < len(gems):
        
        if len(dic) == gems_type:
            
            if j - i < answer[1] - answer[0]:
                answer = [i, j]
            else:
                dic[gems[i]] -= 1
                if dic[gems[i]] == 0:
                    del dic[gems[i]]
                i += 1
        else:
            j += 1
            if j == len(gems):
                break
            dic[gems[j]] = dic.get(gems[j], 0) + 1
            
    answer[0]+=1
    answer[1]+=1
    
    return answer
