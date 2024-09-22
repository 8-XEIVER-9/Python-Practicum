num = input()
first = int(num[-1]) + int(num[-2])
second = int(num[0]) + int(num[1])
print(str(max(first, second)) + str(min(first, second)))