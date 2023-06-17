import sys
tem = sys.maxsize
n = int(input())
li =list(map(int,input().split()))
start = 0
end = len(li)-1

while start<end:
    if abs(li[start]+li[end]) <= tem:
        tem = abs(li[start]+li[end])
        result_s = li[start]
        result_e = li[end]

    if li[start]+li[end] < 0:
        start+=1
    else:
        end-=1

print(result_s,result_e)



