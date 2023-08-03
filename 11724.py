import sys
sys.setrecursionlimit(10000)

N, M = list(map(int, sys.stdin.readline().split()))

points = [[] for _ in range(N + 1)]
checked = [False] * (N + 1)
count = 0


def dfs(num):
    global checked
    global points

    checked[num] = True
    for i in points[num]:
        if not checked[i]:
            dfs(i)


for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    points[u].append(v)
    points[v].append(u)

for j in range(1, N+1):
    if not checked[j]:
        count += 1
        dfs(j)

print(count)
