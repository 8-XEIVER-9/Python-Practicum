n = int(input())
ans = ""
for i in range(n):
    max_d = max(list(map(int, input())))
    ans += str(max_d)
print(ans)