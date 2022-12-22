#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solution(jobs):
    
    answer = 0
    start = 0  
    jobs_length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])  

    while len(jobs) != 0:
        
        for i in range(jobs_length):
            
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            
            if i == jobs_length - 1:
                start += 1

    return answer // jobs_length
