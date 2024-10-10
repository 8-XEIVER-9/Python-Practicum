while line := input():
    if line[0] == "#":
        continue
    if line.find("#") != -1:
        print(line[:line.find("#")])
    else:
        print(line)