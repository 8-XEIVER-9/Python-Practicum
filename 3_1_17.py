def check(n):
    return n == n[::-1]


if check(input().replace(" ", "").lower()):
    print("YES")
else:
    print("NO")