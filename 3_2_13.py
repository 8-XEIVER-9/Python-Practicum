dishes = {}
n = int(input())
for _ in range(n):
    dish = input()
    dishes[dish] = True
m = int(input())
for _ in range(m):
    n_dishes = int(input())
    for _ in range(n_dishes):
        check = input()
        dishes[check] = False
for key in sorted(dishes.keys()):
    if dishes[key]:
        print(key)
if True not in dishes.values():
    print("Готовить нечего")