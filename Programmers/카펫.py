#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solution(brown, yellow):
    
    for i in range(1, yellow +1):
        if (yellow % i == 0):
            
            row_yellow = yellow // i
            col_yellow = i
            
            if (2 * (row_yellow + col_yellow) + 4 == brown):
                
                return [row_yellow +2, col_yellow+2]
