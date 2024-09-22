first_num = int(input())
second_num = int(input())
first_digit = ((first_num % 10) + (second_num % 10)) % 10
second_digit = ((first_num // 10 % 10) + (second_num // 10 % 10)) % 10
third_digit = ((first_num // 100) + (second_num // 100)) % 10
print(f'{third_digit}{second_digit}{first_digit}')