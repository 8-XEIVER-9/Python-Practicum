def check(a, b, c):
    return a + b > c


bar1 = int(input())
bar2 = int(input())
bar3 = int(input())
if check(bar1, bar2, bar3) and check(bar2, bar3, bar1) and check(bar1, bar3, bar2):
    print("YES")
else:
    print("NO")