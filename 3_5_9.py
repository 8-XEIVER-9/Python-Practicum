f1 = input()
f2 = input()

with open(f1, encoding="UTF-8") as f1:
    lines = f1.read()

while "\t" in lines:
    lines = lines.replace("\t", "")
while "  " in lines:
    lines = lines.replace("  ", " ")

lines = "\n".join(string.strip() for string in lines.split("\n") if string)

with open(f2, "w", encoding="UTF-8") as f2:
    f2.write(lines)