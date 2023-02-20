#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
number = list(map(int,input().split()))
number.sort() #오름차순, 탐색하기
count = 0
for i in range(N):
    left = 0
    right =N-1
    while left < right:
        if number[left]+number[right] == number[i]: #1
            if left !=i and right !=i: #2개 모두 각 다른 자리 수 일때
                count+=1
                break
            elif left ==i: #left만 같을때
                left+=1
            else: #right만 같을때
                right-=1
        elif number[left]+number[right]>number[i]:#2
            right-=1
        else: #3
            left+=1

print(count)