name = input()
cost = int(input())
weight = int(input())
money = int(input())
print("Чек")
print(f"{name} - {weight}кг - {cost}руб/кг")
print(f"Итого: {cost * weight}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {money - (cost * weight)}руб")