ans = {}
n = int(input())
for _ in range(n):
    man = input()
    if man in ans:
        ans[man] += 1
    else:
        ans[man] = 1
cnt = 0
for key in sorted(ans.keys()):
    if ans[key] != 1:
        cnt += ans[key]
        print(f"{key} - {ans[key]}")
if not cnt:
    print("Однофамильцев нет")
