from itertools import combinations
n = int(input())
kids = []
for _ in range(n):
    kids.append(input())
for first, second in combinations(kids, r=2):
    print(f"{first} - {second}")
