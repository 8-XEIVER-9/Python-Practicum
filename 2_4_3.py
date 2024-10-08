n = int(input())
k = 1
n1 = 0
n2 = n
while n > 0:
    for i in range(k):
        n1 += 1
        if n1 > n2:
            break
        print(n1, end=" ")
    print()
    n -= k
    k += 1