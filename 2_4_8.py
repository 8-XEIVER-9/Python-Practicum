n = int(input())
ans_n = ""
ans_s = 0
for i in range(n):
    t_name = input()
    t_s = sum(list(map(int, input())))
    if t_s >= ans_s:
        ans_s = t_s
        ans_n = t_name
print(ans_n)