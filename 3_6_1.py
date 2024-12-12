n = int(input())
for _ in range(n):
    A, B, line = input().split("&")
    res = ""
    need_line = line[int(A):]
    for i in range(0, len(need_line), 2):
        if len(res) == int(B):
            break
        else:
            res += need_line[i]
    print(res)
