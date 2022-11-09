#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 13:38:16 2022

@author: kimsubin
"""


def solution(progresses, speeds):
    answer = []
    count = 0
    while progresses:
        if progresses[0] + speeds[0] >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            if count:
                answer.append(count)
                count = 0 # 다음 배포 차례로->count 다시 세기
            progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]
    answer.append(count)
    return answer