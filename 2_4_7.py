n = int(input())
p = [3 + i for i in range(n)]
for i in range(n):
    secs = p[i]
    for j in range(p[i]):
        print(f"До старта {secs} секунд(ы)")
        secs -= 1
    print(f"Старт {i + 1}!!!")