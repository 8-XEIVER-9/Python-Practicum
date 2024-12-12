d = dict()
while (line := input()):
    words = line.split()
    for word in words:
        key = word[-1].capitalize()
        d[key] = d.get(key, "") + " " + word.lower()
for key, item in d.items():
    print(f"{key} - {", ".join(sorted(set(item.split())))}")