n = int(input())
cnt = 0
for _ in range(n):
    line = input()
    cnt += line.count("зайка")
print(cnt)