N, K = map(int, input().split())
things = [(0, 0)]

for i in range(1, N+1):
    W, V = map(int, input().split())
    things.append((W, V))

bag = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if things[i][0] > j:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(bag[i-1][j], things[i][1] + bag[i-1][j-things[i][0]])

print(bag[N][K])


