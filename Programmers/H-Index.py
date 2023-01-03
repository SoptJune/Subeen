#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(citations):
    citations.sort() #0,1,3,5,6
    citations_len = len(citations)
    for i, citation in enumerate(citations):
        
        if citation >= citations_len - i :
            return citations_len - i
    return 0
