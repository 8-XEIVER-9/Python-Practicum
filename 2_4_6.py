from math import gcd
n = int(input())
ans = []
for i in range(n):
    ans.append(int(input()))
print(gcd(*ans))