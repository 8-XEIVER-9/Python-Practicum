def check(n):
    return n == n[::-1]


n = input()
if check(n):
    print("YES")
else:
    print("NO")