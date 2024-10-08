n = int(input())
summ = 0
for i in range(n):
    summ += sum(list(map(int, input())))
print(summ)