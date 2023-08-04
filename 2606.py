computer_count = int(input())
network = int(input())

computers = [[] for _ in range(computer_count + 1)]
virus_check = [False] * (computer_count + 1)
count = 1

def dfs(num):
    global virus_check
    virus_check[num] = True
    for i in computers[num]:
        if not virus_check[i]:
            dfs(i)

for j in range(network):
    v1, v2 = map(int, input().split())
    computers[v1].append(v2)
    computers[v2].append(v1)

dfs(1)
print(virus_check.count(True) - 1)