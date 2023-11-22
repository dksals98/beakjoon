from collections import deque

N, M = map(int, input().split())
count = 0
queue = deque()
check = [0] * (100001)


def bfs(num):
    queue.append(num)
    while queue:
        v = queue.poplesft()
        if v == M:
            return print(check[v])
        for i in [v+1, v-1, v*2]:
            if 0 <= i <= 100000 and not check[i]:
                check[i] = check[v] + 1
                queue.append(i)


bfs(N)