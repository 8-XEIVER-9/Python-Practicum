n = sorted(list((map(str, input()))))
if n[0] == "0":
    print(n[1] + n[0], n[-1] + n[-2])
else:
    print(n[0] + n[1], n[-1] + n[-2])