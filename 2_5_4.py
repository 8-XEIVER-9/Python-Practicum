n = int(input())
prev = int(input())
min_ans = 10**9
for _ in range(n - 1):
    current = int(input())
    if current > prev and current < min_ans:
        min_ans = current
    prev = current
print(min_ans)
