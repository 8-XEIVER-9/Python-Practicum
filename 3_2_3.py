n = int(input())
ans = set()
for _ in range(n):
    for i in input().split():
        ans.add(i)
print("\n".join(ans))