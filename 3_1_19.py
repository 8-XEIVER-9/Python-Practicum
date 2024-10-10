line = list(input().split())
op = "+-*"
while "*" in line or "+" in line or "-" in line:
    for i in range(len(line)):
        if line[i] not in op:
            continue
        else:
            match line[i]:
                case "*":
                    line[i - 1] = str(int(line[i - 1]) * int(line[i - 2]))
                    line.pop(i - 2)
                    line.pop(i - 1)
                    break
                case "+":
                    line[i - 1] = str(int(line[i - 1]) + int(line[i - 2]))
                    line.pop(i - 2)
                    line.pop(i - 1)
                    break
                case "-":
                    line[i - 1] = str(int(line[i - 2]) - int(line[i - 1]))
                    line.pop(i - 2)
                    line.pop(i - 1)
                    break
print(line[-1])