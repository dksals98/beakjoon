from collections import deque

N = int(input())

def bfs(a, b, color):
    queue.append((a, b))
    check[b][a] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N-1 and 0 <= ny <= N-1 and grid[ny][nx] == color:
                if check[ny][nx] == 0:
                    queue.append((nx, ny))
                    check[ny][nx] = 1


grid = [list(input()) for _ in range(N)]
check = [[0]*N for _ in range(N)]
queue = deque()
count = 0
count2 = 0

for i in range(N):
    for j in range(N):
        if check[i][j] == 0:
            bfs(j, i, grid[i][j])
            count += 1

check = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if check[i][j] == 0:
            bfs(j, i, grid[i][j])
            count2 += 1

print(count, count2)

