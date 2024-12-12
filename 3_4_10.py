from itertools import product
n = int(input())
print("А Б В")
for comb in product(range(1, n), repeat=3):
    if sum(comb) == n:
        print(*comb)