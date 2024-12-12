from itertools import product

n = int(input())
digits = []

for _ in range(n):
    line = input()
    digits.append(line.split(", "))
combinations = product(*digits)
numbers = set(int("".join(combo)) for combo in combinations)
for number in sorted(numbers):
    print(number)