from itertools import permutations
n = int(input())
goods = []
for _ in range(n):
    goods += input().replace(" ", "").split(",")
goods.sort()
for need in permutations(goods, r=3):
    print(*need)