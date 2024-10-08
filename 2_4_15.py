n = int(input())
m = int(input())
matrix = [[0] * m for i in range(n)]
d = 1
for j in range(m):
    if j % 2 != 0:
        for i in range(n):
            matrix[i][j] = d
            d += 1
    else:
        for i in range(n - 1, -1, -1):
            matrix[i][j] = d
            d += 1
wth = len(str(n * m))
for i in range(n):
    for j in range(m):
        print(f"{matrix[::-1][i][j]:>{wth}}", end=" ")
    print()
