from itertools import product
n = int(input())
m = int(input())
wdh = len(str(n * m))
for i, j in product(range(1, n + 1), range(1, m + 1)):
    print(f'{((i - 1) * m + j):>{wdh}}', end=' ')
    if j == m:
        print()