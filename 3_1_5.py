def pal(n):
    return n == n[::-1]


if pal(input()):
    print("YES")
else:
    print("NO")