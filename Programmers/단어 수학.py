#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:48:43 2023

@author: kimsubin
"""

#import sys
#input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in  range(n)]
dict = {}

#자릿수합으로 가중치 주면 됨
#10제곱수로 계산하면 될듯
#pow가 내장함수 , math.pow는 실수형 math라이브러리

for word in words:
    
    alphabet = len(word)-1 #4자리수이면 10의 3/2/1/0 자리 제곱
    
    for i in word:
        
        if i in dict: #만약 이미 존재하는 알파벳이면 더해주기만
           dict[i] += pow(10, alphabet) ## **와 동일
        else:
           dict[i] = pow(10, alphabet)
           
        alphabet -= 1
            

dict = sorted(dict.values(), reverse=True) #각 알파벳의 자릿값 내림차순으로

answer = 0
number = 9 #9부터 감소하면서 가중치 주기

for i in dict:
    answer += number * i
    number -= 1

print(answer)