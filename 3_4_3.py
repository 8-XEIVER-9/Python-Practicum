from itertools import count
n1, n2, n3 = list(map(float, input().split()))

for value in count(n1, n3):
    if value <= n2:
        print(f"{value:.2f}")
    else:
        break
