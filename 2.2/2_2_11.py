n = list(map(int, input()))
if max(n) + min(n) == 2 * (sum(n) - max(n) - min(n)):
    print("YES")
else:
    print("NO")