while line := input():
    if line[:2] == "##":
        line = line[2:]
    if line[-3:] == "@@@":
        continue
    print(line)