n = int(input())
min_word = "яяяяяяяяяяяяяяяяяя"
for i in range(n):
    name = input()
    min_word = min(min_word, name)
print(min_word)