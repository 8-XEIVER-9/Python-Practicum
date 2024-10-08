cnt = 0
n = input()
while n != "Приехали!":
    if "зайка" in n:
        cnt += 1
    n = input()
print(cnt)