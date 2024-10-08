n = int(input())
cnt = 0
for i in range(n):
    f = 0
    while (h := input()) != "ВСЁ":
        if h == "зайка" and f == 0:
            cnt += 1
            f = 1
print(cnt)