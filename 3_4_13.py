from itertools import permutations
n = int(input())
people = []
for _ in range(n):
    people.append(input())
people.sort()
for comb in permutations(people):
    print(", ".join(comb))