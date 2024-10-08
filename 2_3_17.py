even = "24680"
n = input()
new = ""
for x in n:
    if x not in even:
        new += x
print(new)