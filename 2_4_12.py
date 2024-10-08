n = int(input())
m = int(input())
wth = len(str(m * n))
nm = 0
for i in range(n):
    for j in range(m):
        nm += 1
        print(f'{nm:>{wth}}', end=' ')
    print()