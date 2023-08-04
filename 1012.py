import sys
sys.setrecursionlimit(10000)

T = int(sys.stdin.readline())

def dfs(a, b):
    checked[a][b] = True
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        xj = b + dx[i]
        yi = a + dy[i]
        if 0 <= xj <= M - 1 and 0 <= yi <= N - 1 and ground[yi][xj]:
            if not checked[yi][xj]:
                dfs(yi, xj)

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    ground = [[0]*M for _ in range(N)]
    checked = [[False]*M for _ in range(N)]
    count = 0

    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1

    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1 and not checked[i][j]:
                dfs(i, j)
                count += 1
    print(count)
