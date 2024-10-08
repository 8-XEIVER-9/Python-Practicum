def check(n):
    ans = set()
    for i in range(1, int(n**0.5 + 1)):
        if n % i == 0:
            ans.add(i)
            ans.add(n // i)
    return len(ans) == 2


n = int(input())
dels = [0] * n
for i in range(2, len(dels)):
    cnt = 0
    if n % i == 0 and check(i):
        while n % i == 0:
            cnt += 1
            n //= i
    dels[i] = cnt
ans = ""
for i in range(len(dels)):
    if dels[i] != 0:
        ans += f"{i} * " * dels[i]
print(ans[:-2])