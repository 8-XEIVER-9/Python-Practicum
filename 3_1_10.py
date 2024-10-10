maxx = 0
char = ""
all_w = ""
while (line := input()) != "ФИНИШ":
    line = line.replace(" ", "")
    all_w += line
all_w = all_w.lower()
for ch in all_w:
    if ch == " ":
        continue
    if all_w.count(ch) > maxx:
        maxx = all_w.count(ch)
        char = ch
    elif all_w.count(ch) == maxx:
        if ch < char:
            char = ch
print(char)