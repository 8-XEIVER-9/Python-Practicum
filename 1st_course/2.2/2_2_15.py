n1 = input()
n2 = input()
n3 = n1 + n2
a = sorted([x for x in n3])
new = a[-1] + str((int(a[1]) + int(a[2])) % 10) + a[0]
print(new)