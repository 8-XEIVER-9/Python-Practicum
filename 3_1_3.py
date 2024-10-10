def sp(line, length):
    return line[:length - 3][-1] != " "


def check(line, length):
    if len(line) > length:
        return line[:length - 3] + sp(line, length) * "..."
    else:
        return line


length = int(input())
n = int(input())
for _ in range(n):
    print(check(input(), length))