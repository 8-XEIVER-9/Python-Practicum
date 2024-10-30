goods = []
recipes = {}
cook = []

for _ in range(int(input())):
    goods.append(input())
for _ in range(int(input())):
    name = input()
    need = []
    for _ in range(int(input())):
        need.append(input())
    recipes[name] = need

for name in recipes:
    if (set(recipes[name]) & set(goods) == set(recipes[name])):
        cook.append(name)

if cook:
    cook.sort()
    print("\n".join(cook))
else:
    print('Готовить нечего')