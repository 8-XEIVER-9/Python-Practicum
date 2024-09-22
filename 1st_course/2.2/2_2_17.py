a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c
if a == b == c == 0:
    print('Infinite solutions')
elif a == 0 and b != 0 and c != 0:
    print(f'{(-1) * (c / b):.2f}')
elif a == b == 0:
    print('No solution')
elif a == c == 0:
    print(0)
else:
    if D > 0:
        x1 = ((-1) * b + D**0.5) / 2 / a
        x2 = ((-1) * b - D**0.5) / 2 / a
        print(f"{min(x1, x2):.2f} {max(x1, x2):.2f}")
    elif D == 0:
        print(f"{((-1) * b) / 2 * a:.2f}")
    else:
        print("No solution")
