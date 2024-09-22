def green(x, y):
    return x**2 + y**2 <= 100


def red(x, y):
    if x >= 0 and y >= 0:
        return x**2 + y**2 <= 25
    if y < 0:
        return y >= 0.25 * x**2 + 0.5 * x - 9
    if x < 0 and y >= 0:
        return y <= 5 and y <= 5 / 3 * x + 35 / 3


x = float(input())
y = float(input())
if green(x, y) and not red(x, y):
    print("Зона безопасна. Продолжайте работу.")
elif red(x, y):
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Вы вышли в море и рискуете быть съеденным акулой!")