n = int(input())
goods = []
ans = []
for _ in range(n):
    line = input()
    goods.append(set(line[line.find(":") + 2:].split(", ")))
for i in range(n):
    ans += list(goods[i].difference(*goods[:i], *goods[i + 1:]))
ans.sort()
print("\n".join(ans))
