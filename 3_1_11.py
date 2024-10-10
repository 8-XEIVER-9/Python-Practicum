n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
need = input()
for line in lines:
    if need.lower() in line.lower():
        print(line)