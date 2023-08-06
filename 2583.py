import sys
sys.setrecursionlimit(10000)

M, N, K = map(int, sys.stdin.readline().split())

board = [[0]*N for _ in range(M)]
check = [[0]*N for _ in range(M)]
count = 0
width_count = []

def dfs(a, b):
    global width
    width += 1
    check[b][a] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx <= N-1 and 0 <= ny <= M-1 and board[ny][nx] == 0:
            if check[ny][nx] == 0:
                dfs(nx, ny)

for _ in range(K):
    ax, ay, bx, by = map(int, sys.stdin.readline().split())
    for i in range(ax, bx):
        for j in range(ay, by):
            board[j][i] = 1

for i in range(M):
    for j in range(N):
        width = 0
        if board[i][j] == 0 and check[i][j] == 0:
            dfs(j, i)
            count += 1
            width_count.append(width)

print(count)
width_count.sort()
for i in width_count:
    print(i, end=" ")
