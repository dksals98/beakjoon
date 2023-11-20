from collections import deque

N, M, V = map(int, input().split())
node = [[] for _ in range(N+1)]
checked_dfs = [False] * (N+1)
checked_bfs = [False] * (N+1)
queue = deque()


def dfs(num):
    print(num, end=' ')
    checked_dfs[num] = True
    for i in node[num]:
        if not checked_dfs[i]:
            dfs(i)


def bfs(num):
    queue.append(num)
    checked_bfs[num] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in node[v]:
            if not checked_bfs[i]:
                checked_bfs[i] = True
                queue.append(i)


for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for i in range(1, N+1):
    node[i].sort()

dfs(V)
print()
bfs(V)

