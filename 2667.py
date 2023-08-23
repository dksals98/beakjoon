from collections import deque

N = int(input())

map = [list(map(int, input())) for _ in range(N)]
checked = [[0] * N for _ in range(N)]
count = 0
house_num = 0
house = []


def bfs(a, b):
    global house_num
    house_num = 1
    queue.append((a, b))
    checked[b][a] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and map[ny][nx] == 1:
                if checked[ny][nx] == 0:
                    queue.append((nx, ny))
                    house_num += 1
                    checked[ny][nx] = 1


queue = deque()
for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and checked[j][i] == 0:
            bfs(i, j)
            count += 1
            house.append(house_num)

house.sort()
print(count)
for k in house:
    print(k)
