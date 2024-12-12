from sys import stdin
summ = 0
for num in stdin:
    summ += sum(map(int, num.rstrip().split()))
print(summ)
