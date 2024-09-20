str3 = [input() for i in range(3)]
zayka = []
for n in str3:
    if "зайка" in n:
        zayka.append(n)
print(min(zayka), len(min(zayka)))