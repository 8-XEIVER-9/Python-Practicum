treasure = {}
for _ in range(int(input())):
    x, y = input().split()
    square = str(int(x) // 10) + " " + str(int(y) // 10)
    treasure[square] = treasure.get(square, 0) + 1
print(max(treasure.values()))