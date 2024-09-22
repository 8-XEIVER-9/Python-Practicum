P = int(input())
V = int(input())
T = int(input())
a = ["0"] * 10000
a[P] = "Петя"
a[V] = "Вася"
a[T] = "Толя"
a = a[::-1]
place = 0
while place != 3:
    for n in a:
        if n != "0":
            place += 1
            print(f"{place}. {n}")