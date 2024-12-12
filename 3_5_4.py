from sys import stdin

lines = stdin.readlines()
request = lines[-1].rstrip().lower()
lines.pop()
for line in lines:
    if request in line.lower():
        print(line.rstrip())