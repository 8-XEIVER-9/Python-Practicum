size = int(input())
wth = len(str((size + 1) // 2))
for i in range(size):
    for j in range(size):
        print(f'{min(i + 1, j + 1, size - i, size - j):>{wth}}', end=' ')
    print()