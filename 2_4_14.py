n = int(input())
m = int(input())
d = 1
wth = len(str(m * n))
for i in range(n):
    ans = []
    for _ in range(1, m + 1):
        ans.append(d)
        d += 1
    if (i + 1) % 2 != 0:
        for j in range(len(ans)):
            print(f'{str(ans[j]):>{wth}}', end=' ')
        print()
    else:
        for j in range(len(ans) - 1, -1, -1):
            print(f'{str(ans[j]):>{wth}}', end=' ')
        print()