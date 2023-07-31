N = int(input())

square = [list(input()) for _ in range(N)]
width = 0
height = 0

for i in range(N):
    wcount = 0
    hcount = 0
    for j in range(N):
        if square[i][j] == "X":
            if wcount >= 2:
                width += 1
            wcount = 0
        if square[i][j] == ".":
            wcount += 1
            if j == N-1:
                if wcount >= 2:
                    width += 1

        if square[j][i] == "X":
            if hcount >= 2:
                height += 1
            hcount = 0
        if square[j][i] == ".":
            hcount += 1
            if j == N - 1:
                if hcount >= 2:
                    height += 1

print(width, height)