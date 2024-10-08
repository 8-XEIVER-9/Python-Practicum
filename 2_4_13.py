n = int(input())
m = int(input())
wth = len(str(n * m))
for i in range(n):
    d = i + 1
    for j in range(m):
        print(f"{d:>{wth}}", end=" ")
        d += n
    print()