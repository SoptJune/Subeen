#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
def num_check(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            return "NO"
    return "YES"

t = int(input()) #ㅌㅔ스트케이스
for _ in range(t):
    n = int(input())#전화번호의 수
    numbers = [sys.stdin.readline().strip() for _ in range(n)] #전화번호 입력 문자열로
    numbers.sort()
    print(num_check(numbers))
    



#2
#3
#911
#97625999
#91125426
