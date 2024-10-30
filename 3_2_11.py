ans = {}
n = int(input())
for _ in range(n):
    man = input()
    if man in ans:
        ans[man] += 1
    else:
        ans[man] = 1
cnt = 0
for value in ans.values():
    if value != 1:
        cnt += value
print(cnt)