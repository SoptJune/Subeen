#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(numbers, target):
    
    nodes= [0]
    for i in numbers:
        trees = []
        for j in nodes : 
            trees.append(j+i) #0+1 
            trees.append(j-i) #0-1
        nodes = trees
        
    return nodes.count(target)

