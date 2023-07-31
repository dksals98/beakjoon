number = []
color = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
count_number = [0] * 10

def sequence(numbers):
    for i in range(4):
        if numbers[i]+1 != numbers[i+1]:
            return False
    return True

for _ in range(5):
    first_card, second_card = input().split()
    color[first_card] += 1
    count_number[int(second_card)] += 1
    number.append(second_card)

number = sorted(list(map(int, number)))

if 5 in color.values() and sequence(number) == True:
        print(max(number) + 900)

elif 4 in count_number:
    print(800 + count_number.index(4))

elif 3 in count_number and 2 in count_number:
    print(count_number.index(3) * 10 + count_number.index(2) + 700)

elif 5 in color.values():
    print(max(number) + 600)

elif sequence(number) == True:
    print(max(number) + 500)

elif 3 in count_number:
    print(count_number.index(3) + 400)

elif count_number.count(2) == 2:
    first_num = count_number.index(2)
    count_number[count_number.index(2)] = 0
    second_num = count_number.index(2)
    print(second_num * 10 + first_num + 300)

elif 2 in count_number:
    print(count_number.index(2) + 200)

else:
    print(max(number) + 100)