N, K = map(int, input().split())
products = list(map(int, input().split()))  # 두 번째 줄에는 전기용품의 이름이 K 이하의 자연수
mt = [0] * N
answer = 0
change = 0
key = 0
# 멀티탭에 동일제품 있을 때 -> products에서 그 뒤에 있는 용품이 멀티탭에 있는지 우선 확인
#
while products:
    product = products[0]
    if product in mt:
        products.remove(product)  # 멀티탭에 있으면 리스트에서 삭제
        continue

    elif 0 in mt: # 0은 초기화값 , 따라서 멀티탭 비어있는 자리에 넣기
        mt[mt.index(0)] = product
        products.remove(product)

    # 멀티탭에 빈자리가 없을 경우
    else:
        for i in mt:
          #멀티탭에 있는 것 중에 또 쓸 제품이 있는지 => 없을 때
            if i not in products:
                change = i
                break
            #있다면 => 가장 나중에 사용하는 것을 골라
            elif products.index(i) > key:
                key = products.index(i)
                change = i
        key = 0
        answer += 1
        mt[mt.index(change)] = product
        products.remove(product)


print(answer)
