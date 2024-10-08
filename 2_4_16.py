n = int(input())
wth = int(input())
for i in range(1, n + 1):
    ans = []
    for j in range(1, n + 1):
        ans.append(f"{i * j:^{wth}}")
    print(*ans, end=" ", sep="|")
    print()
    if i < n:
        print("-" * (n * wth + (n - 1)))