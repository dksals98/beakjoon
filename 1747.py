import math

N = int(input())

def Prime(Num):
    if Num == 1:
        return False
    elif Num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(Num))+1):
            if Num % i == 0:
                return False
    return True

for i in range(N, 10000001):
    tostr = str(i)
    check = True
    for j in range(len(tostr) // 2):
        if tostr[j] != tostr[len(tostr)-1-j]:
            check = False
            break
    if check == True:
        if Prime(i):
            print(i)
            break