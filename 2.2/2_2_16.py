P = int(input())
V = int(input())
T = int(input())
a = ["0"] * 10000
a[P] = "Петя"
a[V] = "Вася"
a[T] = "Толя"
a = a[::-1]
places = []
k = 0
while k != 3:
    for n in a:
        if n != "0":
            k += 1
            places.append(n)
print(f"{places[0]:^24}")
print(f"{places[1]:^8}{" " * 16}")
print(f"{" " * 16}{places[2]:^8}")
print(f"{"II":^8}{"I":^8}{"III":^8}")