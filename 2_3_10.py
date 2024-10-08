way = input()
how = int(input())
x = 0
y = 0
while True:
    if way[0] == "С":
        y += how
    elif way[0] == "Ю":
        y -= how
    elif way[0] == "В":
        x += how
    elif way[0] == "З":
        x -= how
    way = input()
    if way != "СТОП":
        how = int(input())
    else:
        break
print(y)
print(x)