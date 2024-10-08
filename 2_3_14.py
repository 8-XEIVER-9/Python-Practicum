def dels(n):
    ans = set()
    for i in range(1, int(n**0.5 + 1)):
        if n % i == 0:
            ans.add(n // i)
            ans.add(i)
    return len(ans)


n = int(input())
if dels(n) == 2:
    print("YES")
else:
    print("NO")