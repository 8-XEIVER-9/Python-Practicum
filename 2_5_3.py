N = int(input())
M = int(input())
move = (N - M) // 3
ans = []
while N >= M:
    ans.append(str(N))
    N -= move
print("; ".join(ans))
print("Старт!")