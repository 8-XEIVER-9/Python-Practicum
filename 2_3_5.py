n = float(input())
summ = 0
while n != 0:
    if n >= 500:
        summ += n * 0.9
    else:
        summ += n
    n = float(input())
print(summ)