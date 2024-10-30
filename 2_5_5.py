n = int(input())
sum_mid = 0
for _ in range(n):
    prom = []
    cnt = 0
    while (cur := input()) != "stop":
        cnt += 1
        prom.append(int(cur))
    prom_sum = sum(prom) / cnt
    sum_mid += prom_sum
print(f"{sum_mid:.2f}")

