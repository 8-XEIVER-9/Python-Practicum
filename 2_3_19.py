binn = [i for i in range(1, 1001)]
left = -1
right = len(binn)
mid = (left + right) // 2
print(binn[mid])
while (answer := input()) != 'Угадал!':
    if answer == 'Меньше':
        right = mid
    elif answer == 'Больше':
        left = mid
    mid = (left + right) // 2
    print(binn[mid])