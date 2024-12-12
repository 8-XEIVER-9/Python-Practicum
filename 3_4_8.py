from itertools import cycle
m = int(input())
poridges = []
for _ in range(m):
    poridges.append(input())
n = int(input())

days = 0
for poridge in cycle(poridges):
    if days < n:
        print(poridge)
        days += 1
    else:
        break