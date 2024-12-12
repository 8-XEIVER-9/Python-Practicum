summ = 0
with open('numbers.num', 'rb') as file:
    while (chunk := file.read(2)):
        summ += int.from_bytes(chunk)

print(summ % 65536)