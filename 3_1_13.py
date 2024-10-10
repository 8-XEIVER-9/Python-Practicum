n = int(input())
ans = []
for _ in range(n):
    ans.append(int(input()))
s = int(input())
for i in range(n):
    print(ans[i]**s)