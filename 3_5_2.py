from sys import stdin
summ = 0
cnt = 0
for num in stdin:
    cnt += 1
    height = list(map(int, num.rstrip().split()[1:]))
    summ += height[1] - height[0]
print(round(summ / cnt))