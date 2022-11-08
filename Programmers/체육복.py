#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 17:40:08 2022

@author: kimsubin
"""

def solution(n, lost, reserve):
    
    reserve_list = set(reserve) - set(lost)
    lost_list = set(lost) - set(reserve)
    
    for i in reserve_list:
        if (i - 1) in lost_list:
            lost_list.remove(i - 1)
        elif (i + 1) in lost_list:
            lost_list.remove(i + 1)
            
    return n - len(lost_list)