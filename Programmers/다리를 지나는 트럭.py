#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0 #시간
    #queue 풀이
    
    bridge = deque(0 for _ in range(bridge_length))
    total = 0
    
    while(bridge):
        answer+=1
        total -= bridge.popleft() #다리에서 트럭 제거
        if(truck_weights):
            if(truck_weights[0] + total <= weight):
                total += truck_weights[0]
                bridge.append(truck_weights.pop(0)) #대기에서 트럭 1개 제거 하고 다리위에 올
            else:
                bridge.append(0)
    return answer