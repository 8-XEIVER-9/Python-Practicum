sides = sorted([int(input()) for x in range(3)])
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("100%")
elif sides[0]**2 + sides[1]**2 > sides[2]**2:
    print("крайне мала")
else:
    print("велика")