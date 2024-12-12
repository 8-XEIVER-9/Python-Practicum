def tail(n, mass):
    return mass[-n:]


name = input()
n = int(input())

with open(name, "r", encoding="UTF-8") as lines:
    print("\n".join(tail(n, [line for line in lines.read().split("\n") if line])))