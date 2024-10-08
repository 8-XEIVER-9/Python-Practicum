def check(n):
    return n == n[::-1]


n = int(input())
cnt = 0
for _ in range(n):
    nm = input()
    if check(nm):
        cnt += 1
print(cnt)