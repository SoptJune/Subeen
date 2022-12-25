#!/usr/bin/env python3
# -*- coding: utf-8 -*-



n,m=map(int,input().split())
arr=list(map(int,input().split()))
def search(x):
  high = arr[0]
  low = arr[0]
  cnt=1
  
  for i in range(1,n):
      
    high=max(high,arr[i]) # 구간 중에 가장 high
    low=min(low,arr[i]) # 구간 중에 가장 low
    
    if high - low > x:
      cnt+=1  # x는 전체 배열 (구간) 기준 mid 인데 이보다 작으면 구간 쪼개기
      high=arr[i]
      low=arr[i]
      
  return cnt

start= 0 #전체 배열기준
end = max(arr)
result=0

while start<=end:
  mid=(start+end)//2
  if search(mid)<=m:
    end = mid-1
    result=mid
  else:
    start = mid+1

print(result)



