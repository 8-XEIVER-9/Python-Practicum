ans = {}
while (line := input()):
    data = line.split()
    for unit in data:
        if unit in ans:
            ans[unit] += 1
        else:
            ans[unit] = 1
for key, value in ans.items():
    print(key, value)