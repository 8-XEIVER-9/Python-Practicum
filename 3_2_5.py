n = int(input())
m = int(input())
d1 = set()
d2 = set()
for _ in range(n + m):
    name = input()
    if name in d1:
        d2.add(name)
    else:
        d1.add(name)

if d1 ^ d2:
    print(len(d1 ^ d2))
else:
    print("Таких нет")