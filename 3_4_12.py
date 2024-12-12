n = int(input())
goods = []
for _ in range(n):
    goods += input().replace(" ", "").split(",")
goods.sort()
for index, value in enumerate(goods, 1):
    print(f"{index}. {value}")