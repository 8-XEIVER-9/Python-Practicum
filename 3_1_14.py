ans = list(map(int, input().split()))
s = int(input())
for i in range(len(ans)):
    ans[i] = ans[i]**s
print(*ans)
    