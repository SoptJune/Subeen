

n,m = map(int,input().split()) # n 행 m 열
li = list(map(int,input().split()))

left  = 0
right = m-1
result = 0
left_h = li[left]
right_h = li[right]

while left<right:
    left_h = max(li[left],left_h)
    print(left_h,li[left])
    right_h = max(li[right],right_h)
    if left_h <= right_h:
        result+= left_h - li[left]
        left+=1
    else:
        result+= right_h-li[right]
        right-=1
print(result)


