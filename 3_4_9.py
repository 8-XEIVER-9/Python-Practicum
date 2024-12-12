from itertools import product
n = int(input())
table_in_line = [x * y for x, y in product(range(1, n + 1), repeat=2)]
start = 0
end = n
for _ in range(n):
    print(*table_in_line[start:end])
    start += n
    end += n