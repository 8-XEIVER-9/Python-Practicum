n = int(input())
d = "абв"
for _ in range(n):
    word = input()
    if word[0] in d:
        continue
    else:
        print("NO")
        exit()
print("YES")