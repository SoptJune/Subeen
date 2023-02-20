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
        if number[left]+number[right] == number[i]:
            if left !=i and right !=i:
                count+=1
                break
            elif left ==i:
                left+=1
            else:
                right-=1
        elif number[left]+number[right]>number[i]:
            right-=1
        else:
            left+=1

print(count)