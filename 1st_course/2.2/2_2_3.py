P = int(input())
V = int(input())
T = int(input())
maxx = max(P, V, T)
if maxx == P:
    print("Петя")
if maxx == V:
    print("Вася")
if maxx == T:
    print("Толя")