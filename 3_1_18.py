line = input() + "a"
while line != "a":
    prev = line[0]
    i = 0
    while line[i] == prev:
        i += 1
    print(prev, i)
    line = line[i:]