length = int(input())
n = int(input())
length_c = length - 3
for _ in range(n):
    line = input()
    if len(line) < length_c:
        print(line)
        length_c -= len(line)
    else:
        print(line[:length_c] + "...")
        break
