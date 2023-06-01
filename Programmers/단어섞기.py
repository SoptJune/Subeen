from collections import deque


def word(n):
    a, b, c = input().split()
    queue = deque([(0, 0)])  # first,second
    visited = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    i = 0
    while queue:
        for l in range(len(queue)):
            first, second = queue.popleft()
            if first < len(a) and not visited[first + 1][second] and a[first] == c[i]:
                visited[first + 1][second] = True  # 방문처리
                queue.append((first + 1, second))
            if second < len(b) and not visited[first][second + 1] and b[second] == c[i]:
                visited[first][second + 1] = True
                queue.append((first, second + 1))
        i += 1
    #출력
    if i == len(c) + 1:
        print("Data set %d: yes" % (n + 1))
    else:
        print("Data set %d: no" % (n + 1))


n = int(input())
for i in range(n):
    word(i)
