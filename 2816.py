N = int(input())
channel = []

for i in range(N):
    channel.append(input())
    if channel[i] == 'KBS1':
        kbs1 = i
    elif channel[i] == 'KBS2':
        kbs2 = i


for j in range(kbs2):
    print('1', end='')
for j in range(kbs2):
    print('4', end='')

if kbs2 > kbs1:
    kbs1 += 1

for j in range(kbs1):
    print('1', end='')
for j in range(kbs1):
    print('4', end='')