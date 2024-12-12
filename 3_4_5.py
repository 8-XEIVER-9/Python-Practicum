goods = []
for _ in range(3):
    goods += input().replace(" ", "").split(",")
    goods.sort()
for index, value in enumerate(goods, 1):
    print(f"{index}. {value}")