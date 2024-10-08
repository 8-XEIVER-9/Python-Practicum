def check(n):
    ans = set()
    for i in range(1, int(n**0.5 + 1)):
        if n % i == 0:
            ans.add(n // i)
            ans.add(i)
    return len(ans) == 2


n = int(input())
cnt = 0
for i in range(n):
    d = int(input())
    if check(d):
        cnt += 1
print(cnt)