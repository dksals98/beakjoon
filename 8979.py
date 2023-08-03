N, K = map(int, input().split())


nation = [list(map(int, input().split())) for _ in range(N)]

nation.sort(key=lambda x : (x[1], x[2], x[3]), reverse=True)

rank = 1
for i in range(N):
    if nation[i][0] == K:
        for j in range(i-1, -1, -1):
            if nation[j][1:] != nation[i][1:]:
                rank = j+2
                break
        break

print(rank)








