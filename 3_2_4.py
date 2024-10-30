n = int(input())
m = int(input())
d1 = set()
d2 = set()
for _ in range(n):
    d1.add(input())
for _ in range(m):
    d2.add(input())
if d1 & d2:
    print(len(d1 & d2))
else:
    print("Таких нет")