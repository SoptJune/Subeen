
x,y = map(int,input().split())
diff= y - x

# 약간 이분탄색으로 생각했는데 조건따져서 풀이로~
# 제곱근 범위 수 , 그 외의 수 규칙 따져서

i = 2

if diff <= 2:
    print(diff) # 끝-처음 차이가 2이하면 그대로 출력
else:
    while True:
        if i * (i - 1) < diff <= i * i: #2,4 / 6,9 / 12,16 / 20,25
            print(2 * i - 1)
            break
        elif i * i < diff <= i * (i + 1): #9,12 /16,20 ...
            print(2 * i)
            break
        i += 1
        
# 111
# 121 -> 4일때
# 1211
# 1221
# 12321 -> 9일때
#...
# 1234321 -> 16