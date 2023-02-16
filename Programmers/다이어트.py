#!/usr/bin/env python3
# -*- coding: utf-8 -*-


g = int(input())
k,r = 1,1 #k=현재, r=기억몸무게
answer =[]

while True:
    result =k**2 - r**2
    
    if result > g and k-r == 1:
        break
    if result > g :
        r +=1 #기억하는 몸무게
    elif result < g : 
         k +=1 #현재몸무게
    else:
        answer.append(k)#현재몸무게 추가
        k+=1


if answer:
    for x in answer:
        print(x)
else :
    print(-1)