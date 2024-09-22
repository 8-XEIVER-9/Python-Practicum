n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
cost = n * m
weight1 = n
weight2 = 0
while cost != weight1 * k1 + weight2 * k2:
    weight1 -= 1
    weight2 += 1
print(weight1, weight2)