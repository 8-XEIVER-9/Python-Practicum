num1 = int(input())
num2 = int(input())
len_l = len(input())
if len_l % 6 == 0:
    print(num1 + num2)
elif len_l % 3 == 0:
    print(num1 - num2)
elif len_l % 2 == 0:
    print(num1 * num2)
else:
    print(num1 // num2)