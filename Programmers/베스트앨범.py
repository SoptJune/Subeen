
def solution(genres, plays):
    answer = []
    total_list = {}	#총 횟수 딕셔너리
    genres_list = {}#play수 딕셔너리
    
    for i in range(len(genres)):
        if genres[i] in total_list:
            total_list[genres[i]] += plays[i]
        else:
            total_list[genres[i]] = plays[i]
        
        if genres[i] in genres_list:
            genres_list[genres[i]].append([plays[i], i])
        else:
            genres_list[genres[i]] = [[plays[i], i]] 
            
   
    rank_g = sorted(total_list, key=total_list.get, reverse=True)
    
    for x in rank_g:
        rank_p = sorted(genres_list[x], key=lambda x: (-x[0], x[1]))
        
       
        if len(rank_p) == 1:
            answer.append(rank_p[0][1])
        else:
            for i in range(2):
                answer.append(rank_p[i][1])
    return answer
