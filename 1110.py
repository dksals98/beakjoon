N = int(input())
if N < 10:
    new_num = N * 10
count = 0

new_num = N

while(True):
    left = new_num // 10
    right = new_num % 10

    new_right = (left + right) % 10
    new_num = right * 10 + new_right
    count += 1

    if new_num == N:
        print(count)
        break
